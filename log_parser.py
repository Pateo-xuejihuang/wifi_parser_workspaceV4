#!/usr/bin/env python3
import struct
import re
import sys
import json
import argparse
from typing import List, Dict, Union, Optional
import io
from contextlib import redirect_stdout

try:
    from scapy.layers.dot11 import Dot11Elt
except ImportError:
    print("错误: 无法导入 Scapy。请先运行 'pip install scapy'。", file=sys.stderr)
    sys.exit(1)

# 从我们的配置文件中导入定义
try:
    from definitions import VENDOR_SUBCMD_ENUMS
except ImportError:
    print("错误: 无法找到 'definitions.py' 文件。", file=sys.stderr)
    print("请确保 'definitions.py' 和 'log_parser.py' 在同一个目录下。", file=sys.stderr)
    sys.exit(1)

# --- 核心逻辑区域 ---

NLA_F_NESTED = 0x8000
NLA_TYPE_MASK = 0x3FFF

class NLA:
    def __init__(self, nla_type: int, nla_len: int, payload: bytes):
        self.nla_type_raw = nla_type; self.nla_len = nla_len; self.payload = payload
        self.children: List[NLA] = []; self.is_nested = bool(nla_type & NLA_F_NESTED)
        self.type_id = nla_type & NLA_TYPE_MASK

def align4(x: int) -> int: return (x + 3) & ~3

def parse_nla(data: bytes) -> List[NLA]:
    pos = 0; results = []
    while pos + 4 <= len(data):
        try: nla_len, nla_type = struct.unpack_from('<HH', data, pos)
        except struct.error: break
        if nla_len < 4: break
        if pos + nla_len > len(data):
            payload = data[pos + 4:]; nla = NLA(nla_type, nla_len, payload)
            if nla.is_nested: nla.children = parse_nla(payload)
            results.append(nla); break
        else:
            payload = data[pos + 4: pos + nla_len]; nla = NLA(nla_type, nla_len, payload)
            if nla.is_nested: nla.children = parse_nla(payload)
            results.append(nla); pos += align4(nla_len)
    return results

def get_next_rule_key(subcmd_def: Dict, current_rule_key: Optional[str], type_id: int) -> Optional[str]:
    if not current_rule_key: return None
    nested_rules = subcmd_def.get("nested_rules", {})
    transition_map = nested_rules.get(current_rule_key)
    if not transition_map: return current_rule_key
    return transition_map.get(type_id, transition_map.get("*"))

# log_parser.py 中需要更新的函数

def format_data_value(payload: bytes, data_type: str = 'hex') -> tuple[Union[str, int], str]:
    """【已升级】根据明确的数据类型来解析payload，支持有符号和无符号整数。"""
    hex_data = ' '.join(f"{b:02x}" for b in payload)
    if not payload: return "empty", hex_data

    try:
        # 无符号整数 (Unsigned)
        if data_type == 'u8' and len(payload) == 1:
            return struct.unpack('<B', payload)[0], hex_data
        if data_type == 'u16' and len(payload) == 2:
            return struct.unpack('<H', payload)[0], hex_data
        if data_type == 'u32' and len(payload) == 4:
            return struct.unpack('<I', payload)[0], hex_data
        if data_type == 'u64' and len(payload) == 8:
            return struct.unpack('<Q', payload)[0], hex_data
            
        # --- 新增：有符号整数 (Signed) ---
        if data_type == 's8' and len(payload) == 1:
            return struct.unpack('<b', payload)[0], hex_data
        if data_type == 's16' and len(payload) == 2:
            return struct.unpack('<h', payload)[0], hex_data
        if data_type == 's32' and len(payload) == 4:
            return struct.unpack('<i', payload)[0], hex_data
        if data_type == 's64' and len(payload) == 8:
            return struct.unpack('<q', payload)[0], hex_data

        # 字符串和MAC地址
        if data_type == 'string':
            return payload.rstrip(b'\x00').decode('utf-8', errors='ignore'), hex_data
        if data_type == 'mac_address' and len(payload) == 6:
            return ':'.join(f'{b:02x}' for b in payload), hex_data
            
    except (struct.error, UnicodeDecodeError):
        # 如果解析失败，则回退到十六进制
        pass

    # 默认或回退情况
    return hex_data, hex_data

def parse_ies_with_scapy(payload: bytes) -> List[Dict]:
    """【最终版】捕获 Scapy 的 .show() 输出，并添加一个格式化标志。"""
    if not payload:
        return []

    try:
        all_ies = Dot11Elt(payload)
        f = io.StringIO()
        with redirect_stdout(f):
            all_ies.show()
        captured_output = f.getvalue()
        
        # --- 这是关键修改 ---
        # 返回的字典里加一个特殊的键 'format'
        parsed_ies = [
            {"name": "--- Scapy Raw Output ---", "value": captured_output, "format": "preformatted"}
        ]
        
    except Exception as e:
        parsed_ies = [{"name": "Scapy Parse Error", "value": str(e)}]

    return parsed_ies

# --- NEW FUNCTION ---
# 新增一个函数，用于将原始字节 payload 解析为基于偏移量定义的结构体
def parse_struct(payload: bytes, struct_def: Dict) -> List[Dict]:
    """将原始字节 payload 解析为基于偏移量定义的C风格结构体。"""
    children = []
    # 保证按偏移量顺序解析
    for offset in sorted([k for k in struct_def.keys() if isinstance(k, int)]):
        field_def = struct_def[offset]
        field_name = field_def.get("name", f"Field@Offset{offset}")
        field_type = field_def.get("type", "hex")
        
        # 根据类型推断字段大小
        type_sizes = {'u8': 1, 'u16': 2, 'u32': 4, 'u64': 8}
        size = type_sizes.get(field_type)
        
        # 如果无法确定大小（例如string），则无法在结构体中切片，暂时跳过
        if size is None: continue
        
        if offset + size <= len(payload):
            field_payload = payload[offset : offset + size]
            value, hex_value = format_data_value(field_payload, field_type)
            children.append({"name": field_name, "value": value, "hex": hex_value})
            
    return children

# --- MODIFIED FUNCTION ---
# 修改 build_translated_tree 以识别和处理 "struct" 类型
def build_translated_tree(nlas: List[NLA], subcmd_def: Dict, current_rule_key: Optional[str]) -> List[Dict]:
    tree = []
    for nla in nlas:
        attr_name = f"Type {nla.type_id} [UNKNOWN]"; data_type = 'hex'; attr_def = None
        if current_rule_key:
            current_map = subcmd_def.get(current_rule_key, {})
            attr_def = current_map.get(nla.type_id)
            if attr_def is None and "*" in current_map:
                attr_def = current_map["*"]
                attr_name = f"{attr_def.get('name', 'UNKNOWN')}_{nla.type_id}"
                data_type = attr_def.get('type', 'hex')
            elif isinstance(attr_def, dict):
                attr_name = attr_def.get('name', attr_name)
                data_type = attr_def.get('type', 'hex')

        node = {"name": attr_name, "type_id": nla.type_id}
        
        # 检查这是否是我们定义的特殊 "struct" 类型
        is_custom_struct = isinstance(attr_def, dict) and attr_def.get('type') == 'struct'
        # --- 新增：检查是否是我们的特殊 IEs 类型 ---
        is_assoc_ies = isinstance(attr_def, dict) and attr_def.get('type') == 'assoc_req_ies'
        if is_assoc_ies:
            # 如果是，使用 Scapy 解析函数
            node["children"] = parse_ies_with_scapy(nla.payload)

        if is_custom_struct:
            # 如果是，使用新的 parse_struct 函数来解析 payload
            next_rule_key = get_next_rule_key(subcmd_def, current_rule_key, nla.type_id)
            struct_definition = subcmd_def.get(next_rule_key, {})
            node["children"] = parse_struct(nla.payload, struct_definition)
        elif nla.is_nested:
            # 否则，如果它是一个标准的嵌套属性，使用旧逻辑
            next_rule_key = get_next_rule_key(subcmd_def, current_rule_key, nla.type_id)
            node["children"] = build_translated_tree(nla.children, subcmd_def, next_rule_key)
        else:
            # 否则，它是一个简单值
            value, hex_value = format_data_value(nla.payload, data_type)
            node["value"] = value; node["hex"] = hex_value
            
        tree.append(node)
    return tree

# --- 渲染器区域 (无变化) ---

def render_to_txt(event: Dict, file=sys.stdout):
    print(f"\n{'='*20} Parsing Event from Log Line ~{event['line_number']} (subcmd {event['subcmd']}) {'='*20}", file=file)
    print(f"Timestamp: {event['data_timestamp']} (Handler: {event['handler_timestamp']})", file=file)
    print("-" * (44 + len(str(event['subcmd'])) + len(str(event['line_number']))), file=file)
    
    def _render_tree_txt(tree: List[Dict], depth=0):
        indent = '  ' * depth
        for node in tree:
            display_name = node['name']
            if "children" in node:
                print(f"{indent}{display_name}:", file=file)
                _render_tree_txt(node["children"], depth + 1)
            else:
                value, hex_val = node.get('value', 'N/A'), node.get('hex', 'N/A')
                data_str = f'"{value}" ({hex_val})' if isinstance(value, str) and value != hex_val else f"{value} ({hex_val})"
                print(f"{indent}{display_name}: {data_str}", file=file)
    
    _render_tree_txt(event['tree'])

def render_to_json(data: List[Dict], filepath: str):
    try:
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"JSON 输出已保存到: {filepath}")
    except Exception as e:
        print(f"错误: 无法写入JSON文件 {filepath}: {e}", file=sys.stderr)

def hex_to_bytes(hexstr: str) -> bytes:
    return bytes.fromhex(hexstr.replace(' ', '').replace('\n', '').strip())

# --- 主程序逻辑 (无变化) ---

def process_log_file(filename: str, vendor_enums: Dict, args: argparse.Namespace):
    ts_re = re.compile(r"^\[(.*?)\]")
    handler_re = re.compile(r"nl80211_response_handler:.*subcmd\s+(\d+)")
    data_re = re.compile(r"NL80211_ATTR_VENDOR_DATA.*:\s*(.*)")
    all_parsed_events, current_event_context = [], {}
    try:
        with open(filename, 'r') as f:
            for line_num, line in enumerate(f, 1):
                ts_match = ts_re.search(line); current_timestamp = ts_match.group(1) if ts_match else "N/A"
                handler_match = handler_re.search(line)
                if handler_match:
                    current_event_context = {"subcmd": int(handler_match.group(1)), "handler_timestamp": current_timestamp}
                    continue
                if "subcmd" in current_event_context:
                    data_match = data_re.search(line)
                    if data_match:
                        ctx = current_event_context
                        subcmd_def = vendor_enums.get(ctx["subcmd"], {})
                        initial_rule_key = subcmd_def.get("initial_rule")
                        if not initial_rule_key:
                             print(f"警告: subcmd {ctx['subcmd']} 在 definitions.py 中缺少 'initial_rule'，跳过解析。")
                             current_event_context = {}; continue

                        nlas = parse_nla(hex_to_bytes(data_match.group(1).strip()))
                        translated_tree = build_translated_tree(nlas, subcmd_def, initial_rule_key)
                        
                        event_data = {
                            "line_number": line_num, "handler_timestamp": ctx["handler_timestamp"],
                            "data_timestamp": current_timestamp, "subcmd": ctx["subcmd"],
                            "subcmd_name": subcmd_def.get("name", "UNKNOWN"), "tree": translated_tree
                        }
                        all_parsed_events.append(event_data)
                        current_event_context = {}
    except FileNotFoundError: print(f"错误: 文件未找到 -> '{filename}'", file=sys.stderr); return
    
    if args.output_txt:
        with open(args.output_txt, 'w', encoding='utf-8') as txt_file:
            for event in all_parsed_events: render_to_txt(event, file=txt_file)
        print(f"TXT 输出已保存到: {args.output_txt}")
    elif not args.output_json:
        for event in all_parsed_events: render_to_txt(event)
    if args.output_json: render_to_json(all_parsed_events, args.output_json)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="解析 NL80211 Vendor Command 日志。")
    parser.add_argument("logfile", help="要解析的日志文件路径。")
    parser.add_argument("--output-txt", help="可选：保存TXT输出的文件路径。")
    parser.add_argument("--output-json", help="可选：保存JSON输出的文件路径。")
    args = parser.parse_args()
    process_log_file(args.logfile, VENDOR_SUBCMD_ENUMS, args)
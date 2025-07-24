#!/usr/bin/env python3
import json
import argparse
import os
from datetime import datetime
from typing import Dict, List, Any, Callable

# --- 1. 计算函数工具箱 (The Calculation Engine) ---

def calculate_duration(inputs: List[Any], params: Dict) -> str:
    """计算两个jiffies时间戳之间的时长（秒）。"""
    try:
        start_jiffies, end_jiffies = float(inputs[0]), float(inputs[1])
        hz = params.get("hz", 100)
        if end_jiffies >= start_jiffies:
            return f"{(end_jiffies - start_jiffies) / hz:.3f} 秒"
    except (ValueError, TypeError, IndexError, AttributeError):
        pass
    return "N/A"

def convert_kbps_to_mbps(inputs: List[Any], params: Dict) -> str:
    """【最终修正版】将速率从 Kbps 转换为 Mbps，能处理数字和字符串输入。"""
    try:
        rate_kbps = float(inputs[0])
        return f"{rate_kbps / 1000.0:.2f} Mbps"
    except (ValueError, TypeError, IndexError, AttributeError):
        return "N/A"

def clean_and_format_channel_flags(inputs: List[Any], params: Dict) -> str:
    """
    清理并格式化信道标志位。
    它会移除驱动内部的私有标志，并以十六进制格式显示。
    """
    try:
        # 输入是原始的 flags 整数值
        raw_flags = int(inputs[0])
        
        # 定义我们想要移除的驱动私有标志位
        PRIVATE_DRIVER_FLAG = 0x80000
        
        # 使用位掩码进行清理
        clean_flags = raw_flags & ~PRIVATE_DRIVER_FLAG
        
        # 以十六进制字符串格式返回结果
        return f"0x{clean_flags:04x}" # 例如: 0x01a0
        
    except (ValueError, TypeError, IndexError, AttributeError):
        # 如果输入不是有效的数字，则返回 N/A
        return "N/A"

def debug_passthrough(inputs: List[Any], params: Dict) -> str:
    """
    一个用于调试的“透传”函数。
    它会返回它收到的输入的真实、明确的字符串表示。
    """
    # repr() 函数能给出变量最无歧义的表示，例如：
    # [524704] -> "[524704]"
    # [None]   -> "[None]"
    # []       -> "[]"
    return f"Input: {repr(inputs)}"

# -- 计算函数注册表 --
CALCULATION_FUNCTIONS: Dict[str, Callable] = {
    "duration": calculate_duration,
    "kbps_to_mbps": convert_kbps_to_mbps,  # <--- 我们将使用这个键 "kbps_to_mbps"
    "clean_channel_flags": clean_and_format_channel_flags,
    "debug_passthrough": debug_passthrough,
}

# --- 1. 样式与HTML模板定义 (Dashboard Design) ---

CSS_STYLES = """
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;700&family=JetBrains+Mono:wght@400;500&display=swap');
    :root {
        --bg-color: #f8f9fa;
        --card-bg: #ffffff;
        --border-color: #dee2e6;
        --header-bg: #f1f3f5;
        --text-color: #212529;
        --text-muted-color: #6c757d;
        --accent-color: #007bff;
        --label-color: #1971c2;
        --value-color: #d9480f;
        --font-sans: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
        --font-mono: 'JetBrains Mono', SFMono-Regular, Menlo, Monaco, Consolas, monospace;
    }
    *, *::before, *::after { box-sizing: border-box; }
    body {
        font-family: var(--font-sans); background-color: var(--bg-color); color: var(--text-color);
        line-height: 1.6; margin: 0; padding: 2em;
    }
    .container { max-width: 1200px; margin: 0 auto; }
    h1, h2 { font-weight: 500; color: #343a40; border-bottom: 1px solid var(--border-color); padding-bottom: 0.5em; margin-top: 2em; margin-bottom: 1em;}
    
    /* 过滤区域 */
    .filter-container { background: var(--card-bg); padding: 1.5em; border-radius: 8px; margin-bottom: 2em; border: 1px solid var(--border-color); }
    .filter-controls { display: flex; flex-wrap: wrap; gap: 10px 20px; }
    .filter-controls label { display: flex; align-items: center; cursor: pointer; font-size: 0.9em; }
    .filter-controls input { margin-right: 8px; accent-color: var(--accent-color); }
    .filter-actions { margin-top: 1em; border-top: 1px solid var(--border-color); padding-top: 1em; display: flex; gap: 10px; }
    .filter-btn { background: var(--accent-color); color: white; border: none; padding: 8px 15px; border-radius: 5px; cursor: pointer; font-size: 0.9em; transition: background 0.2s; }
    .filter-btn:hover { background: #0056b3; }
    .filter-btn.secondary { background: #6c757d; }
    .filter-btn.secondary:hover { background: #5a6268; }

    /* 事件统计区块 - 可折叠设计 */
    .summary-section { border: 1px solid var(--border-color); border-radius: 8px; background: var(--card-bg); margin-bottom: 2em; }
    .summary-header { padding: 12px 18px; cursor: pointer; font-weight: 500; color: var(--label-color); border-bottom: 1px solid var(--border-color); display: flex; align-items: center; }
    .summary-header::after { content: '›'; font-size: 2em; color: var(--accent-color); margin-left: auto; transition: transform 0.3s ease; }
    .summary-header.active::after { transform: rotate(90deg); }
    .summary-body { max-height: 0; overflow: hidden; transition: max-height 0.4s ease-out, padding 0.4s ease-out; padding: 0 1.5em; background-color: #fcfcfc; }
    .summary-body.active { max-height: 4000px; padding: 1.5em; }
    .summary-table { width: 100%; border-collapse: collapse; background: none; border-radius: 0; border: none; }
    .summary-table th, .summary-table td { padding: 12px 15px; text-align: left; border-bottom: 1px solid var(--border-color); font-size: 0.9em; }
    .summary-table thead { background-color: var(--header-bg); }
    .summary-table th { font-weight: 600; }
    .summary-table tbody tr:last-child td { border-bottom: none; }
    .subcmd-id { font-family: var(--font-mono); background-color: #e9ecef; padding: 2px 6px; border-radius: 4px; }

    /* 消息列表 - 紧凑设计 */
    .event-list { border: 1px solid var(--border-color); border-radius: 8px; margin-top: 1em; background: var(--card-bg); }
    .event-item { border-bottom: 1px solid var(--border-color); }
    .event-item:last-child { border-bottom: none; }
    .event-header { padding: 10px 15px; cursor: pointer; display: flex; align-items: center; gap: 1em; transition: background-color 0.2s ease; }
    .event-header:hover { background-color: var(--header-bg); }
    .event-timestamp { font-family: var(--font-mono); font-weight: 500; color: var(--text-color); flex-shrink: 0; }
    .event-title { font-weight: 500; flex-grow: 1; } /* 占据剩余空间 */
    .event-header::after { content: '›'; font-size: 2em; transition: transform 0.3s ease; }
    .event-header.active::after { transform: rotate(90deg); }
    
    .event-body { max-height: 0; overflow: hidden; transition: max-height 0.4s ease-out, padding 0.4s ease-out; padding: 0 1.5em; background-color: #fcfcfc; }
    .event-body.active { max-height: 4000px; padding: 1.5em; }

    .tree-container { font-family: var(--font-mono); font-size: 0.9em; }
    .attr-node { padding-left: 20px; position: relative; }
    .attr-node::before { content: ''; position: absolute; left: 0; top: 0; border-left: 1px solid #ced4da; height: 100%; }
    .attr-node:last-child::before { height: 1.1em; }
    .attr-row { position: relative; display: flex; align-items: baseline; padding: 2px 0; }
    .attr-row::before { content: ''; position: absolute; left: -20px; top: 1.1em; border-top: 1px solid #ced4da; width: 15px; }
    .label { color: var(--label-color); margin-right: 1ch; }
    .value { color: var(--value-color); font-weight: 500; }
</style>
"""

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>WLAN Log Analysis Report</title>
    {styles}
</head>
<body>
    <div class="container">
        <h1>WLAN Log Analysis Report</h1>
        
        {filter_section}

        <div class="summary-section">
            <div class="summary-header">SubCmd Event Summary</div>
            <div class="summary-body">
                <table class="summary-table">
                    <thead>
                        <tr>
                            <th>Event Name</th>
                            <th>SubCmd ID</th>
                            <th>Count</th>
                        </tr>
                    </thead>
                    <tbody>
                        {summary_table_rows}
                    </tbody>
                </table>
            </div>
        </div>

        <h2>Event Details</h2>
        <div id="event-list-container" class="event-list">
            {event_items}
        </div>
    </div>
    {javascript_code}
</body>
</html>
"""

JAVASCRIPT_CODE = """
<script>
    document.addEventListener('DOMContentLoaded', () => {
        const headers = document.querySelectorAll('.event-header');
        const filterControls = document.getElementById('filter-controls');
        const eventItems = document.querySelectorAll('.event-item');
        const selectAllBtn = document.getElementById('select-all');
        const deselectAllBtn = document.getElementById('deselect-all');
        
        // 折叠/展开逻辑
        headers.forEach(header => {
            header.addEventListener('click', () => {
                header.classList.toggle('active');
                header.nextElementSibling.classList.toggle('active');
            });
        });
        // SubCmd Event Summary区块折叠
        const summaryHeader = document.querySelector('.summary-header');
        const summaryBody = document.querySelector('.summary-body');
        if (summaryHeader && summaryBody) {
            summaryHeader.addEventListener('click', () => {
                summaryHeader.classList.toggle('active');
                summaryBody.classList.toggle('active');
            });
        }

        // 过滤逻辑
        const applyFilter = () => {
            const checkedSubCmds = new Set();
            filterControls.querySelectorAll('input[type="checkbox"]:checked').forEach(checkbox => {
                checkedSubCmds.add(checkbox.dataset.subcmdId);
            });

            eventItems.forEach(item => {
                if (checkedSubCmds.has(item.dataset.subcmdId)) {
                    item.style.display = '';
                } else {
                    item.style.display = 'none';
                }
            });
        };

        if (filterControls) {
            filterControls.addEventListener('change', applyFilter);

            selectAllBtn.addEventListener('click', () => {
                filterControls.querySelectorAll('input[type="checkbox"]').forEach(cb => cb.checked = true);
                applyFilter();
            });

            deselectAllBtn.addEventListener('click', () => {
                filterControls.querySelectorAll('input[type="checkbox"]').forEach(cb => cb.checked = false);
                applyFilter();
            });
        }
    });
</script>
"""

# --- 3. 通用事件预处理器 (Generic Event Preprocessor) ---

# 【新增改动】这是一个新的辅助函数，用于递归地“扁平化”整个事件树
def _flatten_tree_for_data_lookup(nodes: List[Dict]) -> Dict[str, Any]:
    """
    递归地遍历节点树，并将其所有成员扁平化到一个字典中，以便于按名称快速查找值。
    """
    data_map = {}
    
    def recurse(node_list: List[Dict]):
        for node in node_list:
            # 如果节点有值，就存入字典
            if 'value' in node:
                data_map[node['name']] = node.get('value')
            # 如果节点有子节点，就递归进入子节点列表
            if 'children' in node and isinstance(node['children'], list):
                recurse(node['children'])
                
    recurse(nodes)
    return data_map

def preprocess_event_tree(event: Dict, display_defs: Dict) -> Dict:
    """
    【已重构为通用引擎】
    预处理事件的属性树，根据定义动态执行计算并注入虚拟属性。
    此版本现在可以从嵌套结构中读取数据。
    """
    subcmd_name = event['subcmd_name']
    attr_defs = display_defs.get(subcmd_name, {}).get('attributes', {})
    if not attr_defs: return event

    # 【核心改动】使用新的辅助函数来构建一个可以查找嵌套值的 data_map
    data_map = _flatten_tree_for_data_lookup(event['tree'])
    
    new_nodes = []

    for attr_name, attr_def in attr_defs.items():
        format_type = attr_def.get("format")
        if not format_type: continue

        # 动态查找计算函数
        calculation_func = CALCULATION_FUNCTIONS.get(format_type)
        if not calculation_func: continue
            
        # 准备输入和参数
        input_names = attr_def.get("inputs", [])
        params = attr_def.get("params", {})
        
        try:
            # 查找逻辑保持不变, 但现在 data_map 包含了嵌套数据
            input_values = [data_map.get(name) for name in input_names]
            
            # 【代码健壮性优化】如果任何一个输入数据没找到 (为None)，则跳过此次计算
            if any(v is None for v in input_values):
                continue

            # 执行计算
            computed_value = calculation_func(input_values, params)
            new_nodes.append({"name": attr_name, "value": computed_value})
        except Exception as e:
            print(f"⚠️ 计算属性 '{attr_name}' 时出错: {e}")
            new_nodes.append({"name": attr_name, "value": "计算错误"})

    if new_nodes:
        # 将新计算出的节点追加到树的顶层
        event['tree'].extend(new_nodes)
    return event

# --- 4. 其他所有函数 (render_tree_to_html, generate_report等) ---
# ... 以下所有函数均保持不变 ...
def get_display_mapping(subcmd_name: str, display_defs: Dict) -> Dict:
    return display_defs.get(subcmd_name, {})

def render_tree_to_html(nodes: List[Dict], subcmd_name: str, display_defs: Dict) -> str:
    """
    【最终修正版】渲染属性树到HTML。
    采用两段式渲染，确保已定义的属性按顺序显示，未定义的属性也能回退显示。
    """
    if not nodes: return ""
    html = '<div class="tree-container">'
    
    data_map = {node['name']: node for node in nodes}
    attr_defs = get_display_mapping(subcmd_name, display_defs).get("attributes", {})
    rendered_keys = set()  # 用来记录哪些key已经被第一阶段渲染

    # --- 第一段: 优先渲染在 display_definitions.js 中定义的属性 ---
    for attr_name, attr_def in attr_defs.items():
        node = data_map.get(attr_name)
        
        # 如果是计算出的虚拟节点，它在原始数据中不存在，但预处理后已加入data_map
        if not node:
            # 检查data_map中是否有预处理时加入的计算值
            if attr_name in data_map and isinstance(data_map[attr_name], dict) and 'value' in data_map[attr_name]:
                 node = data_map[attr_name]
            else:
                 continue # 如果节点不存在，则跳过

        if attr_def.get("display") == "none":
            rendered_keys.add(attr_name) # 标记为已处理，但什么也不显示
            continue

        label = attr_def.get("label", attr_name) # 使用定义的label
        
        # (这部分是通用的渲染逻辑)
        html += '<div class="attr-node"><div class="attr-row">'
        if "children" in node and node.get("children"):
            content = render_tree_to_html(node["children"], subcmd_name, display_defs)
            html += f'<span class="label">{label}:</span>{content}'
        else:
            value = node.get('value')
            if "values" in attr_def and str(value) in attr_def["values"]:
                mapped_value = attr_def["values"][str(value)]
                value_str = f'{mapped_value} ({value})'
            else:
                value_str = f'"{value}"' if isinstance(value, str) and value != "empty" else str(value)
            html += f'<span class="label">{label}:</span><span class="value">{value_str}</span>'
        html += '</div></div>'
        
        rendered_keys.add(attr_name) # 标记为已渲染

    # --- 第二段: 渲染任何未在定义文件中提及的、剩余的原始属性 ---
    for node in nodes:
        if node['name'] not in rendered_keys:
            label = node['name'] # 使用原始名称作为label
            
            # (复用通用的渲染逻辑)
            html += '<div class="attr-node"><div class="attr-row">'
            if "children" in node and node.get("children"):
                content = render_tree_to_html(node["children"], subcmd_name, display_defs)
                html += f'<span class="label">{label}:</span>{content}'
            else:
                value = node.get('value')
                value_str = f'"{value}"' if isinstance(value, str) and value != "empty" else str(value)
                html += f'<span class="label">{label}:</span><span class="value">{value_str}</span>'
            html += '</div></div>'
            
    html += '</div>'
    return html

def create_event_item_html(event: Dict, display_defs: Dict) -> str:
    subcmd_name = event['subcmd_name']
    subcmd_map = get_display_mapping(subcmd_name, display_defs)
    friendly_name = subcmd_map.get("friendly_name", subcmd_name)
    
    header = f"""
    <div class="event-header">
        <span class="event-timestamp">{event['data_timestamp'].split()[-1]}</span>
        <span class="event-title">{friendly_name}</span>
    </div>
    """
    body = f"""
    <div class="event-body">
        {render_tree_to_html(event['tree'], subcmd_name, display_defs)}
    </div>
    """
    return f'<div class="event-item" data-subcmd-id="{event["subcmd"]}">\n{header}\n{body}\n</div>'


def generate_filter_controls_html(summary: List) -> str:
    controls_html = ""
    for name, data in summary:
        subcmd_id = data['subcmd_id']
        controls_html += f"""
        <label>
            <input type="checkbox" data-subcmd-id="{subcmd_id}" checked>
            {name}
        </label>
        """
    return f"""
    <div class="filter-container">
        <h2>Filter Events</h2>
        <div id="filter-controls" class="filter-controls">
            {controls_html}
        </div>
        <div class="filter-actions">
            <button id="select-all" class="filter-btn">Select All</button>
            <button id="deselect-all" class="filter-btn secondary">Deselect All</button>
        </div>
    </div>
    """


def calculate_stats_and_summary(parsed_data: List[Dict], display_defs: Dict) -> List:
    summary = {}
    for event in parsed_data:
        subcmd_name, subcmd_id = event['subcmd_name'], event['subcmd']
        friendly_name = get_display_mapping(subcmd_name, display_defs).get("friendly_name", subcmd_name)
        
        if friendly_name not in summary:
            summary[friendly_name] = {"count": 0, "subcmd_id": subcmd_id}
        summary[friendly_name]["count"] += 1
        
    return sorted(summary.items(), key=lambda item: item[1]['subcmd_id'])


def generate_report(parsed_json_path: str, display_defs_path: str, output_html_path: str):
    try:
        with open(parsed_json_path, 'r', encoding='utf-8') as f:
            parsed_data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"❌ 错误: 无法读取或解析JSON文件 {parsed_json_path}. {e}"); return

    display_defs = {}
    try:
        with open(display_defs_path, 'r', encoding='utf-8') as f:
            js_content = f.read(); json_str = js_content.partition('=')[2].strip().rstrip(';')
            display_defs = json.loads(json_str)
    except Exception as e:
        print(f"⚠️ 警告: 无法解析显示定义文件 {display_defs_path}: {e}")

    summary = calculate_stats_and_summary(parsed_data, display_defs)
    summary_table_rows = "\n".join([f'<tr><td>{name}</td><td><span class="subcmd-id">{data["subcmd_id"]}</span></td><td>{data["count"]}</td></tr>' for name, data in summary])
    filter_section_html = generate_filter_controls_html(summary) if summary else ""

    processed_events = [preprocess_event_tree(event, display_defs) for event in parsed_data]
    event_items_html = "\n".join([create_event_item_html(event, display_defs) for event in processed_events])
    
    final_html = HTML_TEMPLATE.format(
        styles=CSS_STYLES,
        filter_section=filter_section_html,
        summary_table_rows=summary_table_rows,
        event_items=event_items_html,
        javascript_code=JAVASCRIPT_CODE
    )

    try:
        with open(output_html_path, 'w', encoding='utf-8') as f:
            f.write(final_html)
        print(f"✅ HTML报告已成功生成: {output_html_path}")
    except Exception as e:
        print(f"❌ 错误: 无法写入HTML报告文件: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="从JSON数据生成一个独立的、专业的、可交互的HTML报告。")
    parser.add_argument("json_file", nargs='?', default='parsed.json', help="输入的已解析JSON文件路径 (默认: parsed.json)")
    parser.add_argument("--definitions", default='display_definitions.js', help="显示定义JS文件的路径 (默认: display_definitions.js)")
    parser.add_argument("-o", "--output", default='report.html', help="输出的HTML报告文件路径 (默认: report.html)")
    
    args = parser.parse_args()
    generate_report(args.json_file, args.definitions, args.output)
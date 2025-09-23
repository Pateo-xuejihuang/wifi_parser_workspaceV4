#!/usr/bin/env python3
"""
WiFi调试日志解析器 - Web版本
支持上传wifidebug文件，在线解析，下载HTML报告
"""

import streamlit as st
import tempfile
import os
import sys
import zipfile
from pathlib import Path

# 添加当前目录到Python路径，确保能导入本地模块
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

try:
    from log_parser import process_log_file
    from report_generator import generate_report
    from definitions import VENDOR_SUBCMD_ENUMS
except ImportError as e:
    st.error(f"导入模块失败: {e}")
    st.stop()

def is_likely_wifidebug_file(filename: str, file_size: int) -> tuple[bool, str]:
    """检查上传的文件是否可能是wifidebug文件"""
    filename_lower = filename.lower()
    
    # 检查文件名模式
    wifidebug_patterns = [
        'wifidebug',
        'wifi_debug', 
        'wlan_debug',
        'cnss_fw_log',
        'host_driver_log'
    ]
    
    # 检查是否包含常见的wifidebug文件名模式
    is_likely = any(pattern in filename_lower for pattern in wifidebug_patterns)
    
    # 检查文件大小（wifidebug文件通常较大）
    if file_size < 1024:  # 小于1KB可能不是真正的日志文件
        return False, "⚠️ 文件过小，可能不是有效的WiFi调试日志"
    elif file_size > 50 * 1024 * 1024:  # 大于50MB
        return True, "⚠️ 文件较大，解析可能需要较长时间"
    elif is_likely:
        return True, "✅ 文件名符合WiFi调试日志模式"
    else:
        return True, "⚠️ 文件名不常见，请确认这是WiFi调试日志文件"

def main():
    st.set_page_config(
        page_title="WiFi调试日志解析器", 
        page_icon="📡",
        layout="wide"
    )
    
    st.title("📡 WiFi调试日志解析器")
    st.markdown("---")
    
    # 侧边栏信息
    with st.sidebar:
        st.header("ℹ️ 使用说明")
        st.markdown("""
        1. **上传文件**: 选择您的wifidebug日志文件
        2. **开始解析**: 点击解析按钮处理文件
        3. **下载报告**: 解析完成后下载HTML报告
        
        **支持的文件格式**:
        - `wifidebug` (无扩展名)
        - `wifidebug(1)`, `wifidebug(2)` 等编号文件
        
        **常见文件示例**:
        - ✅ `wifidebug`
        - ✅ `wifidebug copy`  
        - ✅ `wifidebug(1)`
        - ✅ `wifidebug(2)`
        - ✅ `wifi_debug.log`
        """)
        
        st.header("🔧 项目信息")
        st.markdown("""
        **技术栈**: Python + Streamlit
        **架构**: 数据驱动设计
        **适用平台**: 高通车载平台 QCA8397
        """)
    
    # 主界面
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.header("📁 文件上传")
        uploaded_file = st.file_uploader(
            "选择wifidebug文件",
            type=None,  # 允许所有文件类型
            help="支持上传wifidebug文件（包括无扩展名文件）和各种格式：wifidebug, wifidebug(1), wifidebug(2), .txt, .log等"
        )
        
        if uploaded_file is not None:
            # 验证文件
            is_valid, message = is_likely_wifidebug_file(uploaded_file.name, uploaded_file.size)
            
            # 显示文件信息
            file_details = {
                "文件名": uploaded_file.name,
                "文件大小": f"{uploaded_file.size / 1024:.2f} KB",
                "文件类型": uploaded_file.type if uploaded_file.type else "未知类型"
            }
            
            st.success("✅ 文件上传成功!")
            st.json(file_details)
            
            # 显示文件验证结果
            if "✅" in message:
                st.success(message)
            else:
                st.warning(message)
            
            # 解析按钮
            if st.button("🚀 开始解析", type="primary", use_container_width=True):
                process_file(uploaded_file)
    
    with col2:
        st.header("📊 解析状态")
        if 'parsing_status' not in st.session_state:
            st.info("等待文件上传...")
        else:
            st.success(st.session_state.parsing_status)

def process_file(uploaded_file):
    """处理上传的文件并生成报告"""
    
    # 创建进度条
    progress_bar = st.progress(0)
    status_text = st.empty()
    
    try:
        # 步骤1: 保存上传的文件
        status_text.text("📁 正在保存文件...")
        progress_bar.progress(10)
        
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_input_path = os.path.join(temp_dir, uploaded_file.name)
            temp_json_path = os.path.join(temp_dir, "parsed.json")
            temp_html_path = os.path.join(temp_dir, "report.html")
            
            # 保存上传的文件
            with open(temp_input_path, 'wb') as f:
                f.write(uploaded_file.getbuffer())
            
            # 步骤2: 解析日志文件
            status_text.text("🔍 正在解析日志文件...")
            progress_bar.progress(40)
            
            # 调用log_parser解析文件
            try:
                # 创建一个简单的args对象来模拟命令行参数
                import argparse
                args = argparse.Namespace()
                args.output_txt = None
                args.output_json = temp_json_path
                
                # 捕获解析输出
                import io
                from contextlib import redirect_stdout, redirect_stderr
                
                stdout_buffer = io.StringIO()
                stderr_buffer = io.StringIO()
                
                with redirect_stdout(stdout_buffer), redirect_stderr(stderr_buffer):
                    process_log_file(temp_input_path, VENDOR_SUBCMD_ENUMS, args)
                
                # 检查解析是否成功
                if not os.path.exists(temp_json_path):
                    raise Exception("解析失败，未生成JSON文件")
                    
            except Exception as e:
                st.error(f"日志解析失败: {str(e)}")
                return
            
            # 步骤3: 生成HTML报告
            status_text.text("📄 正在生成HTML报告...")
            progress_bar.progress(70)
            
            try:
                # 调用report_generator生成报告
                display_defs_path = os.path.join(os.path.dirname(__file__), "display_definitions.js")
                
                stdout_buffer = io.StringIO()
                stderr_buffer = io.StringIO()
                
                with redirect_stdout(stdout_buffer), redirect_stderr(stderr_buffer):
                    generate_report(temp_json_path, display_defs_path, temp_html_path)
                
                # 检查报告是否生成成功
                if not os.path.exists(temp_html_path):
                    raise Exception("报告生成失败，未生成HTML文件")
                    
            except Exception as e:
                st.error(f"报告生成失败: {str(e)}")
                return
            
            # 步骤4: 准备下载
            status_text.text("📦 正在准备下载...")
            progress_bar.progress(90)
            
            # 读取生成的HTML报告
            with open(temp_html_path, 'rb') as f:
                html_content = f.read()
            
            # 也读取JSON文件（可选下载）
            with open(temp_json_path, 'rb') as f:
                json_content = f.read()
            
            # 步骤5: 完成
            status_text.text("✅ 解析完成!")
            progress_bar.progress(100)
            
            # 更新会话状态
            st.session_state.parsing_status = "解析成功完成!"
            st.session_state.html_report = html_content
            st.session_state.json_data = json_content
            st.session_state.original_filename = uploaded_file.name
            
            # 显示下载按钮
            st.success("🎉 解析成功完成!")
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.download_button(
                    label="📄 下载 HTML 报告",
                    data=html_content,
                    file_name=f"report_{Path(uploaded_file.name).stem}.html",
                    mime="text/html",
                    type="primary",
                    use_container_width=True
                )
            
            with col2:
                st.download_button(
                    label="📊 下载 JSON 数据",
                    data=json_content,
                    file_name=f"parsed_{Path(uploaded_file.name).stem}.json",
                    mime="application/json",
                    use_container_width=True
                )
            
            # 显示解析统计信息
            show_parsing_stats(temp_json_path)
            
    except Exception as e:
        st.error(f"处理过程中发生错误: {str(e)}")
        st.exception(e)

def show_parsing_stats(json_path):
    """显示解析统计信息"""
    try:
        import json
        with open(json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        st.header("📈 解析统计")
        
        # 计算统计信息
        total_events = len(data)
        
        # 按类型统计
        event_types = {}
        for event in data:
            subcmd = event.get('subcmd', 'unknown')
            event_types[subcmd] = event_types.get(subcmd, 0) + 1
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric("总事件数", total_events)
        
        with col2:
            st.metric("事件类型数", len(event_types))
        
        with col3:
            if event_types:
                most_common = max(event_types.items(), key=lambda x: x[1])
                st.metric("最频繁事件", f"{most_common[0]} ({most_common[1]}次)")
        
        # 显示事件类型分布
        if event_types:
            st.subheader("📊 事件类型分布")
            st.bar_chart(event_types)
            
    except Exception as e:
        st.warning(f"无法显示统计信息: {str(e)}")

if __name__ == "__main__":
    main()
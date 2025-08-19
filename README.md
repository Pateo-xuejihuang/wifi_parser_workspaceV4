# WiFi 调试日志解析器

这是一个用于解析和分析WiFi调试日志的工具集，可以将复杂的WiFi驱动日志转换为易于阅读的HTML报告。

## 核心文件说明

### 📄 `log_parser.py`
**主要解析引擎** - 核心日志解析器

- **功能**: 解析WiFi驱动的netlink消息和调试日志，提取结构化数据
- **技术特点**: 
  - 支持NLA（Netlink Attribute）格式解析
  - 集成Scapy库进行802.11帧分析
  - 自动识别和解析vendor特定命令
- **使用方式**: 
  ```bash
  python log_parser.py examples/wifidebug --output-txt parsed.txt --output-json parsed.json
  ```
- **输出**: 生成指定的`parsed.json`和`parsed.txt`文件

### 🎯 `definitions.py`
**数据定义库** - WiFi协议和vendor命令定义

- **功能**: 包含所有WiFi vendor子命令的定义和属性映射
- **内容**: 
  - QCA vendor命令枚举 (`VENDOR_SUBCMD_ENUMS`)
  - 各种WiFi协议参数的类型定义
  - 属性ID到名称的映射关系
- **使用方式**: 作为模块被其他脚本导入
- **扩展**: 新增WiFi命令时需要在此文件中添加对应定义

### 📊 `report_generator.py`
**报告生成器** - 智能HTML报告生成

- **功能**: 将解析后的JSON数据转换为美观的HTML报告
- **特色功能**:
  - 自动数据转换（如Kbps→Mbps，jiffies→秒）
  - 智能标志位清理和格式化
  - 支持自定义计算函数
- **使用方式**:
  ```bash
  python report_generator.py
  ```
- **输出**: 生成`report.html`文件

### 🎨 `display_definitions.js`
**显示配置** - 用户界面本地化定义

- **功能**: 定义技术术语到中文用户友好标签的映射
- **内容**:
  - WiFi命令的中文友好名称
  - 属性标签的本地化翻译
  - 枚举值的可读化显示
- **使用方式**: 被HTML报告页面动态加载
- **定制**: 修改此文件可改变网页显示的中文标签

## 完整使用流程

1. **解析日志**:
   ```bash
   python log_parser.py examples/wifidebug --output-txt parsed.txt --output-json parsed.json
   ```

2. **生成报告**:
   ```bash
   python report_generator.py
   ```

3. **查看结果**: 用浏览器打开`report.html`

## 依赖要求

- Python 3.6+
- Scapy库: `pip install scapy`

## 项目特点

- ✅ **模块化设计**: 解析、定义、生成、显示各司其职
- ✅ **易于扩展**: 新增命令只需更新definitions.py
- ✅ **中文友好**: 完整的本地化显示支持
- ✅ **智能转换**: 自动将技术数据转换为可读格式
- ✅ **Web展示**: 生成美观的HTML报告页面

适用于WiFi驱动开发、调试分析、性能测试等场景。

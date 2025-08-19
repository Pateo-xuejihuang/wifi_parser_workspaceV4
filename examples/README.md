# 示例文件说明

本文件夹包含用于测试和演示的WiFi调试日志文件。

## 文件列表

- `wifidebug` - WiFi调试日志示例文件

## 使用方法

使用示例文件来测试日志解析功能：

```bash
# 使用示例日志文件
python log_parser.py examples/wifidebug --output-txt parsed.txt --output-json parsed.json
```

然后生成报告：
```bash
python report_generator.py
```

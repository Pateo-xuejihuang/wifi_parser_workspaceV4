# 示例文件说明

本文件夹包含用于测试和演示的WiFi调试日志文件。

## 文件列表

- `wifidebug` - 主要的WiFi调试日志文件
- `wifidebug.txt` - 文本格式的WiFi调试日志
- `wifidebug1.txt` - 额外的测试日志文件1
- `wifidebug2.txt` - 额外的测试日志文件2

## 使用方法

可以使用任何一个文件来测试日志解析功能：

```bash
# 使用主要日志文件
python log_parser.py examples/wifidebug --output-txt parsed.txt --output-json parsed.json

# 或使用其他日志文件
python log_parser.py examples/wifidebug.txt --output-txt parsed.txt --output-json parsed.json
```

然后生成报告：
```bash
python report_generator.py
```

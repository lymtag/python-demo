# Step 02 - Build A Small Script

## Goal

从 `test.json` 读取数据，写一个小脚本输出天气摘要。

## Suggested File

可以新增：

```text
scripts/weather_summary.py
```

如果暂时不想新增目录，也可以先在 `test.py` 里练习。

## Practice

实现一个脚本，输出类似：

```text
杭州: 28.5°C, 晴朗
未来预报: 多云, 晴朗, 雷阵雨
```

## Development Steps

1. 用 `pathlib.Path` 找到 `test.json`。
2. 用 `json.loads` 或 `json.load` 读取内容。
3. 从字典里取出 `城市`、`温度`、`天气`、`预报`。
4. 格式化输出字符串。

## Verify

运行：

```bash
python3 scripts/weather_summary.py
```

如果你写在 `test.py`：

```bash
python3 test.py
```

## Feedback

记录：

- JSON 读取是否成功？
- 字段名写错时会发生什么？
- 这段逻辑是否适合抽成函数？


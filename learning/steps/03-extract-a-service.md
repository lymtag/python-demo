# Step 03 - Extract A Service

## Goal

把脚本里的可复用逻辑抽到服务层，学习“脚本入口”和“业务函数”分离。

## Suggested File

新增：

```text
app/services/weather_service.py
```

## Practice

实现两个函数：

```python
def load_weather(path):
    ...

def format_weather_summary(weather):
    ...
```

## Development Steps

1. 从脚本中复制最小可复用逻辑。
2. 让 `load_weather` 只负责读取 JSON。
3. 让 `format_weather_summary` 只负责把字典变成字符串。
4. 脚本只负责调用函数和 `print`。

## Verify

运行脚本，确认输出不变。

```bash
python3 scripts/weather_summary.py
```

## Feedback

记录：

- 抽出函数后，脚本是否更短？
- 函数是否容易单独测试？
- 有没有函数做了太多事情？


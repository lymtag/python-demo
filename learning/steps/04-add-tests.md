# Step 04 - Add Tests

## Goal

给服务层函数补测试，学习用 pytest 验证代码行为。

## Suggested File

新增：

```text
tests/test_weather_service.py
```

## Practice

测试这些行为：

1. 能读取一个 JSON 文件。
2. 能格式化天气摘要。
3. 文件不存在时抛出清楚的异常。

## Development Steps

1. 用 `tmp_path` 创建临时 JSON 文件。
2. 调用 `load_weather`。
3. 用 `assert` 验证返回值。
4. 用 `pytest.raises` 验证异常。

## Verify

运行：

```bash
python3 -m pytest
```

期望新增测试和旧测试一起通过。

## Feedback

记录：

- 哪个测试最容易写？
- 哪个测试让你发现了代码问题？
- 是否需要调整函数参数，让测试更简单？


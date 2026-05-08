# Step 01 - Read The Project

## Goal

理解当前项目由哪些部分组成，以及每个文件适合承担什么职责。

## Read

- `README.md`
- `test.py`
- `test.json`
- `test2.py`
- `app/services/upload_client.py`
- `tests/test_test2.py`

## Practice

1. 用自己的话写下 `test.py` 是什么类型的文件。
2. 用自己的话写下 `test2.py` 和 `app/services/upload_client.py` 的区别。
3. 找出一个你认为可以继续练习的小功能。

## Verify

运行：

```bash
python3 -m pytest
```

期望结果：

```text
tests passed
```

## Feedback

记录：

- 哪个文件最容易理解？
- 哪个文件最难理解？
- 下一步想先练脚本、CLI、测试，还是 Web？


# Troubleshooting

Python 学习最容易卡在环境、路径和依赖。遇到问题先看这里。

## venv 没激活

现象：

```text
ModuleNotFoundError
```

检查：

```bash
which python3
python3 -m pip --version
```

处理：

```bash
source .venv/bin/activate
python3 -m pip install -e ".[dev]"
```

## pytest 找不到模块

现象：

```text
ModuleNotFoundError: No module named 'app'
```

处理：

- 确认在项目根目录运行。
- 确认 `pyproject.toml` 中有 `pythonpath = ["."]`。

```bash
pwd
python3 -m pytest
```

## pip install 失败

处理：

```bash
python3 -m pip install --upgrade pip
python3 -m pip install -e ".[dev]"
```

如果是网络问题，换网络或配置镜像源。

## uvicorn 启动失败

检查：

```bash
python3 -c "import app.main; print(app.main.app.title)"
```

启动：

```bash
uvicorn app.main:app --reload
```

## 端口被占用

现象：

```text
address already in use
```

处理：

```bash
uvicorn app.main:app --reload --port 8001
```

## JSON 读取失败

检查：

- 文件路径是否正确。
- JSON 是否有多余逗号。
- 中文字段名是否写错。

命令：

```bash
python3 -m json.tool test.json
```


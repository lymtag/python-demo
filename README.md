# Python Learning Lab

这是一个 Python 学习项目。它既包含基础语法练习，也包含一个逐步演进出来的
FastAPI Web 项目骨架。学习时不要只把它当成 Web 项目；它也可以表达为脚本、
CLI 工具、数据处理程序、接口客户端、自动化任务和测试练习项目。

## Best Start

建议按下面顺序上手：

1. 先读 `test.py`，把它当成 Python 基础语法草稿本。
2. 再读 `test.json`，练习 JSON 读取、字典、列表、空值、布尔值。
3. 然后读 `test2.py`，理解一个脚本如何变成可复用 CLI。
4. 接着读 `app/services/upload_client.py`，理解业务逻辑如何从脚本中拆出来。
5. 最后读 `app/main.py` 和 `app/api/routes/`，理解 Web API 如何调用服务层。
6. 每改一个小功能，就在 `tests/` 里补一个测试。

如果想按课程方式跟练，请从 [learning/README.md](learning/README.md) 开始。
那里提供了“开发、测试、反馈、迭代”的一步步教学目录。
如果想按天执行，请使用 [21-Day Daily Practice Plan](learning/daily-practice-plan.md)。
如果你已有 JS 前端基础，建议同时参考 [Frontend To Python Growth Plan](learning/frontend-to-python-growth-plan.md)，重点训练框架意识、设计、测试质量、算法和并发。
日常记录使用 [Daily Journal Template](learning/journal/template.md)，任务看板使用 [Learning Tasks](learning/TASKS.md)。
从 JS 迁移时可查看 [JS To Python Cheatsheet](learning/js-to-python-cheatsheet.md)。
算法和并发专项分别看 [Algorithm Drills](learning/algorithm-drills.md) 与 [Concurrency Drills](learning/concurrency-drills.md)。

推荐学习节奏：

- 每次只练一个主题，比如文件读取、函数、异常、HTTP、测试。
- 先让代码跑起来，再考虑代码是否优雅。
- 能写函数时不要只写顶层脚本。
- 能测试函数时不要依赖人工打印检查。
- 网络请求、文件系统、时间、随机数都视为外部边界，测试时尽量 mock 或隔离。

## Project Forms

这个项目可以扩展成多种 Python 项目形态。

### 1. Script

适合学习基础语法、流程控制、文件读写、JSON 处理。

推荐位置：

- `test.py`
- 新增 `scripts/`

示例方向：

- 读取 `test.json` 并打印天气摘要。
- 批量重命名文件。
- 统计文本中的词频。

### 2. CLI Tool

适合学习 `argparse`、参数校验、错误处理、命令行输出。

当前示例：

- `test2.py`

示例方向：

- 上传指定文件。
- 增加 `--dry-run` 只打印请求参数。
- 增加 `--json` 控制输出格式。

### 3. Web API

适合学习 FastAPI、路由、Pydantic、服务层分离、接口测试。

当前示例：

- `app/main.py`
- `app/api/routes/health.py`
- `app/api/routes/uploads.py`

示例方向：

- 增加 `/api/weather` 返回 `test.json` 内容。
- 增加请求参数校验。
- 增加统一错误响应格式。

### 4. Service Module

适合学习把可复用逻辑从脚本和 Web 层中抽离出来。

当前示例：

- `app/services/upload_client.py`

示例方向：

- 把 JSON 读取封装成 `weather_service.py`。
- 把文件校验封装成独立函数。
- 给外部 HTTP 请求增加超时、重试或错误包装。

### 5. Data Processing

适合学习 JSON、CSV、列表推导式、排序、过滤、聚合。

推荐位置：

- `app/services/`
- `scripts/`
- `tests/`

示例方向：

- 从 `test.json` 中提取城市、温度、预报。
- 将 JSON 转成 CSV。
- 对一组天气数据做最高温、最低温、平均值统计。

### 6. Test Practice

适合学习 pytest、fixture、临时文件、monkeypatch。

当前示例：

- `tests/test_test2.py`
- `tests/test_health_api.py`

示例方向：

- 测试文件不存在时是否抛异常。
- 测试 JSON 解析失败时是否回退到文本。
- 测试 Web 接口是否返回正确状态码。

## Project Layout

```text
.
├── app/                     FastAPI application package
│   ├── api/                 HTTP API layer
│   │   └── routes/          Route handler modules
│   ├── core/                Application settings and shared configuration
│   ├── schemas/             Pydantic request and response models
│   └── services/            Business logic and external service adapters
├── tests/                   Pytest test suite
├── learning/                Step-by-step development and testing lessons
├── scripts/                 Small runnable learning scripts
├── algorithms/              Algorithm practice functions
├── concurrency/             Threading and async practice demos
├── docs/                    Troubleshooting and support notes
├── skills/                  Project-specific Codex skill documentation
├── python_demo_web.egg-info/ Editable-install package metadata
├── .venv/                   Local virtual environment
├── __pycache__/             Python bytecode cache
├── AGENTS.md                OpenAI/Codex agent project guide
├── CLAUDE.md                Claude Project guide
├── pyproject.toml           Python package, dependency, and tool config
├── test2.py                 Backward-compatible upload CLI entry
├── test.py                  Legacy Python learning/demo script
└── test.json                Sample JSON data
```

## Folder Guide

### `app/`

主应用代码。适合放结构化、可复用、可测试的 Python 代码。

### `app/api/`

Web API 层。负责 HTTP 请求和响应组织，不建议在这里堆业务逻辑。

### `app/api/routes/`

FastAPI 路由文件。一个业务主题可以放一个路由文件，例如健康检查、上传、天气。

### `app/core/`

项目配置。环境变量、应用名称、端口、调试开关等适合放这里。

### `app/schemas/`

Pydantic 模型。用于定义接口输入输出结构。

### `app/services/`

服务层。放业务逻辑、文件处理、外部 API 调用、数据转换等可复用能力。

### `tests/`

测试代码。学习项目里测试非常重要，它能帮助你确认“我真的理解了这段代码”。

### `learning/`

一步步练习目录。按开发、测试、反馈、迭代组织，适合跟练和复盘。

### `scripts/`

小脚本练习目录。适合放 JSON 读取、文件处理、CLI 入门等可直接运行的脚本。

### `algorithms/`

算法练习目录。适合放列表、字典、栈、队列、排序、递归等基础题。

### `concurrency/`

并发练习目录。适合放线程、线程池、锁、队列、asyncio 对比示例。

### `docs/`

辅助文档目录。适合放环境问题、依赖安装、故障排查等说明。

### `skills/`

AI 编程助手使用的项目说明。它记录本项目的协作规则、设计习惯和验证方式。

### `.venv/`

本地虚拟环境。由 setup 命令生成，不需要手动编辑。

### `python_demo_web.egg-info/`

本地可编辑安装生成的包元数据，不是应用源码。

### `__pycache__/` and nested `__pycache__/`

Python 自动生成的字节码缓存目录，可以忽略。

### `.pytest_cache/`

pytest 自动生成的测试缓存目录，可以忽略。

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -e ".[dev]"
```

## Run Script

```bash
python3 test.py
```

Run the upload CLI:

```bash
python3 test2.py ./some-file.xlsx --token "your-token"
```

## Run Web API

```bash
uvicorn app.main:app --reload
```

Health check:

```bash
curl http://127.0.0.1:8000/api/health
```

## Test

```bash
python3 -m pytest
```

## Practice Roadmap

1. Python from JS：把已有 JS 经验迁移到 Python 数据类型、函数和模块。
2. 基础语法：变量、字符串、列表、字典、条件、循环。
3. 函数与设计：参数、返回值、异常、类型边界、单一职责。
4. 文件与 JSON：读取、写入、解析、格式化输出。
5. CLI：用 `argparse` 把脚本变成命令行工具。
6. HTTP 客户端：用 `requests` 调接口，处理状态码和响应。
7. Web API：用 FastAPI 提供接口，理解 route、schema、service 分层。
8. 测试质量：用 pytest、tmp_path、monkeypatch、TestClient 保护功能。
9. 算法基础：列表、字典、集合、排序、栈、队列、复杂度。
10. 并发基础：线程、线程池、锁、I/O 密集任务、asyncio 入门。
11. 项目结构：把脚本、服务、路由、模型、测试和文档分层管理。

## Good Habits

- 小步提交、小步测试。
- 函数名表达意图，不用 `do_it`、`handle_data` 这类模糊名字。
- 打印适合学习，测试适合验证。
- 不把真实 token 写进测试和文档。
- 复杂功能先写成普通函数，再接 CLI 或 Web。
- 遇到重复代码时再抽象，不提前设计太重的框架。

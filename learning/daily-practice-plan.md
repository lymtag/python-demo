# Daily Practice Plan

这是一个 21 天 Python 学习任务计划。每天控制在 30 到 60 分钟，固定按这个节奏走：

```text
读代码 5 分钟 -> 开发 25 分钟 -> 测试 10 分钟 -> 反馈记录 10 分钟
```

不要追求一天写很多代码。真正重要的是每天完成一个小闭环：有目标、有代码、有验证、有反馈。

## Daily Checklist

每天结束前检查：

- 今天是否只练了一个主题？
- 是否至少运行了一次代码？
- 是否至少运行了一次测试？
- 是否记录了一个问题或一个收获？
- 是否知道明天要做什么？

## Week 1 - Python Basics And Scripts

### Day 01 - 认识项目

目标：知道项目里每个主要文件是做什么的。

任务：

- 阅读 `README.md`
- 阅读 `test.py`
- 阅读 `test.json`
- 写下 `test.py`、`test2.py`、`app/` 的区别

验证：

```bash
python3 -m pytest
```

反馈：

- 今天最容易理解的文件是什么？
- 今天最不理解的地方是什么？

### Day 02 - JSON 读取

目标：学会读取 `test.json`。

任务：

- 新增 `scripts/weather_summary.py`
- 用 `json` 和 `pathlib.Path` 读取 `test.json`
- 打印城市、温度、天气

验证：

```bash
python3 scripts/weather_summary.py
```

反馈：

- JSON 中的 list、dict、null、bool 分别对应 Python 的什么类型？

### Day 03 - 函数封装

目标：把脚本中的重复逻辑封装成函数。

任务：

- 在 `scripts/weather_summary.py` 中新增 `load_weather`
- 新增 `format_weather_summary`
- 让顶层代码只负责调用函数和打印

验证：

```bash
python3 scripts/weather_summary.py
```

反馈：

- 函数拆出来以后，代码是否更容易读？

### Day 04 - 异常处理

目标：学会处理文件不存在和 JSON 格式错误。

任务：

- 给 JSON 读取增加文件不存在处理
- 给 JSON 解析失败增加清楚的错误提示
- 不要让错误静默消失

验证：

```bash
python3 scripts/weather_summary.py
```

反馈：

- 哪些错误应该抛出？
- 哪些错误适合在 CLI 中打印？

### Day 05 - 列表与格式化

目标：练习列表、字符串拼接和格式化输出。

任务：

- 输出 `预报` 列表
- 把预报格式化成 `多云, 晴朗, 雷阵雨`
- 增加湿度、风向、风速输出

验证：

```bash
python3 scripts/weather_summary.py
```

反馈：

- 哪种字符串格式化方式你最顺手：`f-string`、`format` 还是拼接？

### Day 06 - 小型数据处理

目标：把 JSON 数据转换成新的结构。

任务：

- 写一个函数 `normalize_weather`
- 把中文字段转换成英文字段，例如 `城市 -> city`
- 返回一个新的 dict，不修改原始数据

验证：

```bash
python3 scripts/weather_summary.py
```

反馈：

- 为什么“不修改原始数据”通常更安全？

### Day 07 - Week 1 Review

目标：复盘第一周。

任务：

- 整理 `scripts/weather_summary.py`
- 删除无用打印
- 给重要函数加简短注释
- 写下 3 个本周学到的点

验证：

```bash
python3 scripts/weather_summary.py
python3 -m pytest
```

反馈：

- 下周最想加强的是函数、测试、CLI，还是 Web？

## Week 2 - Services, CLI, And Tests

### Day 08 - 抽出服务层

目标：把脚本逻辑移动到 `app/services/`。

任务：

- 新增 `app/services/weather_service.py`
- 移动 `load_weather`
- 移动 `format_weather_summary`
- 脚本从服务层 import 函数

验证：

```bash
python3 scripts/weather_summary.py
```

反馈：

- 脚本变短了吗？
- 服务函数是否能被其他入口复用？

### Day 09 - 第一个服务测试

目标：用 pytest 测试服务层函数。

任务：

- 新增 `tests/test_weather_service.py`
- 用 `tmp_path` 创建临时 JSON
- 测试 `load_weather`
- 测试 `format_weather_summary`

验证：

```bash
python3 -m pytest
```

反馈：

- 测试失败时，错误信息是否能帮你定位问题？

### Day 10 - 测试异常

目标：学会测试失败场景。

任务：

- 测试文件不存在
- 测试 JSON 格式错误
- 使用 `pytest.raises`

验证：

```bash
python3 -m pytest tests/test_weather_service.py
```

反馈：

- 正常路径和异常路径哪个更容易漏测？

### Day 11 - CLI 参数

目标：把天气脚本变成 CLI 工具。

任务：

- 给 `scripts/weather_summary.py` 增加 `argparse`
- 支持 `--file test.json`
- 支持 `--format text`

验证：

```bash
python3 scripts/weather_summary.py --file test.json
```

反馈：

- CLI 参数名是否清楚？
- 错误输入时提示是否友好？

### Day 12 - CLI JSON 输出

目标：让 CLI 支持不同输出格式。

任务：

- 支持 `--format json`
- text 输出给人看
- json 输出给程序用

验证：

```bash
python3 scripts/weather_summary.py --file test.json --format json
```

反馈：

- 面向人和面向程序的输出有什么不同？

### Day 13 - 阅读上传客户端

目标：理解 `test2.py` 和 `upload_client.py` 的设计。

任务：

- 阅读 `test2.py`
- 阅读 `app/services/upload_client.py`
- 阅读 `tests/test_test2.py`
- 写下 `monkeypatch` 在测试里做了什么

验证：

```bash
python3 -m pytest tests/test_test2.py
```

反馈：

- 为什么测试里不应该真的发网络请求？

### Day 14 - Week 2 Review

目标：复盘服务层、CLI、测试。

任务：

- 整理天气脚本和服务
- 确保所有测试通过
- 写下一个你想继续扩展的小功能

验证：

```bash
python3 -m pytest
```

反馈：

- 你现在能否解释“脚本入口”和“服务层”的区别？

## Week 3 - Web API And Project Practice

### Day 15 - 新增 Weather Schema

目标：学习 Pydantic 响应模型。

任务：

- 新增 `app/schemas/weather.py`
- 定义 `WeatherResponse`
- 字段使用英文名：`city`、`temperature`、`condition`、`forecast`

验证：

```bash
python3 -m compileall app
```

反馈：

- schema 是为了服务代码，还是为了接口边界？

### Day 16 - 新增 Weather API

目标：把服务层能力接到 Web API。

任务：

- 新增 `app/api/routes/weather.py`
- 增加 `GET /api/weather`
- 在 `app/main.py` 注册路由

验证：

```bash
uvicorn app.main:app --reload
curl http://127.0.0.1:8000/api/weather
```

反馈：

- 路由文件里有没有放太多业务逻辑？

### Day 17 - API 测试

目标：给新接口加测试。

任务：

- 新增 `tests/test_weather_api.py`
- 使用 `TestClient`
- 验证状态码和返回 JSON

验证：

```bash
python3 -m pytest tests/test_weather_api.py
```

反馈：

- API 测试和服务测试分别验证什么？

### Day 18 - 错误响应

目标：学习 Web API 错误处理。

任务：

- 当天气文件不存在时返回清楚错误
- 选择合适 HTTP 状态码
- 给错误场景补测试

验证：

```bash
python3 -m pytest
```

反馈：

- Python 异常和 HTTP 错误响应之间是什么关系？

### Day 19 - 项目整理

目标：让项目更像一个可以长期学习的项目。

任务：

- 检查 README 是否和当前结构一致
- 检查 learning 文档是否有过时内容
- 删除临时打印
- 确认命名清楚

验证：

```bash
python3 -m pytest
python3 -m compileall app scripts tests
```

反馈：

- 哪个目录现在最需要整理？

### Day 20 - 小项目整合

目标：完成一个从数据到服务到 API 到测试的小闭环。

任务：

- 数据来源：`test.json`
- 服务层：`weather_service.py`
- CLI：`scripts/weather_summary.py`
- API：`GET /api/weather`
- 测试：service + API

验证：

```bash
python3 scripts/weather_summary.py --file test.json
python3 -m pytest
curl http://127.0.0.1:8000/api/weather
```

反馈：

- 哪一层最容易出错？
- 哪一层最容易测试？

### Day 21 - Final Review

目标：复盘 21 天练习成果，决定下一轮方向。

任务：

- 写一份学习总结
- 列出 3 个掌握的技能
- 列出 3 个仍然不熟的技能
- 选择下一轮项目方向

下一轮方向可选：

- 自动化脚本项目
- 数据处理项目
- 命令行工具项目
- Web API 项目
- 测试专项练习

验证：

```bash
python3 -m pytest
```

反馈：

- 你现在能独立从 0 写一个小 Python 项目吗？
- 如果不能，最需要补的是哪一步？


# Frontend To Python Growth Plan

这份计划适合已经有 JavaScript 前端开发基础的人。重点不是重新学习“什么是变量、什么是函数”，而是补齐 Python 项目开发里的这些能力：

- 框架意识
- 设计思路
- 测试能力
- 代码质量
- 算法基础
- 多线程与并发基础

## Mindset Shift

从前端转到 Python 时，最容易低估的是“项目边界”和“运行环境”：

- 前端常围绕页面、组件、状态、交互组织代码。
- Python 后端和工具项目更常围绕数据流、业务服务、外部资源、任务执行组织代码。
- 前端测试常关注组件行为和用户交互。
- Python 测试更常关注函数、服务、接口、文件、网络、异常和并发边界。

## Competency Map

### 1. Framework Awareness

目标：知道框架负责什么，自己负责什么。

训练重点：

- FastAPI 的 `app`、router、schema、dependency、middleware。
- CLI 项目里的 `argparse`、入口函数、退出码。
- 测试框架里的 fixture、monkeypatch、tmp_path。
- 不把框架对象传得到处都是。

练习任务：

- 给项目增加一个 `/api/weather` 路由。
- 路由只做 HTTP 输入输出，业务逻辑放进 `app/services/`。
- 给同一个服务函数同时接 CLI 和 Web API。

验收标准：

- 你能说清楚 route、schema、service 各自职责。
- 删除 Web 层后，服务函数仍然能被 CLI 使用。

### 2. Design Thinking

目标：写代码前先判断边界、职责和变化点。

训练重点：

- 单一职责。
- 函数式核心，命令式外壳。
- Adapter boundary：文件、网络、数据库、时间、随机数都属于外部边界。
- DTO/schema 与业务 dict 的区别。
- 错误应该在哪一层被转换。

练习任务：

- 把天气 JSON 读取拆成 `load_weather`。
- 把格式化输出拆成 `format_weather_summary`。
- 把字段转换拆成 `normalize_weather`。
- Web route 中只调用服务函数并返回 schema。

验收标准：

- 一个函数只承担一个主要目的。
- 业务函数不直接 `print`。
- 服务层不依赖 FastAPI。

### 3. Testing Skill

目标：让测试成为开发反馈系统，而不是最后补作业。

训练重点：

- 正常路径测试。
- 异常路径测试。
- 边界值测试。
- Mock 外部请求。
- 临时文件测试。
- API 测试。

练习任务：

- 给 `weather_service.py` 写服务测试。
- 给 `upload_client.py` 补错误场景测试。
- 给 `/api/weather` 写接口测试。
- 测试 JSON 缺字段时的行为。

验收标准：

- 每个新功能至少有一个测试。
- 测试不发真实网络请求。
- 测试失败信息能定位问题。

### 4. Quality Engineering

目标：让代码可读、可维护、可验证。

训练重点：

- 命名。
- 小函数。
- 类型提示。
- 错误信息。
- 配置集中管理。
- 依赖收敛在 `pyproject.toml`。
- 文档和目录结构同步。

练习任务：

- 给服务函数补类型提示。
- 给异常错误写清楚上下文。
- 给 README 更新新增目录和命令。
- 运行 `python3 -m compileall app tests` 做语法检查。

验收标准：

- 新人看函数名能猜到用途。
- 配置不散落在多个文件。
- README 能反映真实项目结构。

### 5. Algorithm Basics

目标：补齐通用编程基本功，而不是只会调框架。

训练重点：

- 列表、字典、集合。
- 排序、过滤、分组、计数。
- 字符串处理。
- 双指针、栈、队列。
- 简单递归。
- 时间复杂度和空间复杂度。

推荐新增目录：

```text
algorithms/
```

练习任务：

- `algorithms/two_sum.py`
- `algorithms/word_count.py`
- `algorithms/valid_parentheses.py`
- `algorithms/group_by_weather.py`
- `tests/test_algorithms.py`

验收标准：

- 每个算法函数都有测试。
- 能说出大概复杂度。
- 能用 Python 内置数据结构写出直接、清楚的实现。

### 6. Threads And Concurrency

目标：理解 Python 并发的基本模型和适用场景。

训练重点：

- 线程适合 I/O 密集任务。
- CPU 密集任务不适合用普通线程提速。
- GIL 的基本影响。
- `threading.Thread`
- `concurrent.futures.ThreadPoolExecutor`
- `asyncio` 与线程的区别。
- 锁、共享状态、竞态条件。

推荐新增目录：

```text
concurrency/
```

练习任务：

- 用普通循环模拟多个 URL 请求。
- 用 `ThreadPoolExecutor` 并发执行。
- 给共享计数器加锁。
- 写一个没有锁会出错的示例，再修复它。
- 对比同步、线程、async 的代码形态。

验收标准：

- 能解释 I/O 密集和 CPU 密集的区别。
- 能说出什么时候用线程，什么时候用 async。
- 能写出一个安全的线程共享计数示例。

## 42-Day Training Plan

如果 21 天计划偏短，可以按 6 周执行。

### Week 1 - Python From JS

目标：把 JS 经验迁移到 Python。

每天练：

- Python 数据类型 vs JS 数据类型。
- `dict` vs object / Map。
- `list` vs Array。
- `None` vs `null` / `undefined`。
- 函数默认参数。
- 异常处理。
- 模块 import。

产出：

- `scripts/weather_summary.py`
- 3 个小函数
- 3 个测试

### Week 2 - Framework Awareness

目标：理解 FastAPI 项目分层。

每天练：

- route。
- schema。
- service。
- config。
- error handling。
- TestClient。
- README 同步。

产出：

- `/api/weather`
- `weather_service.py`
- `test_weather_api.py`

### Week 3 - Testing And Quality

目标：把测试变成默认动作。

每天练：

- pytest 基础。
- `tmp_path`。
- `monkeypatch`。
- `pytest.raises`。
- API 测试。
- 重构后跑全量测试。
- 复盘测试覆盖。

产出：

- 服务测试。
- API 测试。
- 异常测试。

### Week 4 - Design Patterns In Small Projects

目标：学习轻量设计，而不是堆抽象。

每天练：

- functional core, imperative shell。
- adapter boundary。
- command/query separation。
- DTO/schema。
- config object。
- error wrapping。
- 复盘函数职责。

产出：

- 一个 CLI + service + API 共用的功能。
- 清楚的错误类型。

### Week 5 - Algorithms

目标：补齐基础算法肌肉。

每天练：

- 数组和哈希表。
- 字符串。
- 栈和队列。
- 排序和分组。
- 简单递归。
- 复杂度分析。
- 算法复盘。

产出：

- `algorithms/`
- 至少 6 个算法函数。
- 对应测试。

### Week 6 - Threads And Concurrency

目标：理解 Python 并发。

每天练：

- 同步 I/O。
- `threading.Thread`。
- `ThreadPoolExecutor`。
- lock。
- race condition。
- `asyncio` 入门。
- 同步、线程、async 对比总结。

产出：

- `concurrency/`
- 至少 4 个并发示例。
- 至少 3 个测试或可运行 demo。

## Weekly Review Template

```markdown
## Week

## Main Skill

## Files Added

## Tests Added

## Bugs Found

## Design Lesson

## Quality Lesson

## Next Week Focus
```

## Recommended Practice Rule

每个练习都尽量产出三件东西：

1. 一个可运行功能。
2. 一个对应测试。
3. 一段复盘记录。

这三件东西比“看完教程”更重要。


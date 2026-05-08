# Step 06 - Feedback And Iteration

## Goal

学会根据测试、运行结果和代码阅读反馈做下一轮迭代。

## Feedback Loop

每次改动后按这个顺序检查：

1. 代码是否能运行？
2. 测试是否通过？
3. 输出是否符合预期？
4. 文件职责是否清楚？
5. 下一步是否足够小？

## Common Feedback Types

### Test Feedback

现象：

```text
assert failed
```

处理：

- 看失败文件和行号。
- 先确认期望值是否写对。
- 再确认实现是否写对。

### Runtime Feedback

现象：

```text
ModuleNotFoundError
```

处理：

- 确认当前目录是否是项目根目录。
- 确认虚拟环境是否安装依赖。
- 确认 import 路径是否正确。

### Design Feedback

现象：

```text
route handler too long
```

处理：

- 把业务逻辑移动到 `app/services/`。
- 路由只保留参数接收、调用服务、返回响应。

## Iteration Ideas

- 给天气服务增加默认文件路径。
- 给 CLI 增加 `--json-file` 参数。
- 给 Web API 增加错误响应。
- 给上传服务增加更明确的错误类型。
- 给 README 增加新的学习记录。

## Done Criteria

一次练习完成时，至少满足：

- 代码能运行。
- 测试能通过。
- README 或学习笔记能说明你做了什么。
- 下一步任务明确。


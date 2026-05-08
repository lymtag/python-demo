# Learning Path

这个目录是一套可以一步步跟练的教学路线。每个练习都围绕同一个循环：

```text
观察需求 -> 写一点代码 -> 写测试 -> 运行验证 -> 记录反馈 -> 小步迭代
```

学习目标不是一次写出完美项目，而是养成稳定的开发节奏。

## How To Use

1. 按顺序完成 `steps/` 下的练习。
2. 每一步只改少量代码。
3. 每一步都运行测试。
4. 每一步都记录反馈：哪里通过了，哪里失败了，下一步想改什么。
5. 如果卡住，先写下问题，再缩小范围。

## Step Index

Daily plan:

- [21-Day Daily Practice Plan](daily-practice-plan.md)
- [Frontend To Python Growth Plan](frontend-to-python-growth-plan.md)
- [Learning Tasks](TASKS.md)
- [JS To Python Cheatsheet](js-to-python-cheatsheet.md)
- [Algorithm Drills](algorithm-drills.md)
- [Concurrency Drills](concurrency-drills.md)
- [Daily Journal Template](journal/template.md)

Step-by-step lessons:

1. [Step 01 - Read The Project](steps/01-read-the-project.md)
2. [Step 02 - Build A Small Script](steps/02-build-a-small-script.md)
3. [Step 03 - Extract A Service](steps/03-extract-a-service.md)
4. [Step 04 - Add Tests](steps/04-add-tests.md)
5. [Step 05 - Expose A Web API](steps/05-expose-a-web-api.md)
6. [Step 06 - Feedback And Iteration](steps/06-feedback-and-iteration.md)

## Daily Practice Template

```markdown
## Date

## Goal

## Files Changed

## Commands Run

## Result

## What I Learned

## Next Step
```

## Feedback Rules

- 反馈要具体：不要只写“失败了”，要写命令、错误、文件和现象。
- 先复现，再修改：确认问题稳定出现以后再改代码。
- 先小改，再大改：一次只解决一个失败点。
- 先测试服务层，再测试 Web 层：服务层反馈更快、更清楚。

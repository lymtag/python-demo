# Concurrency Drills

并发训练目标是理解 Python 里同步、线程、线程池、锁和 async 的区别。

推荐目录：

```text
concurrency/
tests/test_concurrency.py
```

## Core Ideas

- I/O 密集任务：网络请求、文件读写，线程可能有帮助。
- CPU 密集任务：大量计算，普通线程通常不能明显提速。
- 共享状态要小心竞态条件。
- `ThreadPoolExecutor` 比手动管理 `Thread` 更适合日常任务。
- `asyncio` 是协作式并发，不等于多线程。

## Drill 01 - Sync Baseline

任务：

- 写 `fetch_all_sync(urls)`。
- 先用循环模拟多个请求。
- 可以用 `time.sleep` 模拟 I/O 等待。

验证：

```bash
python3 concurrency/sync_demo.py
```

## Drill 02 - ThreadPoolExecutor

任务：

- 写 `fetch_all_threaded(urls)`。
- 使用 `concurrent.futures.ThreadPoolExecutor`。
- 对比同步版本耗时。

验证：

```bash
python3 concurrency/thread_pool_demo.py
```

## Drill 03 - Race Condition

任务：

- 写一个多个线程同时修改计数器的例子。
- 先故意不加锁。
- 再用 `threading.Lock` 修复。

验证：

```bash
python3 concurrency/race_condition_demo.py
```

## Drill 04 - Queue

任务：

- 用 `queue.Queue` 做生产者/消费者模型。
- 一个线程放任务，多个线程处理任务。

验证：

```bash
python3 concurrency/queue_demo.py
```

## Drill 05 - Asyncio First Look

任务：

- 写 `asyncio.gather` 示例。
- 用 `asyncio.sleep` 模拟 I/O。
- 对比线程池写法。

验证：

```bash
python3 concurrency/asyncio_demo.py
```

## Review Questions

- 哪些任务适合线程？
- 哪些任务适合 async？
- 为什么共享变量需要锁？
- 为什么 CPU 密集任务不能指望普通线程明显提速？


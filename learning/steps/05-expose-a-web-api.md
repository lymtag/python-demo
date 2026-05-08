# Step 05 - Expose A Web API

## Goal

把服务层能力接到 FastAPI 路由上，学习 Web API 如何复用普通函数。

## Suggested Files

可以新增或修改：

```text
app/api/routes/weather.py
app/schemas/weather.py
app/main.py
tests/test_weather_api.py
```

## Practice

新增接口：

```text
GET /api/weather
```

返回示例：

```json
{
  "city": "杭州",
  "temperature": 28.5,
  "condition": "晴朗",
  "forecast": ["多云", "晴朗", "雷阵雨"]
}
```

## Development Steps

1. 在 `app/schemas/weather.py` 定义响应模型。
2. 在 `app/api/routes/weather.py` 定义路由。
3. 在 `app/main.py` 注册路由。
4. 在 `tests/test_weather_api.py` 写接口测试。

## Verify

运行测试：

```bash
python3 -m pytest
```

启动服务：

```bash
uvicorn app.main:app --reload
```

请求接口：

```bash
curl http://127.0.0.1:8000/api/weather
```

## Feedback

记录：

- 服务层函数是否被复用了？
- 路由文件是否只负责 HTTP 输入输出？
- 接口响应字段是否清楚？


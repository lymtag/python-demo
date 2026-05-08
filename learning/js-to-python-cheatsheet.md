# JS To Python Cheatsheet

这份对照表帮助有 JavaScript 前端基础的人快速迁移到 Python。

## Data Types

| JavaScript | Python | Notes |
| --- | --- | --- |
| `null` | `None` | Python 没有 `undefined` |
| `true` / `false` | `True` / `False` | 首字母大写 |
| `Array` | `list` | 有序、可变 |
| `Object` | `dict` | 键值结构 |
| `Map` | `dict` | Python `dict` 已经很强 |
| `Set` | `set` | 去重、集合运算 |
| template string | f-string | `f"{name}"` |

## Functions

JavaScript:

```js
function add(a, b = 1) {
  return a + b
}
```

Python:

```python
def add(a, b=1):
    return a + b
```

注意：

- Python 用缩进表示代码块。
- Python 默认参数如果是 list/dict，要格外小心。
- Python 函数可以加类型提示，但运行时默认不强制。

## Modules

JavaScript:

```js
import { add } from "./math"
```

Python:

```python
from app.services.math import add
```

注意：

- Python import 依赖包路径和运行目录。
- 项目根目录下运行测试通常最稳定。

## Async

JavaScript:

```js
const data = await fetch(url)
```

Python:

```python
async def fetch_data():
    ...
```

注意：

- Python 里同步、线程、async 是不同模型。
- `requests` 是同步 HTTP 客户端。
- FastAPI 支持 `async def` route，但服务层是否 async 要看依赖。

## Testing

| JavaScript | Python |
| --- | --- |
| Jest / Vitest | pytest |
| mock function | monkeypatch / unittest.mock |
| temp dir helpers | tmp_path |
| component test | route/service/function test |

pytest 示例：

```python
def test_add():
    assert add(1, 2) == 3
```

## Framework Mapping

| Frontend / Node idea | Python project idea |
| --- | --- |
| React component | FastAPI route / service function |
| Express route | FastAPI router |
| Zod schema | Pydantic model |
| npm scripts | pyproject scripts / shell commands |
| package.json | pyproject.toml |
| fetch boundary | requests/httpx boundary |
| state management | service/data flow design |


# dataforge

`dataforge` 是一个简化的 schema 校验库，用于定义字段、构造对象并做运行时验证。

## 核心对象

- `Field`：定义字段类型、默认值、是否必填
- `Schema`：声明式 schema 基类，支持 `from_dict`、`validate`、`to_dict`
- `ValidationError`：校验失败异常

## 快速使用

```bash
pip install -e .
```

```python
from dataforge import Field, Schema, ValidationError

class User(Schema):
    name = Field(str, required=True)
    age = Field(int, default=18)

u = User.from_dict({"name": "Allen"})
print(u.age)
print(u.to_dict())

try:
    User.from_dict({"name": "Tom", "age": "wrong"}).validate()
except ValidationError as exc:
    print(exc)
```

## 测试

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pip install -e .
pytest tests/ -v --tb=short --json-report --json-report-file=test_results.json
```

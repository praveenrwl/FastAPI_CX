# FastAPI_CX
FastAPI Learning - CampusX



# 🚀 FastAPI – Complete Notes for Learning & Interview Prep

## 1. What is FastAPI?

**FastAPI** is a **modern, high-performance Python web framework** used to build **REST APIs** quickly and efficiently.

### Key Characteristics

* Built on **Starlette** (web layer)
* Uses **Pydantic** for data validation
* Supports **async / await** natively
* Automatic API documentation (Swagger & ReDoc)

### One-liner for Interview

> *FastAPI is a modern Python framework for building APIs with automatic validation, async support, and high performance.*

---

## 2. Why FastAPI? (Very Important for Interviews)

| Feature       | Benefit                              |
| ------------- | ------------------------------------ |
| Async support | Handles high concurrency efficiently |
| Type hints    | Early error detection + cleaner code |
| Auto docs     | Swagger UI generated automatically   |
| Pydantic      | Strong request/response validation   |
| Fast          | Comparable to Node.js & Go           |

### Interview Question

**Q:** Why FastAPI over Flask or Django?
**A:**

* Flask lacks built-in validation and async
* Django is heavyweight for microservices
* FastAPI is fast, async-ready, and production-friendly

---

## 3. FastAPI vs Flask vs Django (Interview Favorite)

| Aspect      | FastAPI                | Flask       | Django        |
| ----------- | ---------------------- | ----------- | ------------- |
| Performance | Very High              | Medium      | Medium        |
| Async       | Native                 | Limited     | Partial       |
| Validation  | Built-in (Pydantic)    | Manual      | Forms/ORM     |
| Docs        | Auto                   | None        | Limited       |
| Use Case    | ML APIs, microservices | Simple APIs | Full web apps |

---

## 4. Basic FastAPI App Structure

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello World"}
```

### Explanation

* `FastAPI()` → creates app instance
* `@app.get()` → route decorator
* Function return → automatically converted to JSON

---

## 5. Path Parameters

```python
@app.get("/items/{item_id}")
def get_item(item_id: int):
    return {"item_id": item_id}
```

### Key Points

* Type hint (`int`) enables validation
* Invalid type → automatic 422 error

### Interview Tip

> FastAPI validates inputs at runtime using type hints.

---

## 6. Query Parameters

```python
@app.get("/search")
def search(q: str = None):
    return {"query": q}
```

* Optional parameters via default values
* Automatically parsed from URL

---

## 7. Request Body with Pydantic

```python
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    price: float
    in_stock: bool

@app.post("/items")
def create_item(item: Item):
    return item
```

### Why Pydantic Matters

* Data validation
* Type safety
* Auto error messages

### Interview One-liner

> FastAPI uses Pydantic models for schema validation and serialization.

---

## 8. Response Models

```python
@app.get("/item", response_model=Item)
def get_item():
    return {"name": "Pen", "price": 10.5, "in_stock": True}
```

### Benefits

* Controls response structure
* Prevents data leakage
* Improves API consistency

---

## 9. Status Codes

```python
from fastapi import status

@app.post("/create", status_code=status.HTTP_201_CREATED)
def create():
    return {"msg": "Created"}
```

### Interview Angle

* Explicit status codes improve API contract clarity

---

## 10. Error Handling

```python
from fastapi import HTTPException

@app.get("/user/{id}")
def get_user(id: int):
    if id != 1:
        raise HTTPException(status_code=404, detail="User not found")
    return {"id": id}
```

---

## 11. Dependency Injection (Very Important)

```python
from fastapi import Depends

def get_db():
    return "DB Connection"

@app.get("/data")
def read_data(db=Depends(get_db)):
    return {"db": db}
```

### Why This Matters

* Clean code
* Reusable logic
* Easy testing

### Interview Statement

> FastAPI has built-in dependency injection for managing shared resources.

---

## 12. Async vs Sync in FastAPI

```python
@app.get("/sync")
def sync_func():
    return "Sync"

@app.get("/async")
async def async_func():
    return "Async"
```

### Rule of Thumb

* Use `async` for I/O operations
* CPU-heavy tasks → background workers (Celery, RQ)

---

## 13. Middleware

```python
@app.middleware("http")
async def log_requests(request, call_next):
    response = await call_next(request)
    return response
```

### Use Cases

* Logging
* Authentication
* Rate limiting

---

## 14. Authentication (Basic Idea)

* OAuth2
* JWT
* API Keys

FastAPI provides:

```python
fastapi.security
```

---

## 15. Auto Documentation

| URL      | Purpose    |
| -------- | ---------- |
| `/docs`  | Swagger UI |
| `/redoc` | ReDoc UI   |

### Interview Highlight

> FastAPI generates OpenAPI-compliant documentation automatically.

---

## 16. Running FastAPI

```bash
uvicorn main:app --reload
```

* `--reload` → auto restart during development

---

## 17. FastAPI in AI / ML Use-Cases

* Model inference APIs
* Recommendation systems
* NLP pipelines
* Microservices in MLOps

### Typical Flow

```
Client → FastAPI → Model → Response
```

---

## 18. Common Interview Questions (Quick Prep)

**Q1:** Why is FastAPI fast?
**A:** Async support + Starlette + uvicorn.

**Q2:** What is Pydantic?
**A:** Data validation and serialization library.

**Q3:** How does FastAPI handle concurrency?
**A:** Async event loop using ASGI.

**Q4:** Can FastAPI scale?
**A:** Yes, horizontally using Docker + Kubernetes.

---

## 19. When NOT to Use FastAPI

* Heavy server-side rendered apps
* CMS-like systems
* Monolithic enterprise apps

---

## 20. Final Interview Summary (Memorize)

> FastAPI is a modern, async Python framework designed for building fast, scalable APIs with automatic validation and documentation, making it ideal for ML and microservice architectures.

---


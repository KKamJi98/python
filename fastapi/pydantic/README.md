# FastAPI에서 Pydantic v2 사용하기

이 디렉토리는 FastAPI에서 Pydantic v2를 사용하여 데이터 검증을 수행하는 방법에 대한 최신 예제를 포함하고 있습니다.

## Pydantic이란?

Pydantic은 Python의 타입 어노테이션을 사용하여 데이터 검증, 직렬화 및 문서화를 제공하는 라이브러리입니다. FastAPI는 Pydantic을 사용하여 요청 및 응답 데이터의 유효성을 검사합니다. Pydantic v2는 성능이 크게 향상되었으며, 새로운 API와 기능을 제공합니다.

## 설치 방법

```bash
# Pydantic v2 설치
pip install pydantic>=2.0.0

# 이메일 검증을 위한 추가 패키지
pip install pydantic[email]
```

## 기본 모델 정의 (v2 스타일)

```python
from pydantic import BaseModel, Field
from typing import Optional, List

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float = Field(gt=0)
    tax: Optional[float] = None
    tags: List[str] = []
    
    # 모델 설정 (v2 스타일)
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "name": "Foo",
                    "price": 35.4,
                    "tags": ["tag1", "tag2"]
                }
            ]
        }
    }
```

## 필드 검증

`Field` 클래스를 사용하여 필드에 대한 추가 검증 및 메타데이터를 정의할 수 있습니다:

```python
from pydantic import BaseModel, Field, EmailStr
from uuid import UUID, uuid4
from datetime import datetime

class User(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    username: str = Field(min_length=3, max_length=50)
    email: EmailStr
    age: Optional[int] = Field(None, ge=0, lt=120)
    created_at: datetime = Field(default_factory=datetime.now)
```

## 필드 수준 검증 (v2 스타일)

`field_validator` 데코레이터를 사용하여 필드 수준의 검증 로직을 추가할 수 있습니다:

```python
from pydantic import BaseModel, field_validator

class Product(BaseModel):
    id: int
    name: str
    price: float
    
    @field_validator('price')
    @classmethod
    def price_must_be_positive(cls, v: float) -> float:
        if v <= 0:
            raise ValueError('가격은 0보다 커야 합니다')
        return v
```

## 모델 수준 검증 (v2 스타일)

`model_validator` 데코레이터를 사용하여 모델 수준의 검증 로직을 추가할 수 있습니다:

```python
from pydantic import BaseModel, model_validator
from datetime import datetime

class Discount(BaseModel):
    active_from: datetime
    active_until: Optional[datetime] = None
    
    @model_validator(mode='after')
    def check_dates(self) -> 'Discount':
        if self.active_until and self.active_from > self.active_until:
            raise ValueError('종료일은 시작일보다 이후여야 합니다')
        return self
```

## 중첩 모델

모델 안에 다른 모델을 포함할 수 있습니다:

```python
class Image(BaseModel):
    url: str
    name: str
    width: Optional[int] = None
    height: Optional[int] = None

class ComplexItem(BaseModel):
    name: str
    price: float = Field(gt=0)
    images: Optional[List[Image]] = None
    metadata: Dict[str, Any] = {}
```

## 열거형을 사용한 모델

`Enum`을 사용하여 특정 값만 허용하는 필드를 정의할 수 있습니다:

```python
from enum import Enum

class Status(str, Enum):
    PENDING = "pending"
    ACTIVE = "active"
    INACTIVE = "inactive"

class Priority(int, Enum):
    LOW = 1
    MEDIUM = 2
    HIGH = 3

class Task(BaseModel):
    title: str
    status: Status = Status.PENDING
    priority: Priority = Priority.MEDIUM
```

## 모델 상속

모델 상속을 통해 공통 필드를 재사용할 수 있습니다:

```python
class BaseResponse(BaseModel):
    success: bool
    message: str

class ItemResponse(BaseResponse):
    data: Item
```

## FastAPI에서 Pydantic 모델 사용

```python
@app.post("/items/", response_model=ItemResponse)
def create_item(item: Item):
    return ItemResponse(
        success=True,
        message="아이템이 성공적으로 생성되었습니다",
        data=item
    )
```

## 요청 본문에서 중첩된 JSON 객체 추출

```python
@app.post("/offers/")
def create_offer(
    item: Item = Body(..., embed=True),
    user: User = Body(..., embed=True),
    quantity: int = Body(..., gt=0)
):
    return {
        "item": item,
        "user": user,
        "quantity": quantity
    }
```

## Pydantic v1에서 v2로 마이그레이션

Pydantic v2로 마이그레이션할 때 주요 변경 사항:

1. `Config` 클래스 대신 `model_config` 딕셔너리 사용
2. `validator` 대신 `field_validator` 사용
3. `root_validator` 대신 `model_validator` 사용
4. `schema_extra` 대신 `json_schema_extra` 사용

## 예제 코드

이 디렉토리의 `main.py` 파일에는 다음과 같은 Pydantic 모델 사용 예제가 포함되어 있습니다:

1. 기본 Pydantic 모델 정의 (v2 스타일)
2. 필드 검증이 있는 모델
3. 필드 수준 검증이 있는 모델 (`field_validator`)
4. 모델 수준 검증이 있는 모델 (`model_validator`)
5. 중첩 모델
6. 열거형을 사용한 모델
7. 모델 상속
8. 각 모델을 사용하는 FastAPI 엔드포인트

## 실행 방법

```bash
uvicorn pydantic.main:app --reload
```

## 참고 자료

- [Pydantic v2 공식 문서](https://docs.pydantic.dev/latest/)
- [FastAPI 공식 문서 - Pydantic 모델](https://fastapi.tiangolo.com/tutorial/body/)
- [Pydantic v1에서 v2로 마이그레이션 가이드](https://docs.pydantic.dev/latest/migration/)

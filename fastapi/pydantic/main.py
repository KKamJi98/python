from fastapi import FastAPI, HTTPException, Query, Body
from pydantic import BaseModel, Field, EmailStr, field_validator, model_validator
from typing import Optional, List, Dict, Any
from datetime import datetime
from enum import Enum
from uuid import UUID, uuid4

app = FastAPI()

# 기본 Pydantic 모델 (v2 스타일)
class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float = Field(gt=0)
    tax: Optional[float] = None
    tags: List[str] = []
    
    # 모델 메서드 예시
    def total_price(self) -> float:
        return self.price + (self.tax or 0)
    
    # 모델 설정 (v2 스타일)
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "name": "Foo",
                    "description": "A very nice Item",
                    "price": 35.4,
                    "tax": 3.2,
                    "tags": ["tag1", "tag2"]
                }
            ]
        }
    }

# 모델을 사용한 POST 요청 처리
@app.post("/items/")
def create_item(item: Item):
    return {
        "item_name": item.name,
        "item_price": item.price,
        "total_price": item.total_price()
    }

# 필드 검증이 있는 모델
class User(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    username: str = Field(min_length=3, max_length=50)
    email: EmailStr
    full_name: Optional[str] = None
    age: Optional[int] = Field(None, ge=0, lt=120)
    is_active: bool = True
    created_at: datetime = Field(default_factory=datetime.now)
    
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "username": "johndoe",
                    "email": "john@example.com",
                    "full_name": "John Doe",
                    "age": 30,
                    "is_active": True
                }
            ]
        }
    }

# 단일 필드 검증이 있는 모델 (v2 스타일)
class Product(BaseModel):
    id: int
    name: str
    price: float
    stock: int = 0
    
    @field_validator('price')
    @classmethod
    def price_must_be_positive(cls, v: float) -> float:
        if v <= 0:
            raise ValueError('가격은 0보다 커야 합니다')
        return v
    
    @field_validator('stock')
    @classmethod
    def stock_must_be_non_negative(cls, v: int) -> int:
        if v < 0:
            raise ValueError('재고는 음수가 될 수 없습니다')
        return v

# 모델 수준 검증이 있는 모델 (v2 스타일)
class Discount(BaseModel):
    name: str
    percentage: float = Field(ge=0, le=100)
    active_from: datetime
    active_until: Optional[datetime] = None
    
    @model_validator(mode='after')
    def check_dates(self) -> 'Discount':
        if self.active_until and self.active_from > self.active_until:
            raise ValueError('종료일은 시작일보다 이후여야 합니다')
        return self

# 중첩 모델
class Image(BaseModel):
    url: str
    name: str
    width: Optional[int] = None
    height: Optional[int] = None

class ComplexItem(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    name: str
    description: Optional[str] = None
    price: float = Field(gt=0)
    tax: Optional[float] = None
    tags: List[str] = []
    images: Optional[List[Image]] = None
    metadata: Dict[str, Any] = {}

# 열거형을 사용한 모델
class Status(str, Enum):
    PENDING = "pending"
    ACTIVE = "active"
    INACTIVE = "inactive"

class Priority(int, Enum):
    LOW = 1
    MEDIUM = 2
    HIGH = 3

class Task(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    title: str
    description: Optional[str] = None
    status: Status = Status.PENDING
    priority: Priority = Priority.MEDIUM
    created_at: datetime = Field(default_factory=datetime.now)
    tags: List[str] = []
    assigned_to: Optional[str] = None

# 상속을 사용한 모델
class BaseResponse(BaseModel):
    success: bool
    message: str

class ItemResponse(BaseResponse):
    data: Item

class UserResponse(BaseResponse):
    data: User

# 모델을 사용한 엔드포인트 예제
@app.post("/users/", response_model=UserResponse)
def create_user(user: User):
    # 실제로는 데이터베이스에 저장하는 로직이 들어갈 수 있습니다
    return UserResponse(
        success=True,
        message="사용자가 성공적으로 생성되었습니다",
        data=user
    )

@app.post("/products/")
def create_product(product: Product):
    return product

@app.post("/complex-items/")
def create_complex_item(item: ComplexItem):
    return item

@app.post("/tasks/")
def create_task(task: Task):
    return task

@app.post("/discounts/")
def create_discount(discount: Discount):
    return discount

# 요청 본문에서 중첩된 JSON 객체 추출
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

# 실행 방법: uvicorn pydantic.main:app --reload

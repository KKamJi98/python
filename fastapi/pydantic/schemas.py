"""
Pydantic 모델 정의를 위한 스키마 모듈
이 모듈은 애플리케이션에서 사용되는 모든 Pydantic 모델을 정의합니다.
"""

from pydantic import BaseModel, Field, EmailStr, field_validator, model_validator
from typing import Optional, List, Dict, Any, Union
from datetime import datetime
from enum import Enum
from uuid import UUID, uuid4


# 기본 모델 - 입력 및 출력 모델 분리 패턴
class ItemBase(BaseModel):
    """기본 아이템 속성"""
    name: str
    description: Optional[str] = None
    price: float = Field(gt=0, description="아이템 가격은 0보다 커야 합니다")
    tax: Optional[float] = None
    tags: List[str] = []


class ItemCreate(ItemBase):
    """아이템 생성 시 사용되는 모델"""
    pass


class ItemUpdate(BaseModel):
    """아이템 업데이트 시 사용되는 모델 (모든 필드 선택적)"""
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = Field(None, gt=0)
    tax: Optional[float] = None
    tags: Optional[List[str]] = None


class ItemInDB(ItemBase):
    """데이터베이스에 저장된 아이템 모델"""
    id: UUID = Field(default_factory=uuid4)
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: Optional[datetime] = None


class Item(ItemInDB):
    """API 응답으로 반환되는 아이템 모델"""
    
    def total_price(self) -> float:
        """세금을 포함한 총 가격 계산"""
        return self.price + (self.tax or 0)
    
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
                    "name": "Foo",
                    "description": "A very nice Item",
                    "price": 35.4,
                    "tax": 3.2,
                    "tags": ["tag1", "tag2"],
                    "created_at": "2023-05-29T13:00:00",
                    "updated_at": None
                }
            ]
        }
    }


# 사용자 모델
class UserBase(BaseModel):
    """기본 사용자 속성"""
    username: str = Field(min_length=3, max_length=50)
    email: EmailStr
    full_name: Optional[str] = None
    is_active: bool = True


class UserCreate(UserBase):
    """사용자 생성 시 사용되는 모델"""
    password: str = Field(min_length=8)


class UserUpdate(BaseModel):
    """사용자 업데이트 시 사용되는 모델 (모든 필드 선택적)"""
    username: Optional[str] = Field(None, min_length=3, max_length=50)
    email: Optional[EmailStr] = None
    full_name: Optional[str] = None
    is_active: Optional[bool] = None
    password: Optional[str] = Field(None, min_length=8)


class UserInDB(UserBase):
    """데이터베이스에 저장된 사용자 모델"""
    id: UUID = Field(default_factory=uuid4)
    hashed_password: str
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: Optional[datetime] = None


class User(BaseModel):
    """API 응답으로 반환되는 사용자 모델"""
    id: UUID
    username: str
    email: EmailStr
    full_name: Optional[str] = None
    is_active: bool
    created_at: datetime
    updated_at: Optional[datetime] = None
    
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
                    "username": "johndoe",
                    "email": "john@example.com",
                    "full_name": "John Doe",
                    "is_active": True,
                    "created_at": "2023-05-29T13:00:00",
                    "updated_at": None
                }
            ]
        }
    }


# 상태 및 우선순위 열거형
class Status(str, Enum):
    """작업 상태 열거형"""
    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    FAILED = "failed"
    CANCELLED = "cancelled"


class Priority(int, Enum):
    """작업 우선순위 열거형"""
    LOW = 1
    MEDIUM = 2
    HIGH = 3
    URGENT = 4


# 작업 모델
class TaskBase(BaseModel):
    """기본 작업 속성"""
    title: str
    description: Optional[str] = None
    status: Status = Status.PENDING
    priority: Priority = Priority.MEDIUM
    due_date: Optional[datetime] = None
    tags: List[str] = []
    assigned_to: Optional[UUID] = None


class TaskCreate(TaskBase):
    """작업 생성 시 사용되는 모델"""
    pass


class TaskUpdate(BaseModel):
    """작업 업데이트 시 사용되는 모델 (모든 필드 선택적)"""
    title: Optional[str] = None
    description: Optional[str] = None
    status: Optional[Status] = None
    priority: Optional[Priority] = None
    due_date: Optional[datetime] = None
    tags: Optional[List[str]] = None
    assigned_to: Optional[UUID] = None


class TaskInDB(TaskBase):
    """데이터베이스에 저장된 작업 모델"""
    id: UUID = Field(default_factory=uuid4)
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: Optional[datetime] = None
    created_by: UUID


class Task(TaskInDB):
    """API 응답으로 반환되는 작업 모델"""
    
    @model_validator(mode='after')
    def check_due_date(self) -> 'Task':
        """작업 기한이 생성일 이후인지 확인"""
        if self.due_date and self.due_date < self.created_at:
            raise ValueError("작업 기한은 생성일 이후여야 합니다")
        return self


# 중첩 모델 예제
class Image(BaseModel):
    """이미지 모델"""
    url: str
    name: str
    width: Optional[int] = None
    height: Optional[int] = None
    
    @field_validator('url')
    @classmethod
    def url_must_be_valid(cls, v: str) -> str:
        """URL이 유효한지 확인"""
        if not v.startswith(('http://', 'https://')):
            raise ValueError('URL은 http:// 또는 https://로 시작해야 합니다')
        return v


class ProductBase(BaseModel):
    """기본 상품 속성"""
    name: str
    description: Optional[str] = None
    price: float = Field(gt=0)
    stock: int = Field(ge=0)
    is_available: bool = True
    category: Optional[str] = None
    tags: List[str] = []


class ProductCreate(ProductBase):
    """상품 생성 시 사용되는 모델"""
    images: Optional[List[Image]] = None


class ProductUpdate(BaseModel):
    """상품 업데이트 시 사용되는 모델 (모든 필드 선택적)"""
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = Field(None, gt=0)
    stock: Optional[int] = Field(None, ge=0)
    is_available: Optional[bool] = None
    category: Optional[str] = None
    tags: Optional[List[str]] = None
    images: Optional[List[Image]] = None


class ProductInDB(ProductBase):
    """데이터베이스에 저장된 상품 모델"""
    id: UUID = Field(default_factory=uuid4)
    images: List[Image] = []
    metadata: Dict[str, Any] = {}
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: Optional[datetime] = None


class Product(ProductInDB):
    """API 응답으로 반환되는 상품 모델"""
    
    @field_validator('price')
    @classmethod
    def price_must_be_positive(cls, v: float) -> float:
        """가격이 양수인지 확인"""
        if v <= 0:
            raise ValueError('가격은 0보다 커야 합니다')
        return v
    
    @field_validator('stock')
    @classmethod
    def stock_must_be_non_negative(cls, v: int) -> int:
        """재고가 음수가 아닌지 확인"""
        if v < 0:
            raise ValueError('재고는 음수가 될 수 없습니다')
        return v


# 응답 모델
class BaseResponse(BaseModel):
    """기본 API 응답 모델"""
    success: bool
    message: str


class DataResponse(BaseResponse):
    """데이터를 포함하는 API 응답 모델"""
    data: Any


class ItemResponse(BaseResponse):
    """아이템 데이터를 포함하는 API 응답 모델"""
    data: Item


class UserResponse(BaseResponse):
    """사용자 데이터를 포함하는 API 응답 모델"""
    data: User


class TaskResponse(BaseResponse):
    """작업 데이터를 포함하는 API 응답 모델"""
    data: Task


class ProductResponse(BaseResponse):
    """상품 데이터를 포함하는 API 응답 모델"""
    data: Product


class ListResponse(BaseResponse):
    """데이터 목록을 포함하는 API 응답 모델"""
    data: List[Any]
    total: int
    page: int = 1
    page_size: int = 10


class PaginatedItems(ListResponse):
    """페이지네이션된 아이템 목록 응답 모델"""
    data: List[Item]


class PaginatedUsers(ListResponse):
    """페이지네이션된 사용자 목록 응답 모델"""
    data: List[User]


class PaginatedTasks(ListResponse):
    """페이지네이션된 작업 목록 응답 모델"""
    data: List[Task]


class PaginatedProducts(ListResponse):
    """페이지네이션된 상품 목록 응답 모델"""
    data: List[Product]


# 복합 요청 모델
class OfferCreate(BaseModel):
    """제안 생성 요청 모델"""
    product_id: UUID
    user_id: UUID
    quantity: int = Field(gt=0)
    price_per_unit: float = Field(gt=0)
    message: Optional[str] = None
    expires_at: Optional[datetime] = None
    
    @model_validator(mode='after')
    def check_expiry(self) -> 'OfferCreate':
        """만료일이 현재 이후인지 확인"""
        if self.expires_at and self.expires_at < datetime.now():
            raise ValueError("만료일은 현재 이후여야 합니다")
        return self

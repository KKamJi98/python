"""
Pydantic의 고급 기능 예제
"""

from pydantic import (
    BaseModel, Field, EmailStr, field_validator, model_validator,
    AnyUrl, SecretStr, constr, conint, confloat, AnyHttpUrl,
    computed_field
)
from typing import Optional, List, Dict, Any, Union, Annotated
from datetime import datetime, date
from enum import Enum
from uuid import UUID, uuid4
import re


# 고급 타입 힌트 및 제약 조건
class AdvancedTypes(BaseModel):
    # 제약 조건이 있는 문자열
    username: Annotated[str, Field(min_length=3, max_length=50, pattern=r'^[a-zA-Z0-9_-]+$')]
    
    # 이메일 검증
    email: EmailStr
    
    # 비밀번호 (마스킹됨)
    password: SecretStr
    
    # URL 검증
    website: Optional[AnyHttpUrl] = None
    
    # 제약 조건이 있는 정수
    age: Annotated[int, Field(ge=0, lt=120)]
    
    # 제약 조건이 있는 부동 소수점
    score: Annotated[float, Field(ge=0.0, le=10.0)]
    
    # 정규식 패턴이 있는 문자열
    postal_code: Optional[constr(pattern=r'^\d{5}(-\d{4})?$')] = None
    
    # 범위가 있는 정수
    priority: conint(ge=1, le=5) = 1
    
    # 범위가 있는 부동 소수점
    rating: confloat(ge=0.0, le=5.0) = 0.0


# 계산된 필드 (Pydantic v2 기능)
class Product(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    name: str
    price: float = Field(gt=0)
    tax_rate: float = Field(ge=0, le=1, default=0.1)
    discount: float = Field(ge=0, le=1, default=0)
    
    @computed_field
    @property
    def price_with_tax(self) -> float:
        return self.price * (1 + self.tax_rate)
    
    @computed_field
    @property
    def final_price(self) -> float:
        return self.price_with_tax * (1 - self.discount)


# 복잡한 검증 로직
class CreditCard(BaseModel):
    card_number: str
    expiration_month: int = Field(ge=1, le=12)
    expiration_year: int = Field(ge=2000)
    cardholder_name: str
    cvv: str = Field(min_length=3, max_length=4)
    
    @field_validator('card_number')
    @classmethod
    def validate_card_number(cls, v: str) -> str:
        # 공백 및 대시 제거
        v = re.sub(r'[\s-]', '', v)
        
        # 숫자만 포함하는지 확인
        if not v.isdigit():
            raise ValueError("카드 번호는 숫자만 포함해야 합니다")
        
        # 길이 확인 (대부분의 카드는 13-19자리)
        if not (13 <= len(v) <= 19):
            raise ValueError("카드 번호 길이가 유효하지 않습니다")
        
        # Luhn 알고리즘 검증 (간소화된 버전)
        digits = [int(d) for d in v]
        odd_digits = digits[-1::-2]
        even_digits = digits[-2::-2]
        checksum = sum(odd_digits)
        for d in even_digits:
            checksum += sum(divmod(d * 2, 10))
        
        if checksum % 10 != 0:
            raise ValueError("유효하지 않은 카드 번호입니다")
        
        return v
    
    @model_validator(mode='after')
    def check_expiration(self) -> 'CreditCard':
        current_date = datetime.now()
        if (self.expiration_year < current_date.year or 
            (self.expiration_year == current_date.year and 
             self.expiration_month < current_date.month)):
            raise ValueError("카드가 만료되었습니다")
        return self


# 다형성 모델 (Union 타입)
class BaseEvent(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    created_at: datetime = Field(default_factory=datetime.now)
    event_type: str


class UserCreatedEvent(BaseEvent):
    event_type: str = "user_created"
    username: str
    email: EmailStr


class ItemPurchasedEvent(BaseEvent):
    event_type: str = "item_purchased"
    item_id: UUID
    quantity: int = Field(gt=0)
    user_id: UUID


class PaymentProcessedEvent(BaseEvent):
    event_type: str = "payment_processed"
    payment_id: UUID
    amount: float = Field(gt=0)
    status: str


# 이벤트 처리 함수
def process_event(event: Union[UserCreatedEvent, ItemPurchasedEvent, PaymentProcessedEvent]):
    if isinstance(event, UserCreatedEvent):
        print(f"사용자 생성 이벤트 처리: {event.username}")
    elif isinstance(event, ItemPurchasedEvent):
        print(f"아이템 구매 이벤트 처리: {event.item_id}, 수량: {event.quantity}")
    elif isinstance(event, PaymentProcessedEvent):
        print(f"결제 처리 이벤트 처리: {event.payment_id}, 금액: {event.amount}")


# 제네릭 모델
from typing import TypeVar, Generic

T = TypeVar('T')

class Paginated(BaseModel, Generic[T]):
    items: List[T]
    total: int
    page: int = 1
    page_size: int = 10
    
    @computed_field
    @property
    def pages(self) -> int:
        return (self.total + self.page_size - 1) // self.page_size
    
    @computed_field
    @property
    def has_next(self) -> bool:
        return self.page < self.pages
    
    @computed_field
    @property
    def has_previous(self) -> bool:
        return self.page > 1


# 사용 예시
class SimpleUser(BaseModel):
    id: UUID
    username: str


# 제네릭 모델 인스턴스화
def get_paginated_users() -> Paginated[SimpleUser]:
    return Paginated[SimpleUser](
        items=[
            SimpleUser(id=uuid4(), username="user1"),
            SimpleUser(id=uuid4(), username="user2"),
        ],
        total=10,
        page=1,
        page_size=2
    )


# 데이터 마스킹 및 민감 정보 처리
class UserProfile(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    username: str
    email: EmailStr
    password: SecretStr
    birth_date: Optional[date] = None
    phone_number: Optional[str] = None
    
    # 모델 직렬화 시 민감 정보 제외
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "username": "johndoe",
                    "email": "john@example.com",
                    "password": "********",
                    "birth_date": "1990-01-01",
                    "phone_number": "+1234567890"
                }
            ]
        }
    }
    
    # 전화번호 마스킹
    @computed_field
    @property
    def masked_phone(self) -> Optional[str]:
        if not self.phone_number:
            return None
        
        # 마지막 4자리만 표시
        if len(self.phone_number) > 4:
            return "*" * (len(self.phone_number) - 4) + self.phone_number[-4:]
        return self.phone_number
    
    # 이메일 마스킹
    @computed_field
    @property
    def masked_email(self) -> str:
        parts = self.email.split("@")
        if len(parts[0]) > 2:
            return parts[0][0] + "*" * (len(parts[0]) - 2) + parts[0][-1] + "@" + parts[1]
        return "*" * len(parts[0]) + "@" + parts[1]

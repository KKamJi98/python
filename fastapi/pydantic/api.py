"""
FastAPI와 Pydantic을 함께 사용하는 예제 API
"""

from fastapi import FastAPI, HTTPException, Query, Body, Path, Depends
from fastapi.responses import JSONResponse
from typing import List, Optional, Dict, Any
from uuid import UUID, uuid4
from datetime import datetime

# 스키마 모듈에서 모델 가져오기
from schemas import (
    Item, ItemCreate, ItemUpdate, ItemResponse, PaginatedItems,
    User, UserCreate, UserUpdate, UserResponse, PaginatedUsers,
    Task, TaskCreate, TaskUpdate, TaskResponse, PaginatedTasks,
    Product, ProductCreate, ProductUpdate, ProductResponse, PaginatedProducts,
    BaseResponse, DataResponse, ListResponse, Status, Priority
)

# 고급 모듈에서 모델 가져오기
from advanced import (
    AdvancedTypes, CreditCard, UserProfile, 
    UserCreatedEvent, ItemPurchasedEvent, PaymentProcessedEvent
)

app = FastAPI(
    title="Pydantic 예제 API",
    description="FastAPI와 Pydantic v2를 사용한 예제 API",
    version="0.1.0",
)

# 메모리 데이터베이스 (실제 애플리케이션에서는 실제 데이터베이스를 사용해야 함)
items_db: Dict[UUID, Item] = {}
users_db: Dict[UUID, User] = {}
tasks_db: Dict[UUID, Task] = {}
products_db: Dict[UUID, Product] = {}

# 아이템 API 엔드포인트
@app.post("/items/", response_model=ItemResponse, status_code=201)
def create_item(item_create: ItemCreate) -> ItemResponse:
    """새 아이템 생성"""
    item_id = uuid4()
    item_dict = item_create.model_dump()
    item_dict.update({
        "id": item_id,
        "created_at": datetime.now(),
        "updated_at": None
    })
    item = Item(**item_dict)
    items_db[item_id] = item
    return ItemResponse(
        success=True,
        message="아이템이 성공적으로 생성되었습니다",
        data=item
    )


@app.get("/items/", response_model=PaginatedItems)
def read_items(
    skip: int = Query(0, ge=0, description="건너뛸 아이템 수"),
    limit: int = Query(10, ge=1, le=100, description="반환할 최대 아이템 수"),
    name: Optional[str] = Query(None, description="아이템 이름으로 필터링")
) -> PaginatedItems:
    """아이템 목록 조회"""
    filtered_items = list(items_db.values())
    
    if name:
        filtered_items = [item for item in filtered_items if name.lower() in item.name.lower()]
    
    total = len(filtered_items)
    items = filtered_items[skip:skip + limit]
    
    return PaginatedItems(
        success=True,
        message="아이템 목록을 성공적으로 조회했습니다",
        data=items,
        total=total,
        page=skip // limit + 1 if limit > 0 else 1,
        page_size=limit
    )


@app.get("/items/{item_id}", response_model=ItemResponse)
def read_item(item_id: UUID = Path(..., description="조회할 아이템의 ID")) -> ItemResponse:
    """특정 아이템 조회"""
    if item_id not in items_db:
        raise HTTPException(status_code=404, detail="아이템을 찾을 수 없습니다")
    
    return ItemResponse(
        success=True,
        message="아이템을 성공적으로 조회했습니다",
        data=items_db[item_id]
    )


@app.put("/items/{item_id}", response_model=ItemResponse)
def update_item(
    item_update: ItemUpdate,
    item_id: UUID = Path(..., description="업데이트할 아이템의 ID")
) -> ItemResponse:
    """아이템 업데이트"""
    if item_id not in items_db:
        raise HTTPException(status_code=404, detail="아이템을 찾을 수 없습니다")
    
    item = items_db[item_id]
    update_data = item_update.model_dump(exclude_unset=True)
    
    for key, value in update_data.items():
        setattr(item, key, value)
    
    item.updated_at = datetime.now()
    items_db[item_id] = item
    
    return ItemResponse(
        success=True,
        message="아이템이 성공적으로 업데이트되었습니다",
        data=item
    )


@app.delete("/items/{item_id}", response_model=BaseResponse)
def delete_item(item_id: UUID = Path(..., description="삭제할 아이템의 ID")) -> BaseResponse:
    """아이템 삭제"""
    if item_id not in items_db:
        raise HTTPException(status_code=404, detail="아이템을 찾을 수 없습니다")
    
    del items_db[item_id]
    
    return BaseResponse(
        success=True,
        message="아이템이 성공적으로 삭제되었습니다"
    )


# 고급 Pydantic 기능 예제 엔드포인트
@app.post("/advanced-types/", response_model=DataResponse)
def create_advanced_types(data: AdvancedTypes) -> DataResponse:
    """고급 타입 힌트 및 제약 조건 예제"""
    return DataResponse(
        success=True,
        message="데이터가 성공적으로 검증되었습니다",
        data=data
    )


@app.post("/credit-cards/", response_model=BaseResponse)
def validate_credit_card(card: CreditCard) -> BaseResponse:
    """신용카드 검증 예제"""
    # 실제로는 여기서 결제 처리 등의 로직이 들어갈 수 있습니다
    return BaseResponse(
        success=True,
        message="신용카드가 성공적으로 검증되었습니다"
    )


@app.post("/events/user-created/", response_model=DataResponse)
def create_user_event(event: UserCreatedEvent) -> DataResponse:
    """사용자 생성 이벤트 처리"""
    return DataResponse(
        success=True,
        message="사용자 생성 이벤트가 성공적으로 처리되었습니다",
        data=event
    )


@app.post("/events/item-purchased/", response_model=DataResponse)
def create_purchase_event(event: ItemPurchasedEvent) -> DataResponse:
    """아이템 구매 이벤트 처리"""
    return DataResponse(
        success=True,
        message="아이템 구매 이벤트가 성공적으로 처리되었습니다",
        data=event
    )


@app.post("/events/payment-processed/", response_model=DataResponse)
def create_payment_event(event: PaymentProcessedEvent) -> DataResponse:
    """결제 처리 이벤트 처리"""
    return DataResponse(
        success=True,
        message="결제 처리 이벤트가 성공적으로 처리되었습니다",
        data=event
    )


@app.post("/user-profiles/", response_model=DataResponse)
def create_user_profile(profile: UserProfile) -> DataResponse:
    """사용자 프로필 생성 (민감 정보 처리 예제)"""
    # 응답에서는 마스킹된 정보만 반환
    return DataResponse(
        success=True,
        message="사용자 프로필이 성공적으로 생성되었습니다",
        data={
            "id": profile.id,
            "username": profile.username,
            "masked_email": profile.masked_email,
            "masked_phone": profile.masked_phone,
            "birth_date": profile.birth_date
        }
    )


# 에러 핸들러
@app.exception_handler(ValueError)
async def value_error_handler(request, exc):
    return JSONResponse(
        status_code=422,
        content={
            "success": False,
            "message": str(exc),
            "error_type": "ValueError"
        }
    )


# 실행 방법: uvicorn pydantic.api:app --reload

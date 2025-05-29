from fastapi import FastAPI, Path, HTTPException
from enum import Enum
from typing import Optional

app = FastAPI()

# 기본적인 경로 매개변수 사용
@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}

# 경로 매개변수 검증
@app.get("/products/{product_id}")
def read_product(
    product_id: int = Path(..., title="상품 ID", ge=1, description="조회할 상품의 ID")
):
    # 실제로는 데이터베이스에서 상품을 조회하는 로직이 들어갈 수 있습니다
    if product_id > 1000:
        raise HTTPException(status_code=404, detail="상품을 찾을 수 없습니다")
    return {"product_id": product_id, "name": f"상품 {product_id}"}

# 문자열 경로 매개변수
@app.get("/users/{username}")
def read_user(username: str):
    return {"username": username}

# 열거형(Enum) 경로 매개변수
class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

@app.get("/models/{model_name}")
def get_model(model_name: ModelName):
    if model_name == ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}
    
    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}
        
    return {"model_name": model_name, "message": "Have some residuals"}

# 경로 매개변수와 쿼리 매개변수 함께 사용
@app.get("/users/{user_id}/items/{item_id}")
def read_user_item(
    user_id: int, 
    item_id: int, 
    q: Optional[str] = None, 
    short: bool = False
):
    item = {"item_id": item_id, "owner_id": user_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update({"description": "This is an amazing item that has a long description"})
    return item

# 실행 방법: uvicorn path-parameter.main:app --reload

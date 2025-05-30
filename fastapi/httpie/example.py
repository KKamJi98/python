from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="HTTPie 테스트용 API")

# 샘플 데이터
items_db = {
    1: {"name": "Item 1", "price": 50.2},
    2: {"name": "Item 2", "price": 30.5},
    3: {"name": "Item 3", "price": 45.0},
}

# Pydantic 모델
class Item(BaseModel):
    name: str
    price: float

class ItemResponse(BaseModel):
    id: int
    name: str
    price: float

@app.get("/")
def read_root():
    return {"message": "HTTPie 테스트용 API에 오신 것을 환영합니다!"}

@app.get("/items/", response_model=list[ItemResponse])
def read_items(skip: int = 0, limit: int = 10):
    items = [{"id": id, **item} for id, item in items_db.items()]
    return items[skip:skip+limit]

@app.get("/items/{item_id}", response_model=ItemResponse)
def read_item(item_id: int):
    if item_id not in items_db:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"id": item_id, **items_db[item_id]}

@app.post("/items/", response_model=ItemResponse)
def create_item(item: Item):
    item_id = max(items_db.keys()) + 1 if items_db else 1
    items_db[item_id] = item.dict()
    return {"id": item_id, **item.dict()}

@app.put("/items/{item_id}", response_model=ItemResponse)
def update_item(item_id: int, item: Item):
    if item_id not in items_db:
        raise HTTPException(status_code=404, detail="Item not found")
    items_db[item_id] = item.dict()
    return {"id": item_id, **item.dict()}

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    if item_id not in items_db:
        raise HTTPException(status_code=404, detail="Item not found")
    del items_db[item_id]
    return {"message": f"Item {item_id} deleted successfully"}

# 실행 방법: uvicorn httpie.example:app --reload

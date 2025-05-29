from fastapi import FastAPI, Query
from typing import Optional, List

app = FastAPI()

# 기본 쿼리 매개변수
@app.get("/items/")
def read_items(skip: int = 0, limit: int = 10):
    # 실제로는 데이터베이스에서 아이템을 조회하는 로직이 들어갈 수 있습니다
    fake_items = [{"item_id": i, "name": f"Item {i}"} for i in range(skip, skip + limit)]
    return fake_items

# 선택적 쿼리 매개변수
@app.get("/search/")
def search_items(q: Optional[str] = None):
    if q:
        return {"items": [{"item_id": 1, "name": f"Item containing '{q}'"}]}
    return {"items": []}

# 쿼리 매개변수 검증
@app.get("/products/")
def read_products(
    q: Optional[str] = Query(
        None, 
        min_length=3, 
        max_length=50, 
        title="검색어",
        description="검색할 상품 이름"
    )
):
    results = {"products": [{"product_id": 1, "name": "Product 1"}]}
    if q:
        results.update({"q": q, "filtered": True})
    return results

# 필수 쿼리 매개변수
@app.get("/required-query/")
def read_required_query(q: str = Query(..., min_length=3)):
    return {"q": q}

# 여러 값을 가진 쿼리 매개변수
@app.get("/items-multi/")
def read_items_multi_query(q: Optional[List[str]] = Query(None)):
    query_items = {"q": q}
    return query_items

# 쿼리 매개변수 별칭
@app.get("/items-alias/")
def read_items_with_alias(q: Optional[str] = Query(None, alias="item-query")):
    results = {"items": [{"item_id": 1, "name": "Item 1"}]}
    if q:
        results.update({"q": q})
    return results

# 쿼리 매개변수 사용 중단 표시
@app.get("/items-deprecated/")
def read_items_deprecated(
    q: Optional[str] = Query(
        None,
        deprecated=True
    )
):
    results = {"items": [{"item_id": 1, "name": "Item 1"}]}
    if q:
        results.update({"q": q})
    return results

# 실행 방법: uvicorn query-parameter.main:app --reload

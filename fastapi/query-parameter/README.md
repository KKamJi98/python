# FastAPI Query Parameter 사용법

이 디렉토리는 FastAPI에서 쿼리 매개변수(Query Parameter)를 사용하는 다양한 방법에 대한 예제를 포함하고 있습니다.

## 쿼리 매개변수란?

쿼리 매개변수는 URL의 `?` 뒤에 오는 키-값 쌍으로, 형식은 `?param1=value1&param2=value2`와 같습니다. FastAPI에서는 함수 매개변수를 통해 쿼리 매개변수를 정의합니다.

## 기본 사용법

```python
@app.get("/items/")
def read_items(skip: int = 0, limit: int = 10):
    # skip과 limit은 쿼리 매개변수입니다
    return {"skip": skip, "limit": limit}
```

위 예제에서 `skip`과 `limit`은 쿼리 매개변수로, 기본값이 각각 0과 10으로 설정되어 있습니다.

## 선택적 쿼리 매개변수

`Optional`을 사용하여 선택적 쿼리 매개변수를 정의할 수 있습니다:

```python
from typing import Optional

@app.get("/search/")
def search_items(q: Optional[str] = None):
    if q:
        return {"items": [{"item_id": 1, "name": f"Item containing '{q}'"}]}
    return {"items": []}
```

## 쿼리 매개변수 검증

`Query` 클래스를 사용하여 쿼리 매개변수에 대한 추가 검증 및 메타데이터를 정의할 수 있습니다:

```python
from fastapi import Query

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
    # 처리 로직
    return {"q": q}
```

## 필수 쿼리 매개변수

기본값 대신 `...`을 사용하여 필수 쿼리 매개변수를 정의할 수 있습니다:

```python
@app.get("/required-query/")
def read_required_query(q: str = Query(..., min_length=3)):
    return {"q": q}
```

## 여러 값을 가진 쿼리 매개변수

리스트 형태의 쿼리 매개변수를 정의할 수 있습니다:

```python
from typing import List

@app.get("/items-multi/")
def read_items_multi_query(q: Optional[List[str]] = Query(None)):
    query_items = {"q": q}
    return query_items
```

이 경우 URL은 `?q=value1&q=value2`와 같은 형식이 됩니다.

## 쿼리 매개변수 별칭

`alias` 매개변수를 사용하여 쿼리 매개변수의 별칭을 정의할 수 있습니다:

```python
@app.get("/items-alias/")
def read_items_with_alias(q: Optional[str] = Query(None, alias="item-query")):
    # 처리 로직
    return {"q": q}
```

이 경우 URL은 `?item-query=value`와 같은 형식이 됩니다.

## 예제 코드

이 디렉토리의 `main.py` 파일에는 다음과 같은 쿼리 매개변수 사용 예제가 포함되어 있습니다:

1. 기본 쿼리 매개변수
2. 선택적 쿼리 매개변수
3. Query 클래스를 사용한 매개변수 검증
4. 필수 쿼리 매개변수
5. 여러 값을 가진 쿼리 매개변수
6. 쿼리 매개변수 별칭
7. 쿼리 매개변수 사용 중단 표시

## 실행 방법

```bash
uvicorn query-parameter.main:app --reload
```

이 예제를 통해 FastAPI에서 쿼리 매개변수를 효과적으로 사용하는 방법을 이해할 수 있습니다.

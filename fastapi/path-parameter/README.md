# FastAPI Path Parameter 사용법

이 디렉토리는 FastAPI에서 경로 매개변수(Path Parameter)를 사용하는 다양한 방법에 대한 예제를 포함하고 있습니다.

## 경로 매개변수란?

경로 매개변수는 URL 경로의 일부로 전달되는 변수입니다. FastAPI에서는 중괄호 `{}`를 사용하여 경로 매개변수를 정의합니다.

## 기본 사용법

```python
@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}
```

위 예제에서 `item_id`는 경로 매개변수로, 정수형으로 자동 변환됩니다.

## 경로 매개변수 검증

`Path` 클래스를 사용하여 경로 매개변수에 대한 추가 검증 및 메타데이터를 정의할 수 있습니다:

```python
from fastapi import Path

@app.get("/products/{product_id}")
def read_product(
    product_id: int = Path(..., title="상품 ID", ge=1, description="조회할 상품의 ID")
):
    return {"product_id": product_id}
```

## 열거형(Enum) 경로 매개변수

특정 값만 허용하는 경로 매개변수를 정의하려면 `Enum`을 사용할 수 있습니다:

```python
from enum import Enum

class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

@app.get("/models/{model_name}")
def get_model(model_name: ModelName):
    # 모델 이름에 따른 처리
    return {"model_name": model_name}
```

## 경로 매개변수와 쿼리 매개변수 함께 사용

경로 매개변수와 쿼리 매개변수를 함께 사용할 수 있습니다:

```python
@app.get("/users/{user_id}/items/{item_id}")
def read_user_item(
    user_id: int, 
    item_id: int, 
    q: Optional[str] = None, 
    short: bool = False
):
    # 처리 로직
    return {"user_id": user_id, "item_id": item_id}
```

## 예제 코드

이 디렉토리의 `main.py` 파일에는 다음과 같은 경로 매개변수 사용 예제가 포함되어 있습니다:

1. 기본적인 정수형 경로 매개변수
2. Path 클래스를 사용한 매개변수 검증
3. 문자열 경로 매개변수
4. Enum을 사용한 제한된 값 경로 매개변수
5. 경로 매개변수와 쿼리 매개변수 조합

## 실행 방법

```bash
uvicorn path-parameter.main:app --reload
```

이 예제를 통해 FastAPI에서 경로 매개변수를 효과적으로 사용하는 방법을 이해할 수 있습니다.

# FastAPI Study

FastAPI는 현대적이고 빠른(고성능) 웹 프레임워크로, Python 3.7+ 기반으로 API를 구축하는 데 사용됩니다.

## 설치 방법

```bash
# FastAPI 및 ASGI 서버 설치
pip install fastapi uvicorn

# 개발 환경에서만 필요한 패키지 추가 설치 (선택사항)
pip install fastapi[all]
```

## 서버 실행 방법

```bash
# main.py 파일의 app 객체를 사용하여 서버 실행
uvicorn main:app --reload

# --reload 옵션은 코드 변경 시 자동으로 서버를 재시작합니다 (개발 환경에서 유용)
```

## 기본 예제

### 기본 라우트 설정

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI"}
```

### Path Parameter 사용 예제

Path Parameter는 URL 경로의 일부로 전달되는 변수입니다.

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}
```

### Query Parameter 사용 예제

Query Parameter는 URL의 ? 뒤에 오는 키-값 쌍입니다.

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/items/")
def read_items(skip: int = 0, limit: int = 10):
    return {"skip": skip, "limit": limit}
```

## 자동 문서화

FastAPI는 자동으로 API 문서를 생성합니다:
- Swagger UI: `/docs`
- ReDoc: `/redoc`

## 프로젝트 구조

이 저장소는 FastAPI의 다양한 기능을 학습하기 위한 예제들을 포함하고 있습니다:

- [setup](./setup/): FastAPI 프로젝트 설정 및 기본 구성 방법
- [path-parameter](./path-parameter/): 경로 매개변수 사용 방법
- [query-parameter](./query-parameter/): 쿼리 매개변수 사용 방법
- [pydantic](./pydantic/): Pydantic 모델을 사용한 데이터 검증
- [logging](./logging/): FastAPI에서 로깅 설정 방법

각 디렉토리에는 해당 기능에 대한 자세한 설명과 예제 코드가 포함되어 있습니다.

## History

- 2025-05-29: README.md 파일 생성. FastAPI 설치 방법, 서버 실행 방법, 기본 라우트 설정, Path Parameter 및 Query Parameter 사용 예제 추가
- 2025-05-29: 프로젝트 구조 섹션 추가 및 각 기능별 디렉토리에 대한 설명 추가

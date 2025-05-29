# FastAPI 프로젝트 설정

이 디렉토리는 FastAPI 프로젝트의 기본 설정 및 구성 방법에 대한 예제를 포함하고 있습니다.

## 기본 설정

FastAPI 애플리케이션을 설정할 때 다음과 같은 기본 구성을 사용할 수 있습니다:

```python
from fastapi import FastAPI

app = FastAPI(
    title="FastAPI Example API",
    description="FastAPI를 사용한 예제 API 서버입니다.",
    version="0.1.0",
)
```

## 미들웨어 설정

CORS(Cross-Origin Resource Sharing) 미들웨어 설정 예시:

```python
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 실제 프로덕션에서는 특정 도메인만 허용하는 것이 좋습니다
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

## 이벤트 핸들러

애플리케이션 시작 및 종료 시 실행되는 이벤트 핸들러:

```python
@app.on_event("startup")
async def startup_event():
    print("애플리케이션이 시작되었습니다!")

@app.on_event("shutdown")
async def shutdown_event():
    print("애플리케이션이 종료됩니다!")
```

## 실행 방법

```bash
# 현재 디렉토리에서 실행할 경우
uvicorn main:app --reload

# 다른 디렉토리에서 실행할 경우
uvicorn setup.main:app --reload
```

## 예제 코드

이 디렉토리의 `main.py` 파일에는 다음과 같은 기능이 포함되어 있습니다:

1. FastAPI 애플리케이션 인스턴스 생성 및 메타데이터 설정
2. CORS 미들웨어 설정
3. 기본 라우트 및 상태 확인 엔드포인트
4. 애플리케이션 시작/종료 이벤트 핸들러

이 예제를 통해 FastAPI 프로젝트의 기본 구조와 설정 방법을 이해할 수 있습니다.

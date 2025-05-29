# FastAPI에서 로깅 설정하기

이 디렉토리는 FastAPI 애플리케이션에서 로깅을 설정하고 사용하는 방법에 대한 예제를 포함하고 있습니다.

## 로깅의 중요성

로깅은 애플리케이션의 동작을 모니터링하고 문제를 디버깅하는 데 필수적인 요소입니다. 특히 프로덕션 환경에서는 로그를 통해 애플리케이션의 상태와 오류를 파악할 수 있습니다.

## 기본 로깅 설정

Python의 기본 로깅 모듈을 사용하여 FastAPI 애플리케이션에 로깅을 설정할 수 있습니다:

```python
import logging

# 로거 생성
logger = logging.getLogger("app")
logger.setLevel(logging.INFO)

# 핸들러 설정
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s"))
logger.addHandler(handler)
```

## dictConfig를 사용한 고급 로깅 설정

더 복잡한 로깅 설정을 위해 `dictConfig`를 사용할 수 있습니다:

```python
from logging.config import dictConfig

def configure_logging():
    dictConfig({
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "default": {
                "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
            },
        },
        "handlers": {
            "default": {
                "formatter": "default",
                "class": "logging.StreamHandler",
                "stream": "ext://sys.stderr",
            },
            "file": {
                "formatter": "default",
                "class": "logging.handlers.RotatingFileHandler",
                "filename": "app.log",
                "maxBytes": 10485760,  # 10MB
                "backupCount": 5,
            }
        },
        "loggers": {
            "app": {"handlers": ["default", "file"], "level": "INFO"},
        }
    })
```

## 미들웨어를 사용한 요청 로깅

FastAPI 미들웨어를 사용하여 모든 요청과 응답을 로깅할 수 있습니다:

```python
@app.middleware("http")
async def log_requests(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    logger.info(f"{request.method} {request.url.path} - Status: {response.status_code} - Took: {process_time:.4f}s")
    return response
```

## 요청 ID 추적

각 요청에 고유 ID를 할당하여 로그에서 요청을 추적할 수 있습니다:

```python
import uuid

@app.middleware("http")
async def add_request_id(request: Request, call_next):
    request_id = str(uuid.uuid4())
    request.state.request_id = request_id
    response = await call_next(request)
    response.headers["X-Request-ID"] = request_id
    return response
```

## 로그 레벨

Python 로깅 모듈은 다음과 같은 로그 레벨을 제공합니다:
- DEBUG: 디버깅 목적의 상세 정보
- INFO: 일반적인 정보 메시지
- WARNING: 잠재적인 문제 상황
- ERROR: 오류 발생
- CRITICAL: 심각한 오류 발생

## 예제 코드

이 디렉토리의 `main.py` 파일에는 다음과 같은 로깅 기능이 포함되어 있습니다:

1. dictConfig를 사용한 로깅 설정
2. 파일 및 콘솔 로깅
3. 요청 ID 미들웨어
4. 요청 및 응답 로깅
5. 다양한 로그 레벨 사용 예제
6. 예외 처리 및 로깅

## 실행 방법

```bash
uvicorn logging.main:app --reload
```

이 예제를 통해 FastAPI 애플리케이션에서 효과적인 로깅 시스템을 구축하는 방법을 이해할 수 있습니다.

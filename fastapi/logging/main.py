from fastapi import FastAPI, Request
import logging
import time
from logging.config import dictConfig
import uvicorn
import uuid
from fastapi.middleware.cors import CORSMiddleware

# 로깅 설정
def configure_logging():
    dictConfig({
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "default": {
                "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
            },
            "access": {
                "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
            },
        },
        "handlers": {
            "default": {
                "formatter": "default",
                "class": "logging.StreamHandler",
                "stream": "ext://sys.stderr",
            },
            "access": {
                "formatter": "access",
                "class": "logging.StreamHandler",
                "stream": "ext://sys.stdout",
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
            "uvicorn.access": {"handlers": ["access"], "level": "INFO", "propagate": False},
            "uvicorn.error": {"handlers": ["default"], "level": "INFO", "propagate": False},
        }
    })

configure_logging()
logger = logging.getLogger("app")

app = FastAPI()

# CORS 미들웨어 설정
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 요청 ID 미들웨어
@app.middleware("http")
async def add_request_id_and_log(request: Request, call_next):
    request_id = str(uuid.uuid4())
    request.state.request_id = request_id
    
    # 요청 시작 시간
    start_time = time.time()
    
    # 요청 로깅
    logger.info(f"Request started: {request.method} {request.url.path} (ID: {request_id})")
    
    # 다음 미들웨어 또는 엔드포인트 호출
    response = await call_next(request)
    
    # 처리 시간 계산
    process_time = time.time() - start_time
    
    # 응답 로깅
    logger.info(f"Request completed: {request.method} {request.url.path} "
                f"(ID: {request_id}) - Status: {response.status_code} - "
                f"Took: {process_time:.4f}s")
    
    # 응답 헤더에 요청 ID 추가
    response.headers["X-Request-ID"] = request_id
    
    return response

# 기본 라우트
@app.get("/")
def read_root():
    logger.info("Root endpoint called")
    return {"message": "Hello, FastAPI with Logging!"}

# 오류 발생 라우트 (로깅 테스트용)
@app.get("/error")
def trigger_error():
    try:
        # 의도적으로 오류 발생
        1 / 0
    except Exception as e:
        logger.error(f"An error occurred: {str(e)}", exc_info=True)
        return {"error": "An error occurred and was logged"}

# 로그 레벨 테스트 라우트
@app.get("/log-test")
def log_test():
    logger.debug("This is a DEBUG message")
    logger.info("This is an INFO message")
    logger.warning("This is a WARNING message")
    logger.error("This is an ERROR message")
    logger.critical("This is a CRITICAL message")
    return {"message": "Logged messages at different levels"}

# 실행 방법: uvicorn logging.main:app --reload

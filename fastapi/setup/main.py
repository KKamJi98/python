from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# FastAPI 애플리케이션 인스턴스 생성
app = FastAPI(
    title="FastAPI Example API",
    description="FastAPI를 사용한 예제 API 서버입니다.",
    version="0.1.0",
)

# CORS 미들웨어 설정
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 실제 프로덕션에서는 특정 도메인만 허용하는 것이 좋습니다
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 기본 라우트
@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI Example API"}

# 서버 상태 확인 엔드포인트
@app.get("/health")
def health_check():
    return {"status": "healthy"}

# 애플리케이션 시작 이벤트 핸들러
@app.on_event("startup")
async def startup_event():
    print("애플리케이션이 시작되었습니다!")

# 애플리케이션 종료 이벤트 핸들러
@app.on_event("shutdown")
async def shutdown_event():
    print("애플리케이션이 종료됩니다!")

# 실행 방법: uvicorn setup.main:app --reload

import os
import tempfile

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app import models
from app.database import Base, get_db
from app.main import app


@pytest.fixture(scope="function")
def db():
    # 임시 파일 생성
    db_fd, db_path = tempfile.mkstemp()

    # 테스트용 데이터베이스 설정
    test_db_url = f"sqlite:///{db_path}"
    engine = create_engine(test_db_url)
    TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

    # 테스트 데이터베이스 생성
    Base.metadata.create_all(bind=engine)

    # 테스트용 세션 생성
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()
        os.close(db_fd)
        os.unlink(db_path)


@pytest.fixture(scope="function")
def client(db):
    # 테스트용 의존성 오버라이드
    def override_get_db():
        try:
            yield db
        finally:
            pass

    app.dependency_overrides[get_db] = override_get_db

    with TestClient(app) as c:
        yield c

    # 테스트 후 의존성 초기화
    app.dependency_overrides = {}

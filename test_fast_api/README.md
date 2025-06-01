# FastAPI CRUD Application

간단한 FastAPI 기반 CRUD 백엔드 어플리케이션입니다.

## 기능

- SQLite 데이터베이스를 사용한 사용자 정보 저장
- GET Method로 '/' 경로에 'Hello World' 메시지 반환
- 사용자 생성, 조회 API 구현

## 기술 스택

- FastAPI
- SQLAlchemy (ORM)
- SQLite (데이터베이스)
- Poetry (의존성 관리)
- Pytest (테스트)
- Black (코드 포맷팅)
- isort (import 정렬)

## 설치 및 실행

### 필수 요구사항

- Python 3.9 이상
- Poetry

### 설치

```bash
# 의존성 설치
poetry install

# 가상환경 활성화
poetry shell
```

### 실행

```bash
# 개발 서버 실행
uvicorn app.main:app --reload
```

### 테스트

```bash
# 테스트 실행
pytest
```

## API 엔드포인트

- `GET /`: Hello World 메시지 반환
- `POST /users/`: 새 사용자 생성
- `GET /users/`: 모든 사용자 목록 조회
- `GET /users/{user_id}`: 특정 사용자 조회

## 개발 히스토리

- 초기 프로젝트 설정
- 데이터베이스 모델 구현
- API 엔드포인트 구현
- 테스트 작성

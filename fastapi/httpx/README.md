# HTTPX 실습

HTTPX는 Python의 차세대 HTTP 클라이언트 라이브러리로, 동기 및 비동기 요청을 모두 지원하며 현대적인 Python 기능을 활용합니다.

## 설치 방법

```bash
# 기본 설치
pip install httpx

# 비동기 지원을 위한 추가 설치
pip install httpx[http2]
```

## 기본 사용법

### 동기 요청

```python
import httpx

# GET 요청
response = httpx.get("http://localhost:8000/")
print(response.status_code)  # 200
print(response.json())  # {"message": "Hello, FastAPI"}

# 헤더 추가
headers = {"User-Agent": "HTTPX Client", "Accept": "application/json"}
response = httpx.get("http://localhost:8000/", headers=headers)

# 쿼리 파라미터 추가
params = {"skip": 0, "limit": 10}
response = httpx.get("http://localhost:8000/items/", params=params)
```

### 비동기 요청

```python
import httpx
import asyncio

async def fetch_data():
    async with httpx.AsyncClient() as client:
        response = await client.get("http://localhost:8000/")
        return response.json()

# 비동기 함수 실행
data = asyncio.run(fetch_data())
print(data)
```

### POST, PUT, DELETE 요청

```python
import httpx

# POST 요청
data = {"name": "New Item", "price": 45.5}
response = httpx.post("http://localhost:8000/items/", json=data)

# PUT 요청
update_data = {"name": "Updated Item", "price": 99.9}
response = httpx.put("http://localhost:8000/items/1", json=update_data)

# DELETE 요청
response = httpx.delete("http://localhost:8000/items/1")
```

## 고급 기능

### 클라이언트 세션

```python
import httpx

# 클라이언트 세션 생성
with httpx.Client(base_url="http://localhost:8000") as client:
    # 상대 URL 사용
    response = client.get("/")
    print(response.json())
    
    # 다른 엔드포인트 호출
    response = client.get("/items/1")
    print(response.json())
```

### 타임아웃 및 재시도

```python
import httpx

# 타임아웃 설정
client = httpx.Client(timeout=10.0)
response = client.get("http://localhost:8000/")

# 재시도 로직
for attempt in range(3):
    try:
        response = httpx.get("http://localhost:8000/", timeout=5.0)
        break
    except (httpx.TimeoutException, httpx.ConnectError):
        if attempt == 2:
            raise
        continue
```

### 인증

```python
import httpx

# 기본 인증
auth = httpx.BasicAuth(username="user", password="pass")
response = httpx.get("http://localhost:8000/secure", auth=auth)

# Bearer 토큰 인증
headers = {"Authorization": f"Bearer {token}"}
response = httpx.get("http://localhost:8000/secure", headers=headers)
```

## FastAPI와 함께 사용하기

HTTPX는 FastAPI 애플리케이션을 테스트하는 데 매우 유용합니다:

```python
import httpx
from fastapi.testclient import TestClient
from your_app import app

# FastAPI의 TestClient는 내부적으로 HTTPX를 사용합니다
client = TestClient(app)
response = client.get("/")
assert response.status_code == 200
```

## 실무 팁

1. 비동기 클라이언트를 사용하여 동시에 여러 요청 처리
2. 컨텍스트 매니저(`with` 문)를 사용하여 리소스 관리
3. `raise_for_status()`를 사용하여 오류 상태 코드 확인
4. 타임아웃 설정으로 응답 지연 방지
5. 재시도 로직 구현으로 일시적인 네트워크 문제 해결
6. 프록시 설정으로 네트워크 요구사항 충족

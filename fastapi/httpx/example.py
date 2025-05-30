import asyncio
import httpx
from typing import List, Dict, Any

# 동기 요청 예제
def sync_requests_example():
    print("=== 동기 요청 예제 ===")
    
    # 기본 GET 요청
    response = httpx.get("https://httpbin.org/get")
    print(f"GET 응답 상태 코드: {response.status_code}")
    
    # POST 요청 (JSON 데이터)
    data = {"name": "Test Item", "price": 42.5}
    response = httpx.post("https://httpbin.org/post", json=data)
    print(f"POST 응답 상태 코드: {response.status_code}")
    print(f"전송한 데이터: {response.json()['json']}")
    
    # 헤더 추가
    headers = {"User-Agent": "HTTPX-Example", "Custom-Header": "Test Value"}
    response = httpx.get("https://httpbin.org/headers", headers=headers)
    print(f"전송한 헤더: {response.json()['headers']}")
    
    # 쿼리 파라미터
    params = {"param1": "value1", "param2": "value2"}
    response = httpx.get("https://httpbin.org/get", params=params)
    print(f"쿼리 파라미터: {response.json()['args']}")

# 비동기 요청 예제
async def async_requests_example():
    print("\n=== 비동기 요청 예제 ===")
    
    async with httpx.AsyncClient() as client:
        # 여러 요청 동시 실행
        tasks = [
            client.get("https://httpbin.org/get"),
            client.post("https://httpbin.org/post", json={"key": "value"}),
            client.get("https://httpbin.org/headers", headers={"X-Test": "Test"})
        ]
        
        responses = await asyncio.gather(*tasks)
        
        print(f"첫 번째 응답 상태 코드: {responses[0].status_code}")
        print(f"두 번째 응답 상태 코드: {responses[1].status_code}")
        print(f"세 번째 응답 상태 코드: {responses[2].status_code}")

# 클라이언트 세션 예제
def client_session_example():
    print("\n=== 클라이언트 세션 예제 ===")
    
    # 기본 URL과 헤더를 설정한 클라이언트 생성
    with httpx.Client(
        base_url="https://httpbin.org",
        headers={"User-Agent": "HTTPX-Client-Example"}
    ) as client:
        # 상대 경로 사용
        response = client.get("/get")
        print(f"GET 응답 상태 코드: {response.status_code}")
        
        # 다른 엔드포인트 호출
        response = client.post("/post", json={"session": "test"})
        print(f"POST 응답 상태 코드: {response.status_code}")
        
        # 타임아웃 설정
        try:
            response = client.get("/delay/5", timeout=2.0)
        except httpx.TimeoutException:
            print("요청 타임아웃 발생")

# 오류 처리 예제
def error_handling_example():
    print("\n=== 오류 처리 예제 ===")
    
    try:
        # 존재하지 않는 URL
        response = httpx.get("https://httpbin.org/status/404")
        response.raise_for_status()  # 4XX, 5XX 상태 코드에서 예외 발생
    except httpx.HTTPStatusError as e:
        print(f"HTTP 오류: {e.response.status_code}")
    
    try:
        # 연결 오류
        response = httpx.get("https://non-existent-domain.xyz", timeout=2.0)
    except httpx.ConnectError:
        print("연결 오류 발생")
    except httpx.TimeoutException:
        print("타임아웃 발생")

# FastAPI 테스트 클라이언트 사용 예제 (주석 처리: 실제 FastAPI 앱이 필요함)
"""
from fastapi.testclient import TestClient
from your_app import app

def test_client_example():
    print("\n=== FastAPI 테스트 클라이언트 예제 ===")
    
    client = TestClient(app)
    
    # 엔드포인트 테스트
    response = client.get("/")
    print(f"응답 상태 코드: {response.status_code}")
    print(f"응답 내용: {response.json()}")
    
    # POST 요청 테스트
    response = client.post("/items/", json={"name": "Test Item", "price": 42.5})
    print(f"POST 응답 상태 코드: {response.status_code}")
    print(f"생성된 아이템: {response.json()}")
"""

if __name__ == "__main__":
    # 동기 예제 실행
    sync_requests_example()
    
    # 클라이언트 세션 예제 실행
    client_session_example()
    
    # 오류 처리 예제 실행
    error_handling_example()
    
    # 비동기 예제 실행
    asyncio.run(async_requests_example())
    
    # FastAPI 테스트 클라이언트 예제 실행 (주석 처리됨)
    # test_client_example()

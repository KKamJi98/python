# HTTPie 실습

HTTPie는 사용자 친화적인 HTTP 클라이언트 커맨드 라인 도구로, API 테스트 및 디버깅에 매우 유용합니다.

## 설치 방법

```bash
# pip를 사용한 설치
pip install httpie

# macOS에서 Homebrew를 사용한 설치
brew install httpie
```

## 기본 사용법

### GET 요청

```bash
# 기본 GET 요청
http GET http://localhost:8000/

# 헤더 추가
http GET http://localhost:8000/ User-Agent:HTTPie Accept:application/json

# 쿼리 파라미터 추가
http GET http://localhost:8000/items/ skip==0 limit==10
```

### POST 요청

```bash
# JSON 데이터 전송
http POST http://localhost:8000/items/ name=Item price:=42.5

# 폼 데이터 전송
http --form POST http://localhost:8000/login username=user password=pass

# 파일 업로드
http --form POST http://localhost:8000/upload file@/path/to/file
```

### PUT 및 DELETE 요청

```bash
# PUT 요청
http PUT http://localhost:8000/items/1 name=UpdatedItem price:=99.9

# DELETE 요청
http DELETE http://localhost:8000/items/1
```

## 고급 기능

### 인증

```bash
# 기본 인증
http -a username:password GET http://localhost:8000/secure

# Bearer 토큰 인증
http GET http://localhost:8000/secure Authorization:"Bearer token123"
```

### 요청 및 응답 저장

```bash
# 응답 저장
http GET http://localhost:8000/ > response.json

# 요청 및 응답 저장
http --output=response.json --print=hb GET http://localhost:8000/
```

### 세션 유지

```bash
# 세션 생성 및 사용
http --session=mysession GET http://localhost:8000/login
http --session=mysession GET http://localhost:8000/profile
```

## FastAPI와 함께 사용하기

HTTPie는 FastAPI 애플리케이션을 테스트하는 데 매우 유용합니다:

```bash
# FastAPI 엔드포인트 테스트
http GET http://localhost:8000/docs

# JSON 응답 확인
http GET http://localhost:8000/items/1 | jq

# 헤더 및 상태 코드 확인
http -v GET http://localhost:8000/items/1
```

## 실무 팁

1. `-v` 플래그를 사용하여 상세한 요청/응답 정보 확인
2. `--debug` 옵션으로 디버깅 정보 표시
3. `--print=HBhb` 옵션으로 요청 헤더(H), 본문(B), 응답 헤더(h), 응답 본문(b) 표시
4. `jq`와 함께 사용하여 JSON 응답 처리
5. 환경 변수를 활용한 기본 URL 설정: `export API_URL=http://localhost:8000`

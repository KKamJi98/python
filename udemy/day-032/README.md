# Goals: Email SMTP and the datetime module - 자동 생일 축하기

## SMTP(Simple Mail Transfer Protocol)

- 이메일 전송을 위한 표준 통신 프로토콜, 기본적으로 `25`번포트 사용 but 보안 통신을 위해 `587`(STARTTLS 암호화) 또는 `465`(SSL 암호화)포트도 자주 사용됨
- **SMTP**는 단순히 이메일을 전송하는 데 초점을 맞춘 프로토콜이며, 이메일의 수신을 처리하지 않음
- 이메일을 받을 때는 `POP3` 또는 `IMAP`을 사용

### SMTP의 주요 기능

1. 이메일 전송
2. 서버 간 이메일 전송


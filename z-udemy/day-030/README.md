# Goals: try, catch, except, finally, json data

### Try

실행할 코드를 포함하여, 예외가 발생할 가능성이 있는 코드 작성

### Except

`try` 블록에서 예외가 발생하면, `except` 블록에서 그 예외를 처리. 특정 예외 타입을 지정하거나, 모든 예외를 처리할 수 있음

### else (Optional)

`try` 블록에서 예외가 발생하지 않았을 때만 실행되는 블록.

### finally (Optional)

`try`, `except`, `else` 블록에서 예외가 발생하든 발생하지 안든 항상 실행되는 블록 (주로 파일을 닫거나, 자원을 해제하는 등의 작업에 사용)

```python
try:
    file = open("example.txt", "r")
    content = file.read()
    print(content)
except FileNotFoundError:
    print("파일을 찾을 수 없습니다.")
else:
    print("파일을 성공적으로 읽었습니다.")
finally:
    file.close()  # 파일이 열려 있다면 닫음
    print("파일을 닫습니다.")
```

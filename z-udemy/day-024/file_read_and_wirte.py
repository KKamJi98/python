## 1번 방법.
# file = open("test_file.txt")
# contents = file.read()
# print(contents)
# file.close()

## 2번 방법 (close를 하지 않아도 됨)
# with open("test_file.txt") as file:
#     contents = file.read()
#     print(contents)

## 쓰기 작업 (r => 읽기모드(default) w => 쓰기모드 a => 추가 모드)
with open("test_file.txt", mode="w") as file:
    file.write("New text.")
    file.write("New text.")

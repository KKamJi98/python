# 조건이 참인 블록을 반복으로 실행하는 반복문 => while


# 예시 - num1부터 num2까지 더하기
def sum(num1, num2):
    result = 0
    while num1 != num2 + 1:
        result += num1
        num1 += 1

    return result


print(sum(1, 10))

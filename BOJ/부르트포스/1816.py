# 암호키(백준 1816번)
# 1을 제외한 약수가 1,000,000보다 커야 성공


from sys import stdin
input = stdin.readline

T = int(input())

# 간소화
# def validate_password(password):
#    return next(("NO" for n in range(2, 1000001) if password % n == 0), "YES")

def validate_password(password):
    for n in range(2, 1000001):
        if password % n == 0:
            return "NO"
    return "YES"


for _ in range(T):
    password = int(input())
    print(validate_password(password))

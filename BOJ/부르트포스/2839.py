# 설탕배달(백준 2839번)

# 입력
# 18

# 출력
# 4

n = int(input())

bags = 0
while n > 0:
    if n % 5 == 0:
        bags += (n // 5)
        print(bags)
        break
    elif n < 3:
        print(-1)
        break
    n -= 3
    bags += 1
    if n == 0:
        print(bags)
        break

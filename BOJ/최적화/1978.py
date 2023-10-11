# 소수찾기(백준 1978번)
# 주어진 수 N개에서 소수가 몇 개인지 찾아서 출력하는 프로그램

# 입력
# 4
# 1 3 5 7

# 출력
# 3

# 아이디어: 모든 수의 약수의 절반 혹은 절반-1 은 해당 수의 루트를 씌운 값보다 작거나 같다.

from sys import stdin

input = stdin.readline

N = int(input())
numbers = list(map(int, input().split()))

answer = []
for i in numbers:
    if i == 1:
        continue
    prime = True
    max_int =  int(i ** 0.5)
    for j in range(2, max_int + 1):
        if i % j == 0:
            prime = False
            break
    answer.append(prime)
    
print(answer.count(True))


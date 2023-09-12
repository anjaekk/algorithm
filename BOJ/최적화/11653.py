# 소인수분해(백준 11653번)
# 입력-1
# 72

# 출력-1
# 2
# 2
# 2
# 3
# 3

# 입력-2
# 9991

# 출력-2
# 97
# 103

from sys import stdin

input = stdin.readline

N = int(input())

while N > 1:
    for i in range(2, N+1):
        if N % i == 0:
            print(i)
            N //= i
            break

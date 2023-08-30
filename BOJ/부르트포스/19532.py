# 수학은 비대면강의입니다(백준 19532번)
# ax + by = c
# dx + ey = f

# 입력
# 1 3 -1 4 1 7

# 출력
# 2 -1

import itertools
from sys import stdin

input = stdin.readline

a, b, c, d, e, f = map(int, input().split())

def equation(a, b, c, d, e, f):
    for x, y in itertools.product(range(-999, 1000), range(-999, 1000)):
        if a*x + b*y == c and d*x + e*y == f:
            return f"{x} {y}"

print(equation(a, b, c, d, e, f))

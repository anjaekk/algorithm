# 2017 연세대학교 프로그래밍 경시대회(백준 14568번)

# 조건
# 남는 사탕은 없어야 한다.
# 남규는 영훈이보다 2개 이상 많은 사탕을 가져야 한다.
# 셋 중 사탕을 0개 받는 사람은 없어야 한다.
# 택희가 받는 사탕의 수는 홀수개가 되어서는 안 된다.

# 사탕 N개를 3명에게 나눠주는 경우의 수

# 입력
# 6

# 출력
# 1

from sys import stdin

input = stdin.readline

candy = int(input())

def case(candy: int) -> int:
    case = 0
    if candy < 6:
        return case
    
    for N in range(1, candy+1):
        for Y in range(1, candy+1):
            for T in range(1, candy+1):
                if N >= Y + 2 and T % 2 == 0 and N + Y + T == candy:
                    case += 1
    return case

print(case(candy))

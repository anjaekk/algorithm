# 청기 백기(백준 15736번)
#선수 N명, 깃발 N개
#청색이 위로 보이도록 놓여있다.
#1번선수 -> 1의 배수, 2번선수 -> 2의 배수, i번선수 -> i배수
#백색이 위로 놓여있는 깃발의 수 출력

# 입력-1
# 3
# 출력-1
# 1

# 입력-2
# 24
# 출력-2
# 4

# 결과 값은 각 깃발개수의 최소 제곱근 값이 된다는 규칙 발견

from sys import stdin

input = stdin.readline


def flag_game_v1():
    N = int(input()) # 선수와 깃발 개수
    flag = ["B" for _ in range(N+1)] # 인덱스 0부터 시작 청색 깃발로 초기화
    
    if N == 1:
        return 1
    for i in range(1, N+1):
        for j in range(i, N+1, i):
            if flag[j] == "B":
                flag[j] = "W"
            else:
                flag[j] = "B"
    return flag.count("W")



def flag_game_v2():
    N = int(input()) # 선수와 깃발 개수
    if N < 3:
        return 1
    for i in range(N):
        if i**2 == N:
            return i
        if i**2 > N:
            return i-1

#루트 값으로 간편하게 구하기
def flag_game_v3():
    N = int(input()) # 선수와 깃발 개수
    return int(N**0.5)

print(flag_game_v3())

# 1, 2, 3 더하기(백준 9095번)
# 합의 경우의 수 구하기

# 입력
# 3
# 4
# 7
# 10

# 출력
# 7
# 44
# 274


from sys import stdin

input = stdin.readline

cases = int(input())

def solution(num):
    d = [0] * 12
    d[1] = 1 # 1
    d[2] = 2 # 2, 1+1
    d[3] = 4 # 3, 1+2, 2+1, 1+1+1

    # 점화식
    # d[n] = d[n-3] + d[n-2] + d[n-1]
    # 직접 5, 6까지 만들어보면서 찾을 수도 있지만 원리는 다음과 같다
    # 4를 1, 2, 3을 가지고 만들 수 있는 경우의 수라면
    # 4-1에서 1을 더해야만 = 4 완성
    # 4-2에서 2를 더해야만 = 4 완성
    # 4-3에서 3을 더해야만 = 4 완성
    # 그러므로 위의 3가지 경우의 수를 더하면 [n-3] + [n-2] + [n-1]가 된다.
    for i in range(4, num+1):
        d[i] = d[i-3] + d[i-2] + d[i-1]
    return d[num]
    

for _ in range(cases):
    num = int(input())
    print(solution(num))

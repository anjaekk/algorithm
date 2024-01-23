# 욕심쟁이 판다(백준 1937번)-DP

# 입력
# 4
# 14 9 12 10
# 1 11 5 4
# 7 15 2 13
# 6 3 16 8

# 출력
# 4

# 아이디어
# 모든 점을 방문
# 이동할 수 있는 모든 경우의 수를 재귀로 구현
# 재귀로 구현한 후 DP로 변경


import sys
sys.setrecursionlimit(500000)

input = sys.stdin.readline

n = int(input())
# n = 4
graph = [list(map(int, input().split())) for _ in range(n)]

# graph = [[14, 9, 12, 10], [1, 11, 5, 4], [7, 15, 2, 13], [6, 3, 16, 8]]
dp = [[ 0 for _ in range(n)] for _ in range(n)]

def recur(x, y):
    if dp[x][y] != 0:
        return dp[x][y]

    dx = (0, 0, 1, -1)
    dy = (1, -1, 0, 0)

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if n > nx >= 0 and n > ny >= 0 and graph[x][y] < graph[nx][ny]:
            dp[x][y] = max(dp[x][y], recur(nx, ny) + 1)
        
    return dp[x][y]


for i in range(n):
    for j in range(n):
        recur(i, j)

print(max(map(max, dp)) + 1) # 시작 자리부터 +1


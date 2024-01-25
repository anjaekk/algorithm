
# 내리막 길(백준 1520번)

# 입력
# 4 5
# 50 45 37 32 30
# 35 50 40 20 25      
# 30 30 25 17 28
# 27 24 22 15 10

# 출력
# 3

import sys

sys.setrecursionlimit(10000000)
input = sys.stdin.readline

M, N = map(int, input().split()) #4, 5
# M, N= 4, 5
graph = [list(map(int, input().split())) for i in range(M)]
# graph = [[50, 45, 37, 32, 30], [35, 50, 40, 20, 25], [30, 30, 25, 17, 28], [27, 24, 22, 15, 10]]

dp = [[-1 for _ in range(N)] for _ in range(M)] 
# 0으로 할 경우 갈곳이 없어서 0인 경우에도 계속해서 방문을 하게되니 미방문은 -1로 표시

def recur(x, y):
    if x == M-1 and y == N-1: 
        return 1
    
    if dp[x][y] != -1: return dp[x][y]

    dx = (0, 0, 1, -1)
    dy = (1, -1, 0, 0)

    route = 0
    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y

        if M > nx >= 0 and N > ny >= 0 and graph[nx][ny] < graph[x][y]:
            route += recur(nx, ny)

    dp[x][y] = route
    return dp[x][y]

print(recur(0, 0))



# 현수막(백준 14716번)-그래프
# 입력
# 8 19
# 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
# 0 0 0 1 0 0 0 1 0 0 0 1 0 1 1 1 1 1 0
# 0 0 1 0 1 0 0 1 1 0 0 1 0 0 0 1 0 0 0
# 0 1 0 0 0 1 0 1 0 1 0 1 0 0 0 1 0 0 0
# 0 1 1 1 1 1 0 1 0 1 0 1 0 0 0 1 0 0 0
# 0 1 0 0 0 1 0 1 0 0 1 1 0 0 0 1 0 0 0
# 0 1 0 0 0 1 0 1 0 0 0 1 0 0 0 1 0 0 0
# 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0

# 출력
# 3


import sys
from collections import deque

sys.setrecursionlimit(10**9)

input = sys.stdin.readline

M, N = map(int, input().split()) #세로 #가로

graph = [list(map(int, input().split())) for _ in range(M)]
visited = [[False] * N for _ in range(M)]


dx = [1, -1, 0, 0, 1, 1, -1, -1]
dy = [0, 0, 1, -1, 1, -1, 1, -1]

def dfs(x, y):
    global visited
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
        if (0 <= nx < M and 0 <= ny < N and
        visited[nx][ny] == False and graph[nx][ny] == 1):
            visited[nx][ny] = True
            dfs(nx, ny)
    return 


cnt = 0
for i in range(M):
    for j in range(N):
        if visited[i][j] == False and graph[i][j] == 1:
            visited[i][j] = True
            dfs(i, j)
            cnt += 1

print(cnt)

# 그림(백준 1926번)

# 입력
# 6 5
# 1 1 0 1 1
# 0 1 1 0 0
# 0 0 0 0 0
# 1 0 1 1 1
# 0 0 1 1 1
# 0 0 1 1 1

# 출력
# 4
# 9

from collections import deque
import sys


sys.setrecursionlimit(10000000)
input = sys.stdin.readline

n, m = map(int, input().split()) # 세로, 가로
graph = [list(map(int, input().split())) for _ in range(n)]

# Test
# n = 6
# m = 5
# graph = [[1, 1, 0, 1, 1], [0, 1, 1, 0, 0], [0, 0, 0, 0, 0], [1, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1]]

# n = 3
# m = 3
# graph = [[1, 1, 1], [1, 0, 0], [1, 0, 0]]

visited = [[0] * m for _ in range(n)]


dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)

def dfs(x, y):
    global max_size, cnt
    max_size = max(max_size, cnt)
    for i in range(4):
        nx = x + dx[i] # x축
        ny = y + dy[i] # y축
        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and graph[nx][ny]:
            visited[nx][ny] = 1
            cnt += 1
            dfs(nx, ny)

import itertools
paintings = 0
max_size = 0

if __name__ == "__main__":
    if n == 1 and m == 1:
        print(graph[0][0])
        print(graph[0][0])
    else: 
        for i, j in itertools.product(range(n), range(m)):
            if visited[i][j] == 0 and graph[i][j] == 1:
                visited[i][j] = 1
                cnt = 1
                dfs(i, j)
                paintings += 1
        print(paintings)
        print(max_size)

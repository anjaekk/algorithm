# 단지번호붙이기(백준 2667번)

# 입력
# 7
# 0110100
# 0110101
# 1110101
# 0000111
# 0100000
# 0111110
# 0111000

# 출력
# 3
# 7
# 8
# 9

from collections import deque
import sys
sys.setrecursionlimit(100000)

n = int(input())
home = [list(map(int, input())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
visited = [[0]*n for _ in range(n)]

results = []
homes = 1
def dfs(x, y):
    global homes
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < n and\
            not visited[nx][ny] and home[nx][ny]:
            visited[nx][ny] = 1
            homes += 1
            dfs(nx, ny)

for i in range(n):
    for j in range(n):
        if not visited[i][j] and home[i][j]:
            visited[i][j] = 1
            dfs(i, j)
            results.append(homes)
            homes = 1

print(len(results))
for i in sorted(results):
    print(i)

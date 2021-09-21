# BOJ2178(bfs)

from sys import stdin
from collections import deque

input = stdin.readline

n, m = map(int, input().split()) # 목표위치(세로, 가로)
graph = [list(str(input())) for _ in range(n)] 
visited = [[0] * m for i in range(n)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

queue = deque()
queue.append((0, 0))
visited[0][0] = 1
answer = 1

while queue:
    x, y = queue.popleft()

    if x == n-1 and y == m-1:
            print(visited[x][y])

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < m:
            if graph[nx][ny] == "1" and not visited[nx][ny]:
                visited[nx][ny] = visited[x][y] + 1   # visited[x][y]의 상,하,좌,우는 모두 x, y값 + 1
                queue.append((nx, ny))

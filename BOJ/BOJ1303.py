# BOJ1303(bfs)

from sys import stdin
from collections import deque

input = stdin.readline

n, m = map(int, input().split()) # 가로, 세로
white = blue = 0

# graph 초기화
graph = [list(input()) for _ in range(m)]
# visited 리스트 생성
visited = [[0]*n for i in range(m)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def bfs(x, y, color):
    cnt = 1
    queue = deque()
    queue.append((x, y))
    visited[x][y] = 1
    
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i] # 세로
            ny = y + dy[i] # 가로

            if 0 <= nx < m and 0 <= ny < n:
                if graph[nx][ny] == color and not visited[nx][ny]:
                    visited[nx][ny] = True
                    queue.append((nx, ny))
                    cnt += 1
    
    return cnt


for i in range(m): #세로
    for j in range(n): #가로
        if graph[i][j] == "W" and not visited[i][j]:
            white += bfs(i, j, "W")**2
        elif graph[i][j] == "B" and not visited[i][j]:
            blue += bfs(i, j, "B")**2

print(white, blue)

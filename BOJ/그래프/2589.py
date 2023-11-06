# 보물섬(백준 2589번)-그래프

# 입력
# 5 7 # 세로, 가로
# WLLWWWL  # L: 육지, W: 바다
# LLLWLLL
# LWLWLWW
# LWLWLLL
# WLLWLWW

# 출력
# 8


from collections import deque
from sys import stdin

input = stdin.readline

M, N = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(M)]

dx = (0, 0, 1, -1)
dy = (1, -1, 0, 0)


def bfs(i, j):
    global visited

    distance = 1
    queue = deque()
    queue.append((distance, i, j))

    distances = []
    while queue:
        distance, x, y = queue.popleft()
        for n in range(4):
            nx = x + dx[n]
            ny = y + dy[n]
            if (0 <= nx < M and 0 <= ny < N and
                not visited[nx][ny] 
                and graph[nx][ny] == 'L'):
                distances.append(distance)
                visited[nx][ny] = True
                queue.append((distance + 1, nx, ny))
    return max(distances, default=0)


answer = 0
for i in range(M):
    for j in range(N):
        if graph[i][j] == 'L':
            visited = [[False] * N for _ in range(M)]
            visited[i][j] = True
            distance = bfs(i, j)
            answer = max(answer, distance)


print(answer)

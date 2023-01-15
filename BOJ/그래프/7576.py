# 토마토(백준 7576번)
# 입력
# 6 4 #m: 가로, n:세로
# 0 0 0 0 0 0
# 0 0 0 0 0 0
# 0 0 0 0 0 0
# 0 0 0 0 0 1

# 출력
# 8
# 1: 익은토마토, 0: 안익은 토마토, -1: 비어있는 칸

from collections import deque

m, n = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

queue = deque()

def bfs():    
    while queue:
        y, x = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < m and 0 <= ny < n and box[ny][nx] == 0:
                box[ny][nx] = box[y][x] + 1
                queue.append((ny, nx))

for i in range(n):
    for j in range(m):
        if box[i][j] == 1:
            queue.append((i, j))

bfs()

day = 0
for k in range(n):
    for l in range(m):
        if box[k][l] == 0:
            print(-1)
            exit(0)
        elif box[k][l] > 0:
            day = max(box[k][l], day)
print(day-1)



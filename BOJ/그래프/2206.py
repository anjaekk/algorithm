# 벽 부수고 이동하기(백준 2206번)
# 입력
# 6 4  # 세로, 가로
# 0100
# 1110
# 1000
# 0000
# 0111
# 0000

# 출력
# 15

# 최단경로(벽부시기 1개 가능)

from collections import deque

n, m = map(int, input().split())
board = [list(map(int, input())) for _ in range(n)]
#board = [[0, 1, 0, 0], [1, 1, 1, 0], [1, 0, 0, 0], [0, 0, 0, 0], [0, 1, 1, 1], [0, 0, 0, 0]]

#3차원 행렬 이용 벽파괴 파악. visited[x][y][0]은 벽 파괴 가능. [x][y][1]은 불가능.
visited = [[[0, 0] for _ in range(m)] for _ in range(n)]
#visited = [
# [[0, 0], [0, 0], [0, 0], [0, 0]], 
# [[0, 0], [0, 0], [0, 0], [0, 0]], 
# [[0, 0], [0, 0], [0, 0], [0, 0]], 
# [[0, 0], [0, 0], [0, 0], [0, 0]], 
# [[0, 0], [0, 0], [0, 0], [0, 0]], 
# [[0, 0], [0, 0], [0, 0], [0, 0]]
# ]

visited[0][0][0] = 1
dx, dy = (-1, 1, 0, 0), (0, 0, -1, 1)

def bfs(x, y, z):
    queue = deque()
    queue.append((x, y, z))
    while queue:
        x, y, flag = queue.popleft() # 세로, 가로, 

        if x == n-1 and y == m-1: # 목적지 도착
            return visited[x][y][flag]
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                # 벽 부수기
                if flag == 0 and board[nx][ny]: # flag == 0 --> 벽 부수기 가능
                    visited[nx][ny][1] = visited[x][y][0] + 1 # 
                    queue.append((nx, ny, 1))
                # 벽 부수지 않기
                elif not board[nx][ny] and visited[nx][ny][flag] == 0:
                    visited[nx][ny][flag] = visited[x][y][flag] + 1
                    queue.append((nx, ny, flag))
    return -1

print(bfs(0, 0, 0))

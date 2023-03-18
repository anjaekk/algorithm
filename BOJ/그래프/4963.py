# 그래프
# 섬의 개수(백준 4963번)
# 입력
# 1 1 # 너비, 높이 
# 0

# 2 2
# 0 1
# 1 0

# 3 2
# 1 1 1
# 1 1 1

# 5 4
# 1 0 1 0 0
# 1 0 0 0 0
# 1 0 1 0 1
# 1 0 0 1 0

# 5 4
# 1 1 1 0 1
# 1 0 1 0 1
# 1 0 1 0 1
# 1 0 1 1 1

# 5 5
# 1 0 1 0 1
# 0 0 0 0 0
# 1 0 1 0 1
# 0 0 0 0 0
# 1 0 1 0 1

# 0 0 # 입력 종료

# 출력(섬의 개수)
# 0
# 1
# 1
# 3
# 1
# 9

# 1 = 땅, 0 = 바다

import sys
sys.setrecursionlimit(1500)

dx = [-1, 1, 0, 0, 1, -1, 1, -1]
dy = [0, 0, 1, -1, 1, -1, -1, 1]



def dfs(data, x, y, w, h):
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
    
        if 0 <= nx < h and 0 <= ny < w and \
            not visited[nx][ny] and data[nx][ny]:
            visited[nx][ny] += 1
            dfs(data, nx, ny, w, h)

while True:
    w, h = map(int, input().split())
    if not w and not h:
        break
    data = [list(map(int, input().split())) for _ in range(h)]
    global visited
    visited = [[0] * w for _ in range(h)]
    cnt = 0
    for i in range(h):
        for j in range(w):
            if not visited[i][j] and data[i][j]:
                visited[i][j] += 1
                dfs(data, i, j, w, h)
                cnt += 1
    print(cnt)

# 안전영역(백준 2468번)

# 입력
# 5
# 6 8 2 6 2
# 3 2 3 4 6
# 6 7 3 3 2
# 7 2 5 3 6
# 8 9 5 2 7

# 출력
# 5


import sys
sys.setrecursionlimit(100000)

n = int(input())
land = [list(map(int, input().split())) for _ in range(n)]

highest = 0
for i in land:
    highest = max(i+[highest])

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(rain, y, x):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0<= ny < n and \
            visited[ny][nx] == 0 and land[ny][nx] > rain:
            visited[ny][nx] = 1
            dfs(rain, ny, nx)

results = [1]
for i in range(highest):
    visited = [[0]*n for _ in range(n)]
    cnt = 0
    for j in range(n):
        for k in range(n):
            if visited[j][k] == 0 and land[j][k] > i:
                visited[j][k] = 1
                cnt += 1
                dfs(i, j, k)
    results.append(cnt)

print(max(results))

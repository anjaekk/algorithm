# # 유기농 배추(백준 1012번)
# 입력
# 2  # 테스트 개수
# 10 8 17  # 가로, 세로, 배추 심어져있는 수
# 0 0
# 1 0
# 1 1
# 4 2
# 4 3
# 4 5
# 2 4
# 3 4
# 7 4
# 8 4
# 9 4
# 7 5
# 8 5
# 9 5
# 7 6
# 8 6
# 9 6
# 10 10 1  # 가로 m, 세로 n, 배추 심어져있는 수
# 5 5

# 출력
# 5
# 1

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(y, x, n, m):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < m and 0 <= ny < n and \
            not visited[ny][nx] and land[ny][nx]:
            visited[ny][nx] = 1
            dfs(ny, nx, n, m)


case = int(input())
for _ in range(case):
    m, n, cabbage = map(int, input().split())
    global land, visited
    land = [[0]*m for _ in range(n)]
    visited = [[0]*m for _ in range(n)]
    for _ in range(cabbage):
        x, y = map(int, input().split())
        land[y][x] = 1
    count= 0
    for l in range(n):
        for k in range(m):
            if not visited[l][k] and land[l][k]:
                count += 1
                visited[l][k] = 1
                dfs(l, k, n, m)
    print(count)

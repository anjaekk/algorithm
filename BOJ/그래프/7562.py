# 그래프
# 나이트의 이동(백준 7562번)
# 입력
# 3   # 테스트 개수
# 8   # 체스판 한변의 길이
# 0 0 # 나이트가 현재 있는 칸
# 7 0 # 나이트가 이동하려고 하는 칸
# 100
# 0 0
# 30 50
# 10
# 1 1
# 1 1

# 출력
# 5
# 28
# 0


from collections import deque
#x축, y축
direction = [(1, -2), (2, -1), (-1, -2), (-2, -1), (2, 1), (1, 2), (-1, 2),(-2, 1)]


def bfs(now, destination, board):
    queue = deque()
    queue.append(now)

    while queue:
        x, y = queue.popleft()
        if destination[0] == x and destination[1] == y:
            break
        for i in direction:
            nx = i[0] + x
            ny = i[1] + y
            if 0 <= nx < n and 0 <= ny < n and not board[nx][ny]:
                board[nx][ny] = board[x][y] + 1
                queue.append((nx, ny))

    print(board[x][y]-1)


test = int(input())

for _ in range(test):
    n = int(input())
    now = list(map(int, input().split()))
    destination = list(map(int, input().split()))
    board = [[0] * n for _ in range(n)]
    board[now[0]][now[1]] = 1
    cnt = bfs(now, destination, board)

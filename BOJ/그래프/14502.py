# 바이러스(백준 14502번)
# 입력
# 7 7    # n: 세로, m:가로 
# 2 0 0 0 1 1 0
# 0 0 1 0 1 2 0
# 0 1 1 0 1 0 0
# 0 1 0 0 0 0 0
# 0 0 0 0 0 1 1
# 0 1 0 0 0 0 0
# 0 1 0 0 0 0 0

# 출력
# 27

# 0: 빈칸, 1: 벽, 2: 바이러스

import itertools
import copy
from collections import deque

n, m = map(int, input().split())
lap = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0] # x축 이동
dy = [0, 0, -1, 1] # y축 이동

virus_list = deque()
result = 0

def bfs():
    # virus list 만들기
    temp_lap = copy.deepcopy(lap) # deepcopy를 통해 temp_lap생성
    for i, j in itertools.product(range(n), range(m)):
        if temp_lap[i][j] == 2:
            virus_list.append((i, j))

    while virus_list:
        y, x = virus_list.popleft()
        for k in range(4):
            nx = dx[k] + x
            ny = dy[k] + y
            
            if 0 <= nx < m and 0 <= ny < n and temp_lap[ny][nx] == 0:
                temp_lap[ny][nx] = 2
                virus_list.append((ny, nx))
    
    # 감염 안된 0 개수 세기
    global result
    temp_cnt = sum(temp_lap[k].count(0) for k in range(n))
    result = max(temp_cnt, result)

# 벽 3개 선택
def select_wall(wall_cnt):
    if wall_cnt == 3:
        bfs()
        return
    for i, j in itertools.product(range(n), range(m)):
        if lap[i][j] == 0:
            lap[i][j] = 1
            select_wall(wall_cnt+1)
            lap[i][j] = 0

select_wall(0)
print(result)

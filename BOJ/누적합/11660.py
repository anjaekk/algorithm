# 백준 구간합 구하기(11660)

# 입력
# 4 3      # 표의 크기(N*N), 구해야 하는 횟수(M번)
# 1 2 3 4  # 표 
# 2 3 4 5  # 표
# 3 4 5 6  # 표
# 4 5 6 7  # 표
# 2 2 3 4  # (2, 2) 에서 (3, 4) 
# 3 4 3 4  # (3, 4) 에서 (3, 4)
# 1 1 4 4  # (1, 1) 에서 (4, 4)

# 출력
# 27
# 6
# 64



N, M = map(int, input().split(" "))

metrix = [list(map(int, input().split(" "))) for _ in range(N)]
sum_list = [list(map(int, input().split(" "))) for _ in range(M)]

sum_metrix = [[0]*(N+1) for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, N+1):
        sum_metrix[i][j] = metrix[i-1][j-1] + sum_metrix[i-1][j] + sum_metrix[i][j-1] - sum_metrix[i-1][j-1]

for x1, y1, x2, y2 in sum_list:
    result = sum_metrix[x2][y2] - sum_metrix[x2][y1-1] - sum_metrix[x1-1][y2] + sum_metrix[x1-1][y1-1]
    print(result)

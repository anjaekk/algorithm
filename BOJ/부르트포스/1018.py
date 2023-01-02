# 체스판 다시 칠하기(백준 1018번)

# 입력
# 8 8      # N(세로), M(가로)
# WBWBWBWB
# BWBWBWBW
# WBWBWBWB
# BWBBBWBW
# WBWBWBWB
# BWBWBWBW
# WBWBWBWB
# BWBWBWBW

# 출력
# 1

# N = 8
# M = 8
# board = [
#     "WBWBWBWB",
#     "BWBWBWBW",
#     "WBWBWBWB",
#     "BWBBBWBW",
#     "WBWBWBWB",
#     "BWBWBWBW",
#     "WBWBWBWB",
#     "BWBWBWBW",
# ]

N, M = map(int, input().split())
board = [input() for _ in range(N)]
cnt_list = []

for i in range(N-7):
    for j in range(M-7):
        case1 = 0
        case2 = 0
        for k in range(i, i+8):
            for l in range(j, j+8):
                if (k+l) % 2 == 0:
                    if board[k][l] != "W":
                        case1 += 1
                    elif board[k][l] != "B":
                        case2 += 1
                else:
                    if board[k][l] != "B":
                        case1 += 1
                    elif board[k][l] != "W":
                        case2 += 1
        cnt_list.append(min(case1, case2))

print(min(cnt_list))




#########################################################################
# 코드 리팩토링

import itertools
N, M = map(int, input().split())
board = [input() for _ in range(N)]
cnt_list = []

for i, j in itertools.product(range(N-7), range(M-7)):
    case1 = 0
    case2 = 0
    for k, l in itertools.product(range(i, i+8), range(j, j+8)):
        if (
            (k + l) % 2 == 0
            and board[k][l] != "W"
            or (k + l) % 2 != 0
            and board[k][l] != "B"
        ):
            case1 += 1
        else:
            case2 += 1
    cnt_list.append(min(case1, case2))

print(min(cnt_list))

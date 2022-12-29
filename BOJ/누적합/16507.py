# 어두운 건 무서워(백준 16507)
# 입력
# 5 6 1         # 사진크기 세로 R, 가로 C, 찾기 횟수 Q
# 4 1 3 4 9 5
# 1 2 8 7 5 5
# 8 1 2 5 3 2
# 1 5 3 4 2 5
# 5 2 1 2 3 5
# 2 2 4 5

# 출력
# 3

R, C, Q = map(int, input().split())

metrix = [
    list(map(int, input().split())) 
    for _ in range(R)
]
find = [
    list(map(int, input().split())) 
    for _ in range(Q)
]

sum_metrix = [[0]*(C+1) for _ in range(R+1)]

for i in range(1, R+1):
    for j in range(1, C+1):
        sum_metrix[i][j] = metrix[i-1][j-1] + sum_metrix[i-1][j] + sum_metrix[i][j-1] - sum_metrix[i-1][j-1]
    
for r1, c1, r2, c2 in find:
    sum_result = sum_metrix[r2][c2] - sum_metrix[r1-1][c2] - sum_metrix[r2][c1-1] + sum_metrix[r1-1][c1-1]
    result = sum_result // ((r2-r1+1)*(c2-c1+1))
    print(result)

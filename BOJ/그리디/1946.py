# 그리디
# 신입 사원(백준 1946번)

# 입력
# 2  # test cases
# 5  # 지원자 수
# 3 2 # 서류심사 순위, 면접심사 순위
# 1 4
# 4 1
# 2 3
# 5 5
# 7
# 3 6
# 7 3
# 4 2 #
# 1 4 #
# 5 7
# 2 5 
# 6 1 #

# 출력
# 4  # 선발할 수 
# 3

from sys import stdin

input = stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    data = [list(map(int, input().split())) for _ in range(n)]
    data.sort() # [[1, 4], [2, 5], [3, 6], [4, 2], [5, 7], [6, 1], [7, 3]]
    cnt = 1 # 1등은 무조건 포함
    temp = data[0][1]
    for i in range(1, n):
        if data[i][1] < temp:
            temp = data[i][1]
            cnt += 1

    print(cnt)

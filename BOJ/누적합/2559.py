# 수열(백준 2559번)
# 입력: 온도를 측정한 날짜 수, 연속적 날짜 수
# 출력: 합의 최대 

# 입력-1
# 10 2
# 3 -2 -4 -9 0 3 7 13 8 -3
# 출력-1
# 21

# 입력-2
# 10 5
# 3 -2 -4 -9 0 3 7 13 8 -3
# 출력-2
# 31


from sys import stdin

input = stdin.readline

N, K = map(int, input().split())
temperatures = list(map(int, input().split()))

max_num = None
last_sum = 0
for i in range(N-K+1):
    if i == 0:
        last_sum = sum(temperatures[i:i+K])
    else:
        last_sum = last_sum - temperatures[i-1] + temperatures[i+K-1]

    max_num = last_sum if max_num is None else max(max_num, last_sum)
print(max_num)


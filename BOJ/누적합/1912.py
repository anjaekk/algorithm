# 연속합(백준 1912번)

# 입력-1
# 10
# 10 -4 3 1 5 6 -35 12 21 -1
# 출력-1
# 33

# 입력-2
# 10
# 2 1 -4 3 4 -4 6 5 -5 1
# 출력-2
# 14

# 입력-3
# 5
# -1 -2 -3 -4 -5
# 출력-3
# -1

#3
# 1 5 -3 100
# 1 5 -3 1

from sys import stdin

input = stdin.readline

N = int(input())
nums = list(map(int, input().split()))


dp = [0] * N
dp[0] = nums[0]
for n in range(1, N):
    dp[n] = max(nums[n], dp[n-1]+nums[n])
print(max(dp))

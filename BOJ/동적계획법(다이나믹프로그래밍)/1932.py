# 정수 삼각형(백준 1932번)

# dp

from sys import stdin

input = stdin.readline
n = int(input())
nums = [list(map(int, input().split())) for _ in range(n)]

for i in range(1, n):
    for j in range(len(nums[i])):
        if j == 0:
            nums[i][j] += nums[i-1][0]
        elif j == len(nums[i])-1:
            nums[i][j] += nums[i-1][j-1]
        else:
            nums[i][j] += max(nums[i-1][j], nums[i-1][j-1])

print(max(nums[-1]))


# 시간초과 났던 dfs

from sys import stdin, setrecursionlimit

setrecursionlimit(1000)

input = stdin.readline
n = int(input())
nums = [list(map(int, input().split())) for _ in range(n)]
max_num = 0

def dfs(depth, x, temp):
    global max_num
    temp += nums[depth][x]
    if depth == len(nums)-1:
        max_num = max(max_num, temp)
        return
    dfs(depth+1, x, temp)
    dfs(depth+1, x+1, temp)


dfs(0, 0, max_num)
print(max_num)

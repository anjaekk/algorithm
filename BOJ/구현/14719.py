# 빗물(백준 14719번)
# 입력
# 4 4 #세로길이 가로길이
# 3 0 1 4
# 출력
# 5

# 입력
# 4 8
# 3 1 2 3 4 1 1 2
# 출력
# 5

# 아이디어
# 1. 리스트의 맨 앞과 맨 뒤는 제외하고 for문을 돈다
# 2. 현재 기둥을 기준으로 앞에서 제일 큰 기둥, 뒤에서 제일 큰 기둥을 찾는다. 
# 3. 그 두개의 기둥중 작은 기둥 기준으로 현재 기둥과 비교해서 더 크면 현재기둥엔 물이 고일 수 있음.
# 4. 찾은 작은 기둥 - 현재기둥을 하여 빗물의 양을 계산한다. 

from sys import stdin

input = stdin.readline

H, W = map(int, input().split())

blocks = list(map(int, input().split()))

area = 0

for i in range(1, W-1):
    left_max = max(blocks[:i])
    right_max = max(blocks[i+1:])
    min_max = min(left_max, right_max)

    if blocks[i] < min_max:
        area += min_max - blocks[i]

print(area)

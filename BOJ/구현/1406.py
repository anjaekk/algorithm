# 에디터(백준 1406번)

# 입력 
# abcd
# 3
# P x
# L
# P y

# 출력
# abcdyx

from collections import deque
from sys import stdin

input = stdin.readline

input_str = input().strip()

N = int(input())

left = [s for s in input_str]
right = deque()
for _ in range(N):
    cmd = input().strip().split()
    if cmd[0] == 'L':
        if left:
            right.appendleft(left.pop())
    elif cmd[0] == 'D':
        if right:
            left.append(right.popleft())
    elif cmd[0] == 'B':
        if left:
            left.pop()
    else:
        left.append(cmd[1])


print("".join(left+list(right)))

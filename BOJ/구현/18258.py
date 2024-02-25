큐 2(백준 18258번)

입력
15
push 1
push 2
front
back
size
empty
pop
pop
pop
size
empty
pop
push 3
empty
front

출력
1
2
2
0
1
2
-1
0
1
-1
0
3



from sys import stdin
from collections import deque

input = stdin.readline

N = int(input())

queue = deque()

for _ in range(N):
    cmd = input().strip().split()
    if cmd[0] == 'push':
        queue.append(cmd[1])
    elif cmd[0] == 'pop':
        if queue:
            pop = queue.popleft()
            print(pop)
        else: print(-1)
    elif cmd[0] == 'size': 
        print(len(queue))
    elif cmd[0] == 'empty':
        if queue: print(0)
        else: print(1)
    elif cmd[0] == 'front':
        if queue: print(queue[0])
        else: print(-1)
    elif cmd[0] == 'back':
        if queue: print(queue[-1])
        else: print(-1)

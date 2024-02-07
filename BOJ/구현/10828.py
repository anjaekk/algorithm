# 스택(벡준 10828번)

# 입력
# 14
# push 1
# push 2
# top
# size
# empty
# pop
# pop
# pop
# size
# empty
# pop
# push 3
# empty
# top

# 출력
# 2
# 2
# 0
# 2
# 1
# -1
# 0
# 1
# -1
# 0
# 3




from sys import stdin


input = stdin.readline

N = int(input())

stack = []

for _ in range(N):
    command = (input().rstrip()).split()
    
    if command[0] == 'size':
        print(len(stack))
    elif command[0] == 'top':
        if stack:
            print(stack[-1])
        else:
            print(-1)
    elif command[0] == 'empty':
        print(int(bool(not stack)))
    elif command[0] == 'push':
        stack.append(int(command[1]))
    elif command[0] == 'pop':
        if not stack: 
            print(-1)
        else:
            print(stack.pop())

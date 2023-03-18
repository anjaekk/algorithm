# 그래프
# ABCDE(백준 13023번)

# 입력
# 5 4 # 사람의 수, 관계의 수
# 0 1
# 1 2
# 2 3
# 3 4

# 출력
# 1 # ABCDE가 존재하면 1 없으면 0

# 입력
# 6 5 # 사람의 수, 관계의 수
# 0 1
# 0 2
# 0 3
# 0 4
# 0 5

# 출력
# 0 # ABCDE가 존재하면 1 없으면 0

# A -> B -> C -> D -> E 이렇게 쭉 이어지는 친구 관계가 있는지 확인

from sys import stdin
input = stdin.readline

p, r = map(int, input().split())
relations = [[] for _ in range(p)]

visited = [0] * 2001
ans = False

for _ in range(r):
    x, y = map(int, input().split())
    relations[x].append(y)
    relations[y].append(x)


def dfs(i, depth):
    global ans
    visited[i] = 1
    if depth == 4:
        ans = True
        return
    
    for j in relations[i]:
        if not visited[j]:
            visited[j] = 1
            dfs(j, depth+1)
            visited[j] = 0

for i in range(p):
    dfs(i, 0)
    visited[i] = 0
    if ans:
        break

if ans: 
    print(1)
else: 
    print(0)

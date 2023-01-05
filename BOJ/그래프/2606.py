# 바이러스(백준 2606번)

# 입력
# 7
# 6
# 1 2
# 2 3
# 1 5
# 5 2
# 5 6
# 4 7

# 출력
# 4

computers = int(input())
connect = int(input())

data = [list(map(int, input().split())) for _ in range(connect)]

visited = [1]
node = {i+1: set() for i in range(computers)}

for x, y in data:
    node[x].add(y)
    node[y].add(x)
#node = {1: {2, 5}, 2: {1, 3, 5}, 3: {2}, 4: {7}, 5: {1, 2, 6}, 6: {5}, 7: {4}}

def dfs(start):
    for i in node[start]:
        if i not in visited:
            visited.append(i)
            dfs(i)

dfs(1)

print(len(visited)-1)

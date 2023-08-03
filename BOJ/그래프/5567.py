# 결혼식(백준 5567번)


# 입력
# 6
# 5
# 1 2
# 1 3
# 3 4
# 2 3
# 4 5

# 츨력
# 3


from sys import stdin
from collections import deque


input = stdin.readline

people = int(input())
relation = int(input())

graph = [[] for _ in range(people+1)]

for _ in range(relation):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [0] * (people+1)

queue = deque([1])
visited[1] = 1

while queue:
    x = queue.popleft()
    for i in graph[x]:
        if not visited[i]:
            visited[i] = 1
            visited[i] = visited[x] + 1 # 누적 관계 수를 visited에 저장
            queue.append(i)

answer = 0
for i in range(2, people+1):
    if 0 < visited[i] < 4:
        answer += 1
print(answer)

# BOJ1260(bfs, dfs)

from sys import stdin
from collections import deque

input = stdin.readline

n, m, v = map(int, input().split())
# graph 리스트를 초기화, n+1인 이유는 0번째 인덱스의 값은 무시할 수 있도록 하기 위해
""""
만약 n = 4 라면 
[
    [0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0]
]
"""
graph = [[0] * (n+1) for i in range(n+1)]

# 값 받기
for i in range(m):
    m1, m2 = map(int, input().split())
    # 각 노드를 맵핑하여 graph에 넣기
    """
    (1,2)(1,3)(1,4)(2,4)(3,4)를 넣었을 때
    [
        [0, 0, 0, 0, 0], 
        [0, 0, 1, 1, 1], 
        [0, 1, 0, 0, 1], 
        [0, 1, 0, 0, 1], 
        [0, 1, 1, 1, 0]]
    """
    graph[m1][m2] = graph[m2][m1] = 1

def dfs(v, visited=[]):
    visited.append(v)
    print(v, end = " ")

    for i in range(len(graph[v])):  # 여기서는 len(graph[v]) == n
        if graph[v][i] == 1 and (i not in visited):
            dfs(i, visited)

def bfs(v, visited=[]):
    visited = [v] # 확인한 노드
    queue = deque()
    queue.append(v) # 확인할 노드

    while queue:
        v = queue.popleft()
        print(v, end = " ")
        for i in range(len(graph[v])):
            if graph[v][i] == 1 and (i not in visited):
                visited.append(i)
                queue.append(i)

dfs(v)
print()
bfs(v)

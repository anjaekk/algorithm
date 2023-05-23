# 그래프
# 촌수계산(백준 2644번)

# 풀이방법
# dfs

# 고려사항
# 1. 친척관계가 전혀 없을 경우 -1 출력
# 2. 인접 리스트 구성 [[], [2, 3], [1, 7, 8, 9], [1], [5, 6], [4], [4], [2], [2], [2]]
# 3. result list생성하여 결과 저장

# 입력
# 9 # 전체 사람의 수 n
# 7 3 # 촌수를 계산해야하는 대상
# 7 # 부모 자식들 간의 관계의 개수 m
# 1 2 # 부모, 자식
# 1 3
# 2 7
# 2 8
# 2 9
# 4 5
# 4 6

# 출력
# 3


from sys import stdin

input = stdin.readline

n = int(input())
x, y = map(int, input().split())

relations = [[] for _ in range(n+1)]
r = int(input())
for _ in range(r):
    p, c = map(int, input().split())
    relations[p].append(c)
    relations[c].append(p)

result = []
def dfs(v, cnt):
    if v == y:
        result.append(cnt)
        return 
    visited[v] = True
    cnt += 1

    for i in relations[v]:
        if not visited[i]:
            dfs(i, cnt)

visited = [False] * (n+1)


dfs(x, 0)
if result:
    print(result[0])
else:
    print(-1) 

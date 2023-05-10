# 그래프
# 뱀과 사다리 게임(백준 16928번)

# 문제
# 1. 100번 칸에 도착하면 종료
# 2. 사다리나 뱀이 존재하는 칸에가면 이동
# 3. 최소 몇번 주사위를 굴려야 하는지 구하기

# 고려사항
# 1. bfs이용
# 2. 사다리와 뱀을 dictionary로 구현하여 O(1)으로 찾기
# 3. 사다리와 뱀을 만나게 되면 nx값을 변경하도록 구현했으니 다시 한 번 visitied 체크 해야함

# 입력
# 3 7 # 사다리 수, 뱀 수
# 32 62
# 42 68
# 12 98
# 95 13
# 97 25
# 93 37
# 79 27
# 75 19
# 49 47
# 67 17

# 출력
# 3

# 해설
# 5를 굴려 6으로 이동한다.
# 6을 굴려 12로 이동한다. 이 곳은 98로 이동하는 사다리가 있기 때문에, 98로 이동한다.
# 2를 굴려 100으로 이동한다.




from sys import stdin
from collections import deque

input = stdin.readline

n, m = map(int, input().split())
ladder = dict(map(int, input().split()) for _ in range(n))
snake = dict(map(int, input().split()) for _ in range(m))

queue = deque([1])

visited = [0] * 101

while queue:
    x = queue.popleft()
    if x >= 100:
        print(visited[100])
        break
    
    # 주사위
    for i in range(1, 7):
        nx = x + i
        if nx <= 100 and not visited[nx]:
            if nx in ladder:
                nx = ladder[nx]
            if nx in snake:
                nx = snake[nx]
            if not visited[nx]: # ladder과 snake로 nx값을 교체했으니 다시 한번 분기
                queue.append(nx)
                visited[nx] = visited[x] + 1

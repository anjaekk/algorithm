# A -> B(백준 16953번)
# 입력
# 2 162
# 출력
# 5

# 2곱하기 Or 오른쪽 1 추가

from collections import deque

A, B = map(int, input().split())


def solution(A, B):
    queue = deque()
    cnt = 0
    queue.append((A, cnt))

    while queue:
        num, cnt = queue.popleft()
        if num == B:
            print(cnt+1)
            return
        if num * 2 <= B:
            queue.append((num*2, cnt+1))
        if (num * 10) + 1 <= B:
            queue.append(((num*10)+1, cnt+1))
    print(-1)

solution(A, B)

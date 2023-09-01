# 체커(백준 1090번)
# N개의 체커가 엄청 큰 보드 위에 있다. i번 체커는 (xi, yi)에 있다. 
# 같은 칸에 여러 체커가 있을 수도 있다. 
# 체커를 한 번 움직이는 것은 그 체커를 위, 왼쪽, 오른쪽, 아래 중의 한 방향으로 한 칸 움직이는 것이다.
# 첫째 줄에 N이 주어진다. 
# N은 50보다 작거나 같은 자연수이다. 
# 둘째 줄부터 N개의 줄에 각 체커의 x좌표와 y좌표가 주어진다. 
# 이 값은 1,000,000보다 작거나 같은 자연수이다.
# k번째 수는 적어도 k개의 체커가 같은 칸에 모이도록 체커를 이동해야 하는 최소 횟수이다.


# ----------------------------------------------------------
# return
# 체커 1개가 모일때 체커 움직이는 최소 횟수, 체커 2개가 모일때 움직이는 최소 횟수 ... 체커 N개
# ---------------------------------------------------------- 


# 입력
# 4
# 15 14
# 15 16
# 14 15
# 16 15

# 출력
# 0 2 3 4

# 입력
# 4
# 1 1
# 2 1
# 4 1
# 9 1

# 출력
# 0 1 3 10


from sys import stdin

input = stdin.readline

N = int(input())

checkers = [list(map(int,input().split())) for _ in range(N)]
        
answers = [1_000_000 * 1_000_000] * N

for i in range(N): # 최소거리는 지정한 체커 좌표 내에 있기 때문에 그 안에서만 탐색
    for j in range(N):
        distance = []
        # 한 체커에서 다른 체커 사이 거리 확인
        for point in checkers:
            # 좌표간의 거리 계산
            d = abs(checkers[i][0] - point[0]) + abs(checkers[j][1] - point[1])
            distance.append(d)
        distance.sort()
        sum = 0

        # 체커의 각 개수만큼 같은 칸에 모이는 최소 횟수들을 구해준다. 
        for k in range(N):
            sum += distance[k]
            if sum < answers[k]:
                answers[k] = sum


print(" ".join(map(str, answers)))

# 창고 다각형(백준 2304번)

# 입력
# 7 # 기둥의 개수
# 2 4 # 왼쪽면 위치, 높이
# 11 4
# 15 8
# 4 6
# 5 3
# 8 10
# 13 6

# 출력
# 98


from sys import stdin

input = stdin.readline

N = int(input())
pillars = [list(map(int, input().split()))for _ in range(N)]
# pillars = [[2, 4], [11, 4], [15, 8], [4, 6], [5, 3], [8, 10], [13, 6]]

pillars.sort(key=lambda x: x[0])
# [[2, 4], [4, 6], [5, 3], [8, 10], [11, 4], [13, 6], [15, 8]]

# [4, 0, 6, 3, 0, 0, 10, 0, 0, 4, 0, 6, 0, 8]로 변경
pillars_height = [pillars[0][1]]
cnt = pillars[0][0]
for p in pillars[1:]:
    cnt += 1
    if p[0] > cnt:
        pillars_height += [0] * (p[0] - cnt)
        cnt = p[0]
    pillars_height.append(p[1])


# 맨 첫번째, 마지막 번째 기둥은 미리 더해놓기
# 현재 기둥 기준으로 왼쪽 가장 높은 기둥, 오른쪽 가장 높은 기둥 추출
# 둘다 현재 기둥보다 낮다면 현재 기둥만큼 더하기 
# 둘중에 더 낮은 기둥만큼 더하기

if len(pillars_height) <= 1:
    area = pillars_height[0]
else:
    area = pillars_height[0] + pillars_height[-1]
    for i in range(1, len(pillars_height)-1):
        left_max = max(pillars_height[:i])
        right_max = max(pillars_height[i:])
        min_max = min(left_max, right_max)

        if pillars_height[i] >= left_max and pillars_height[i] >= right_max:
            area += pillars_height[i]
        elif pillars_height[i] >= min_max:
            area += pillars_height[i]
        else:
            area += min_max

print(area)

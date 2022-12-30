# 부분수열의 합(백준 1182)

# 입력
# 5 0   # 정수 개수, 결과값
# -7 -3 -2 5 8

# 출력
# 1


N, S = map(int, input().split())
nums = list(map(int, input().split()))

cnt = 0

def dfs(num, sum_num):
    global cnt
    # 탐색해야하는 list를 모두 확인했을 때
    if num == N:
        return
    # sum_num에 현재 인덱스 값을 더해준다.
    sum_num += nums[num]
    # 현재까지 더한 값이 S와 같을 떄 cnt+=1
    if sum_num == S:
        cnt += 1
    # 다음 인덱스를 확인한다
    dfs(num+1, sum_num)
    # 현재 값을 제외하고 다음 인덱스르 확인한다. 
    dfs(num+1, sum_num-nums[num])
    
dfs(0,0)
print(cnt)

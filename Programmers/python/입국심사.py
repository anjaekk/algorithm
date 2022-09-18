# 이진탐색

def solution(n, times):
    answer = 0
    left = min(times)
    right = max(times) * n
    
    while left <= right:
        mid = (left + right ) // 2
        count = 0
        for time in times:
            count += mid // time
            if count >= n: break
            
        if count >= n:
            answer = mid
            right = mid - 1
        else: 
            left = mid + 1
    return answer

def solution(d, budget):
    cnt = 0
    for i in sorted(d):
        if budget  >= i:
            budget -= i
            cnt += 1
    return cnt

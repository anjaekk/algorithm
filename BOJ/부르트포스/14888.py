# 연산자 끼워넣기(백준 14888번)

# 입력
# 2         # 수의 개수
# 5 6       # 5~6
# 0 0 1 0   # 덧셈, 뺄셈, 곱셈, 나눗셈 개수

# 출력
# 30  # 결과 값 최대
# 30  # 결과 값 최소


n = int(input())
nums = list(map(int, input().split()))
plus, minus, mul, div = map(int, input().split())


results =[]

def dfs(depth, total, plus, minus, mul, div):
    depth += 1
    if depth == n:
        results.append(total)
        return
    
    if plus:
        dfs(depth, total+nums[depth], plus-1, minus, mul, div)
    if minus:
        dfs(depth, total-nums[depth], plus, minus-1, mul, div)
    if mul:
        dfs(depth, total*nums[depth], plus, minus, mul-1, div)
    if div:
        dfs(depth, int(total/nums[depth]), plus, minus, mul, div-1)



dfs(0, nums[0], plus, minus, mul, div)
print(max(results))
print(min(results))

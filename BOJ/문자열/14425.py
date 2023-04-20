# 백준 14425번(문자열 집합)

# 입력
# 5 11
# baekjoononlinejudge
# startlink
# codeplus
# sundaycoding
# codingsh
# baekjoon
# codeplus
# codeminus
# startlink
# starlink
# sundaycoding
# codingsh
# codinghs
# sondaycoding
# startrink
# icerink

# 출력
# 4

n, m = map(int, input().split())

str_set = [str(input()) for _ in range(n)]
cnt = 0
for _ in range(m):
    data = str(input())
    if data in str_set:
        cnt += 1

print(cnt)

# BOJ2003번: 수들의 합 2
import sys

N = sys.stdin.readline().rstrip().split()
n = int(N[0])  # 정수의 개수
s = int(N[1])  # 목표 합

m = list(map(int, sys.stdin.readline().rstrip().split()))  # 리스트 입력

left = right = cnt = 0

while right <= n and left <= right:
  sum_li = sum(m[left:right]) 
  if sum_li == s:
    cnt += 1
    right += 1
  elif sum_li < s:
    right += 1
  else:
    left += 1

print(cnt)

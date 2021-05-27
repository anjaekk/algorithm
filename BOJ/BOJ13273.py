# BOJ3273번: 두 수의 합
import sys

n = int(sys.stdin.readline().rstrip())  # 수열의 크기
li = sorted(list(map(int, sys.stdin.readline().rstrip().split())))  # 수열
x = int(sys.stdin.readline().rstrip())  # 기준

count = 0
left, right = 0, n-1

# 투 포인터 알고리즘 이용
while left < right:  
  num = li[left] + li[right]
  if num == x:
    count += 1
    left += 1
  elif num < x:
    left += 1
  else:
    right -= 1

print(count)

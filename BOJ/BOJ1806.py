# BOJ1806번: 부분합

# 성공 코드
import sys

n, s = map(int, sys.stdin.readline().rstrip().split())  # n수열의 길이, 목표 합 s
arr = list(map(int, sys.stdin.readline().rstrip().split()))  # 입력받은 수열

left, right = 0, 1
length = n + 1
sum_arr = arr[left] + arr[right]
if sum(arr) < s:
  print(0)
else:
  while left <= right:
    if sum_arr < s:
      right += 1
      if right >= n:
        break
      sum_arr += arr[right]

    elif sum_arr >= s:
      length = min(length, right-left+1)
      sum_arr -= arr[left]
      left += 1
  print(length)
  
  
  
  
  
# 시간초과 코드
import sys

n, s = map(int, sys.stdin.readline().rstrip().split())  # n수열의 길이, 목표 합 s
arr = list(map(int, sys.stdin.readline().rstrip().split()))  # 입력받은 수열

left, right = 0, 0
length = n + 1

while left <= right and right < n:
  sum_arr = sum(arr[left:right])  # 자른 리스트의 합
  if sum_arr >= s:
    length = min(length, right - left)
    left += 1
  else:
    right += 1

if length == n + 1:  # 예외조건: 합을 만드는 것이 불가능 하다면 0 출력
  print(0)
else:
  print(length)

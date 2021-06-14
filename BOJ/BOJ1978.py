# BOJ1978번: 소수 찾기

import sys

n = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().rstrip().split(" ")))

cnt = 0

for i in arr:
  if i > 1:
    for j in range(2, i + 1):
      if j == i:
        cnt += 1
      if i % j == 0:
        break
  else:
    continue
print(cnt) 

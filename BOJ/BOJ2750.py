# BOJ2750번: 수 정렬하기 
import sys

N = int(sys.stdin.readline().rstrip())
arr = []

for i in range(N):
  m = int(sys.stdin.readline().rstrip())
  arr.append(m)

arr = sorted(arr)

for j in arr:
  print(j)

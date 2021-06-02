# BOJ2751번: 수 정렬하기2
import sys

N = int(sys.stdin.readline().rstrip())
arr = []

for i in range(N):
  m = int(sys.stdin.readline().rstrip())
  arr.append(m)


for j in sorted(arr):
  print(j)

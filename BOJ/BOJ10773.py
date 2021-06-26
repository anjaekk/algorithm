# BOJ10773번: 제로(stack, 스택)
import sys

n = int(sys.stdin.readline().rstrip())

arr = []
for i in range(n):
  num = int(sys.stdin.readline().rstrip())
  if num != 0:
    arr.append(num)
  else:
    del arr[-1]
print(sum(arr))

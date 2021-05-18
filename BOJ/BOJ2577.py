import sys

A = int(sys.stdin.readline().rstrip())
B = int(sys.stdin.readline().rstrip())
C = int(sys.stdin.readline().rstrip())

mul = list(str(A * B * C))

for i in range(10):
  count = 0
  for j in mul:
    if int(j) == i:
      count += 1
  print(count)

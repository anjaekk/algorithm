import sys

N = num = int(sys.stdin.readline().rstrip())

count = 0
while True:
  ten = N // 10
  one = N % 10
  add = str(ten + one)
  N = int(str(one) + add[-1])
  count += 1
  if N == num:
    break
print(count)

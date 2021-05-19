import sys

remain_li =[]

for i in range(10):
  N = int(sys.stdin.readline().rstrip())
  remainder = N % 42
  if remainder not in remain_li:
    remain_li.append(remainder)

print(len(remain_li))

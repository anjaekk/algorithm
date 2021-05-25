# BOJ11720번: 숫자의 합
import sys

N = int(sys.stdin.readline().rstrip())
numbers = list(map(str, sys.stdin.readline().rstrip()))

result = 0
for i in numbers:
  result += int(i)
print(result)

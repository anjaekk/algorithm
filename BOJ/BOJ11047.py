# BOJ11047번: 동전 0
from sys import stdin

n, k = map(int, stdin.readline().rstrip().split(" "))
nlist = []
answer = 0

for i in range(n):
  m = int(stdin.readline().rstrip())
  nlist.append(m)

nlist.sort(reverse=True)

for i in nlist:
  if k >= i:
    answer += k // i
    k %= i
  if k == 0:
    break
print(answer)

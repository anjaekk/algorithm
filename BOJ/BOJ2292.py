# BOJ2292번: 벌집
import sys

N = int(sys.stdin.readline().rstrip())

comb = 1 
cnt = 1

while N > comb :
  comb = comb + (6 * cnt)
  cnt += 1
print(cnt)

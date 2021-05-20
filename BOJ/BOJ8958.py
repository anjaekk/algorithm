import sys

N = int(sys.stdin.readline().rstrip())


for i in range(N):
  case = sys.stdin.readline().rstrip()
  score = 0
  cnt = 0
  for j in case:
    if j == "O":
      cnt += 1
      score += cnt
    else:
      cnt = 0
  print(score)

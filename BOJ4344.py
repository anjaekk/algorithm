import sys

C = int(sys.stdin.readline().rstrip())

for i in range(C):
  score = list(map(int, sys.stdin.readline().rstrip().split()))
  student = score.pop(0)
  avg = sum(score) / len(score)
  high = [j for j in score if j > avg]
  print("{:.3f}%".format(round((len(high) / student * 100), 3)))

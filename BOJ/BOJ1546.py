import sys

# 갯수 입력받기
amount = int(sys.stdin.readline().rstrip())
# 시험점수 입력받기
score = list(map(int, sys.stdin.readline().rstrip().split(" ")))

# 점수 최댓값
best = max(score)

for i in range(amount):
  score[i] = (score[i] / best * 100)
  
print("%.2f" %(sum(score)/ len(score)))

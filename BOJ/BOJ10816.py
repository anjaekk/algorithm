# BOJ10816번: 숫자카드2
from sys import stdin

n = stdin.readline()
arr = list(map(int, stdin.readline().rstrip().split()))
m = stdin.readline()
search = list(map(int, stdin.readline().rstrip().split()))

dic = dict()

for i in arr:
  try :
    dic[i] += 1
  except:
    dic[i] = 1
    
for j in search:
  try:
    print(dic[j], end = " ")
  except:
    print(0, end=" ")

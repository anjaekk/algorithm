# BOJ1427번: 소트인사이드
import sys

N = sys.stdin.readline().rstrip()
li = []

for i in range(len(N)):
  li.append(N[i])
li = sorted(li, reverse=True)
print("".join(li))  

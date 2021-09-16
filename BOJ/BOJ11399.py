# BOJ11399번: ATM
from sys import stdin

n = int(stdin.readline().rstrip())
t = list(map(int, stdin.readline().rstrip().split(" ")))
save_time = 0 # 누계
total_time = 0 # 총계

for i in sorted(t):
  save_time += i
  total_time += save_time

print(total_time)

# BOJ2217번: 로프
from sys import stdin

n = int(stdin.readline().rstrip())
rope_list = []
rope = 0

for i in range(n):
  r = int(stdin.readline().rstrip())
  rope_list.append(r)

rope_list.sort()

for j in range(len(rope_list)):
  temp = rope_list[j] * (n-j)
  if temp > rope:
    rope = temp

print(rope)

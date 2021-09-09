# BOJ1026번: 보물
from sys import stdin

n = int(stdin.readline().rstrip())
a = list(map(int, stdin.readline().rstrip().split(" ")))
b = list(map(int, stdin.readline().rstrip().split(" ")))

a.sort()
b.sort(reverse = True)

answer = sum([x*y for x,y in zip(a, b)])
print(answer)

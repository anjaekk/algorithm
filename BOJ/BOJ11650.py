# BOJ11650번: 보물

from sys import stdin

input = stdin.readline

n = int(input())
m = [list(map(int, input().split())) for i in range(n)]

m.sort(key = lambda x : (x[0], x[1]))
for x, y in m:
    print(x, y)

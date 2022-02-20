# BOJ1931번: 회의실 배정
from sys import stdin

n = int(stdin.readline().rstrip())
nlist = []

nlist = [list(map(int, stdin.readline().rstrip().split())) for i in range(n)]

nlist.sort(key = lambda x: (x[1], x[0]))
cnt = 1
end = nlist[0][1]
for i in range(1, n):
    if nlist[i][0] >= end:
        cnt += 1
        end = nlist[i][1]
print(cnt)

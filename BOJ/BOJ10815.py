# BOJ10815번: 숫자 카드
from sys import stdin

n = int(stdin.readline().rstrip())
nlist = list(map(int, stdin.readline().rstrip().split(" ")))
m = int(stdin.readline().rstrip())
mlist = list(map(int, stdin.readline().rstrip().split(" ")))

nlist.sort()

for i in mlist:
  start = 0
  end = len(nlist) - 1
  while start <= end:
    mid = (start+end) // 2
    if nlist[mid] == i:
      print(1, end=" ")
      break
    elif nlist[mid] < i:
      start = mid+1
    elif nlist[mid] > i:
      end = mid-1
  if start > end:
    print(0, end=" ")

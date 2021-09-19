# BOJ1920번: 수 찾기(이진탐색)
import sys

def binary(target, arr, start, end):
  if start > end:
    return 0
  
  mid = (start + end) // 2

  if target == arr[mid]:
    return 1
  elif target < arr[mid]:
    return binary(target, arr, start, mid-1)
  else:
    return binary(target, arr, mid+1, end)


n = int(sys.stdin.readline().rstrip())
arr = sorted(list(map(int, sys.stdin.readline().rstrip().split(" "))))
m = int(sys.stdin.readline().rstrip())
search = list(map(int, sys.stdin.readline().rstrip().split(" ")))

for target in search:
  start = 0
  end = len(arr)-1
  print(binary(target, arr, start, end))

  
  
  #=========================================================================
  
  for i in mlist:
  start = 0
  end = len(nlist)-1
  while start <= end:
    mid = (start+end) // 2
    if nlist[mid] == i:
      print(1)
      break
    elif nlist[mid] > i:
      end = mid-1
    elif nlist[mid] < i:
      start = mid+1
  if start > end:
    print(0)

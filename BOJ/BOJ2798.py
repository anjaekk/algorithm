# BOJ2798번: 블랙잭
import sys

input_data = sys.stdin.readline().rstrip().split(" ")
arr = sorted(list(map(int, sys.stdin.readline().rstrip().split(" "))))
n = int(input_data[0])
goal = int(input_data[1])

result = 0
length = len(arr)

for i in range(length):
  for j in range(i+1, length):
    for k in range(j+1, length):
      add = arr[i] + arr[j] + arr[k]
      if add <= goal:
        result = max(add, result)

print(result)

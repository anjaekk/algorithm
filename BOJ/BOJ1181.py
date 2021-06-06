# BOJ1181번: 단어정렬
import sys

n = int(sys.stdin.readline().rstrip())

arr = []

for i in range(n):
  word = sys.stdin.readline().rstrip()
  if (len(word), word) not in arr:   # 중복제거
    arr.append((len(word), word))

for j, k in sorted(arr):
  print(k)

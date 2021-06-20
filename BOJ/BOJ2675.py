# BOJ2675번: 문자열 반복
import sys

n = int(sys.stdin.readline().rstrip())

for i in range(n):
  input_data = sys.stdin.readline().rstrip().split(" ")
  num = int(input_data[0])
  word = input_data[1]
  arr = [j * num for j in word]
  print("".join(arr))

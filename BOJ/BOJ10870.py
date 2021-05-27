# BOJ10870번: 피보나치 수 5
import sys

N = int(sys.stdin.readline().rstrip())

def fibo(N):
  if N < 2:
    return N
  return fibo(N - 1) + fibo(N - 2)

print(fibo(N))

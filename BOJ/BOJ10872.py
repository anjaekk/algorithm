# BOJ10872번: 팩토리얼
import sys

N = int(sys.stdin.readline().rstrip())

def factorial(N):
    if N == 0 or N == 1:
        return 1
    return factorial(N - 1) * N
  
print(factorial(N))

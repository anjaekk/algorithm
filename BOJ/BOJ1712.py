# BOJ1712번: 손익분기점
import sys

fixed_cost, variable_cost, price = list(map(int, sys.stdin.readline().split()))

if price - variable_cost <= 0:
  print(-1)
else:
  BEP = fixed_cost / (price - variable_cost)
  print(int(BEP +1))

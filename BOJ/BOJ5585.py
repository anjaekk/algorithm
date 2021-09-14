# BOJ5585번: 거스름 돈(그리디)
from sys import stdin

n = int(stdin.readline().rstrip())
amount = 1000 - n
change = 0

if amount >= 500:
  change += amount//500
  amount %= 500
if amount >= 100:
  change += amount//100
  amount %= 100
if amount >= 50:
  change += amount//50
  amount %= 50
if amount >= 10:
  change += amount//10
  amount %= 10
if amount >= 5:
  change += amount//5
  amount %= 5
if amount >= 1:
  change += amount//1

print(change)

# BOJ10809번: 알파벳 찾기
import sys

N = list(map(str, sys.stdin.readline().rstrip()))
li = []

for i in range(97, 123):
  i = chr(i)  # 아스키코드를 문자로 변환
  if i not in N:
    li.append(-1)  
  else: 
    li.append(N.index(i))

print(' '.join(str(j) for j in li))  # 숫자 리스트를 공백으로 띄어서 출력

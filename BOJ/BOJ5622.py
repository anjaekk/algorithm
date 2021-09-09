
data = str(input())
dial = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']

cnt = 0

for i in data:
  for j in range(len(dial)):
    if i in dial[j]:
      cnt += (j+3)

print(cnt)

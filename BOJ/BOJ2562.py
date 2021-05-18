import sys

li = []
for i in range(1, 10):
 num = int(sys.stdin.readline().rstrip())
 li.append(num)

print(max(li))
print(li.index(max(li))+1)

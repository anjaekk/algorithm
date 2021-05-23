# BOJ4673번: 셀프넘버

self_num = set(range(1, 10001))
del_num = set()

for i in range(1, 10001):
  for j in str(i):
    i += int(j)
  del_num.add(i)

self_num = self_num - del_num

for i in sorted(self_num):
  print(i)

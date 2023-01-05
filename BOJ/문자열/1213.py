#팰린드롬 만들기(백준 1213번)

#입력
#AABB

#출력
#ABBA

from collections import Counter

data = list(map(str, input()))
sorted_data = sorted(data)

single = 0
center = ""
result = []

counter = Counter(sorted_data)
for k, v in counter.items():
    if v % 2 != 0:
        single += 1
        v -= 1
        center = k
        if v > 0:
            result.append(k*(v//2))
    else:
        result.append(k*(v//2))
        
if single > 1:
    print("I'm Sorry Hansoo")
else:
    print("".join(result) + center + "".join(sorted(result, reverse=True)))
        

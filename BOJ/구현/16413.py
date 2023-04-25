# 단어 뒤집기2(백준 16413번)
# 입력
# <ab cd>ef gh<ij kl>

# 출력
# <ab cd>fe hg<ij kl>


string = str(input())

result = ""
temp = []
in_bracket = False
for s in string:
    if s == "<":
        if temp:
            result += "".join(temp[::-1])
            temp = []
        in_bracket = True
        result += s
    elif s == ">":
        in_bracket = False
        result += s
    elif s == " " and in_bracket:
        result += s
    elif s == " ":
        if temp:
            result += "".join(temp[::-1])
            temp = []
        result += s
    elif in_bracket:
        result += s
    else:
        temp.append(s)
if temp:
    result += "".join(temp[::-1])
print(result)

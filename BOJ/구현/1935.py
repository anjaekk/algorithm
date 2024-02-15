# 후위 표기식2(백준 1935번)

# 입력
# 5
# ABC*+DE/-
# 1
# 2
# 3
# 4
# 5

# 출력
# 6.20


from sys import stdin

input = stdin.readline

N = int(input())
string = str(input().strip())
str_list = [s for s in string]

num_set = {}
stack = []
for i in range(len(str_list)):
    if str_list[i] in ['+', '-', '*', '/']:
        first = stack.pop()
        second = stack.pop()
        if str_list[i] == '+':
            tmp_result = second + first
        elif str_list[i] == '-':
            tmp_result = second - first
        elif str_list[i] == '*':
            tmp_result = second * first
        elif str_list[i] == '/':
            tmp_result = second / first
        stack.append(tmp_result)
    else:
        if not str_list[i] in num_set.keys():
            num_set[str_list[i]] = int(input())
        stack.append(num_set[str_list[i]])


print("{:.2f}".format(stack[0]))

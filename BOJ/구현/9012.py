# 괄호(백준 9012번)

# 입력
# 6
# (())())
# (((()())()
# (()())((()))
# ((()()(()))(((())))()
# ()()()()(()()())()
# (()((())()(

# 출력
# NO
# NO
# YES
# NO
# YES
# NO



from sys import stdin

input = stdin.readline


N = int(input())

def check_bracket(N):
    brackets = input().strip()

    check = []
    for i in range(len(brackets)):
        if brackets[i] == '(':
            check.append(brackets[i])
        else:
            if not check:
                return 'NO'
            check.pop()
    if check:
        return 'NO'
    return 'YES'

for _ in range(N):
    print(check_bracket(N))

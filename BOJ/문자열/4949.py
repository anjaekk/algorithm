# 균형잡힌 세상(백준 4949번)

# 입력
# So when I die (the [first] I will see in (heaven) is a score list).
# [ first in ] ( first out ).
# Half Moon tonight (At least it is better than no Moon at all].
# A rope may form )( a trail in a maze.
# Help( I[m being held prisoner in a fortune cookie factory)].
# ([ (([( [ ] ) ( ) (( ))] )) ]).
#  .
# .

# 출력
# yes
# yes
# no
# no
# no
# yes
# yes

from sys import stdin

input = stdin.readline

brackets = {"]":"[", ")":"("}

while True:
    string = input().rstrip()
    if string == ".":
        break

    stack = []
    answer = "yes"
    for c in string:
        if c in brackets.values():
            stack.append(c)
        elif c in brackets:
            if not stack:
                answer = "no"
                break
            else:
                last = stack.pop()
                if last != brackets[c]:
                    answer = "no"
                    break
    if stack:
        answer = "no"
    print(answer)
        
        

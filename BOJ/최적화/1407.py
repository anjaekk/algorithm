# 2로 몇 번 나눠질까(백준 1407번)
# 두 자연수 A, B(A≤B)가 주어지면, A 이상 B 이하의 모든 자연수에 대해서, 
# 그 자연수의 모든 약수 중 2의 거듭제곱 꼴이면서 가장 큰 약수들의 총 합을 구하는 프로그램을 작성하시오. 
# 즉 아래와 같은 수식의 값을 구해야 한다.

# f(A) + f(A+1) + ... + f(B-1) + f(B)


# 입력-1
# 176 177
# 출력-1
# 17

# 입력-2
# 5 9
# 출력-2
# 13

# 입력-3
# 25 28
# 출력-3
# 8

# 아이디어: 8의 약수 중 2의 거듭제곱 꼴이면서 가장 큰 약수들의 총합
# answer += 1 * 8 (모든 수는 1로 나누어 떨어지니)
# answer += (8 // 2) * 1 (2로 나눈 값)
# answer += (8 // 4) * 2 (4로 나눈 값)
# answer += (8 // 8) * 4 (8로 나눈 값)
# 총합 = 8 + 4 + 4 + 4 = 20

from sys import stdin

input = stdin.readline

A, B = map(int, input().split())

def square_of_two(num):
    square = 2
    count = num
    while True:
        if square > num:
            break
        count += (num // square) * square//2
        square *= 2
    return count

print(square_of_two(B) - square_of_two(A-1))

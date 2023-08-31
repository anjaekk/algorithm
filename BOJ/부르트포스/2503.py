# 숫자야구(백준 2503번)
# 정답가능성이 있는 답의 총 개수

# 입력
# 4
# 123 1 1 # 1스트라이크 1볼
# 356 1 0
# 327 2 0
# 489 0 1

# 출력
# 2  # 324와 328

from sys import stdin

input = stdin.readline

T = int(input())

guesses = [list(map(int, input().split())) for _ in range(T)]

answer = 0
for a in range(1, 10): # 100의 자리수
    for b in range(1, 10): # 10의 자리수
        for c in range(1, 10): # 1의 자리수
            
            if any([a == b, b == c, c == a]):
                continue
            
            hint_correct = 0
            for guess in guesses:
                num = guess[0]
                strike = guess[1]
                ball = guess[2]
                
                if strike == 3:
                    print(1)
                    exit()
                
                strike_cnt = 0
                ball_cnt = 0
                if a == num // 100:
                    strike_cnt += 1
                elif str(a) in str(num):
                    ball_cnt += 1

                if b == num // 10 % 10:
                    strike_cnt += 1
                elif str(b) in str(num):    
                    ball_cnt += 1

                if c == num % 10:
                    strike_cnt += 1
                elif str(c) in str(num):
                    ball_cnt += 1
    
                if strike_cnt == strike and ball_cnt == ball:
                    hint_correct += 1

            if hint_correct == T:
                answer += 1
            
print(answer)         

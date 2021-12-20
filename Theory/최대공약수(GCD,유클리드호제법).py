# 최대공약수 계산(GCD, 유클리드 호제법)
# 두 자연수 A, B에 대하여(A>B) A를 B로 나눈 나머지가 R일 때
# A와 B의 최대공약수 = B와 R의 최대공약수

# GCD(192, 162)
# 192, 162 => 30 / 162, 30 => 12 / 30, 12 => 6 / 12, 6
# GCD(192, 162) = GCD(12, 6)

def gcd(a, b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)

print(gcd(192, 162))

# codility

def solution(N):
    binary = str(bin(N)[2:])
    return 0 if "1" not in binary[1:] else len(max(binary.split("1")))

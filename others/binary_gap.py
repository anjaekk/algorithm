# codility

def solution(N):
    binary = bin(N)[2:]
    if "1" not in binary[1:]:
        return 0
    last_one = 0
    for i in range(len(binary)-1, 0, -1):
        if binary[i] == "1":
            last_one = i
            break
    return len(max(binary[:last_one].split("1")))

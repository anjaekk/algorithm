def solution(s):
    list_s = s.split()
    int_s = [int(i) for i in list_s]
    int_s.sort()
    answer = f'{str(int_s[0])} {str(int_s[-1])}'
    return answer
  
  # s = list(map(int,s.split()))

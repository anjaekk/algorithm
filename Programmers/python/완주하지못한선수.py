# 완주하지 못한 선수(프로그래머스)

# 입력
participant = ["mislav", "stanko", "mislav", "ana"]
completion = ["stanko", "ana", "mislav"]
# 출력
# "mislav"

from collections import Counter
def solution(participant, completion):
    cnt_participant = Counter(participant)
    for s in completion:
        cnt_participant[s] -= 1
        
    for k, v in cnt_participant.items():
        if v == 1:
            return k

print(solution(participant, completion))



# 다른 사람의 풀이
import collections

def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]

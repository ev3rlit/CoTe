# 참여자를 기준으로 set을 구성하여 검색
# completion을 순회하면서 완주하지 못한 선수를 찾은 경우 반환

def solution(participant, completion):

    answer = ""

    participant_count = {}
    for p in participant:
        if p in participant_count:
            participant_count[p] += 1
        else:
            participant_count[p] = 1

    for c in completion:
        if c in participant_count:
            participant_count[c] -= 1

    for p, count in participant_count.items():
        if count > 0:
            answer = p
            break

    return answer
    
# 실패율 계산하기
# 
# 해당 스테이지의 실패율 = 스테이지 도달 했으나, 클리어하지 못한 플레이어의 수 / 스테이지 도달한 플레이어의 수
# 실패율 내림차순 반환


# 1. 값 초기화
# - challenging = defaultdict(int)
# - failures = [(스테이지, 실패율)]
# - 직전_사용자수 = len(stages)
# 1 부터 N 까지 진행하면서 실패율 계산
# - 해당 스테이지 실패율 =  해당 스테이지 도전자수 / 직전_사용자수
# - 직전_사용자수 -= 해당 스테이지 도전자수

from collections import defaultdict

def solution(N, stages):
    
    challengers = defaultdict(int)
    for stage in stages:
        challengers[stage] += 1
        
    users = len(stages)
    failures = []
    
    for stage in range(1, N+1):
        if users <= 0 :
            failures.append((stage, 0))
            continue
        
        failure = challengers[stage] / users
        users -= challengers[stage]
        failures.append((stage, failure))
        
    failures.sort(key=lambda x : (-x[1], x[0]))
    print([x[0] for x in failures])
    return [x[0] for x in failures]
        
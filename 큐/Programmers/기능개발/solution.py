
# 각 진행도마다 배포까지 남은 일 수를 계산
# 특정 기능의 배포 일수가  다음 기능의 배포일수 보다 크면    특정 기능 배포 일수에 같이 배포

import math

def solution(progresses, speeds):

    answer = []
    n = len(progresses)

    # 각 기능마다 남은 일수를 계산
    daysleft = [math.ceil( ( 100-progress) / speed ) for (progress, speed) in zip(progresses, speeds)]

    count = 0
    max_day = daysleft[0]

    for left in daysleft:

        # 현재 배포될 작업이 앞선 기능 보다 남은 일 수 가 적으면 같이 배포
        if left <= max_day:
            count += 1
        # 그렇지 않으면, 새로운 배포 일정에 포함됨
        else:
            answer.append(count)
            count = 1
            max_day = left
    
    answer.append(count)
    return answer
    
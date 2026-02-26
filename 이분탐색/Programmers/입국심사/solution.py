# fanout 느낌인데 최솟값이 필요함
# 즉,  n번을 시도하면서 각 시도마다 특정 심사원에 배정될때 발생되는 소요시간의 경우 의수
# 모든 경우의 수 중 최솟값이어야함

def solution_old(n, times):
    # 
    # 두 심사원의 남은 시간 0, 0
    # 모든 사람이 0명이 될때 까지 시도
    # 최선의 선택으로 시도하면 최솟값이 되버리나?
    
    # 7 (7, 0) -> 10 (7,10) -> 7 (14, 10) -> 
    # 10 -> 7 -> 

    # 1분 단위로 시도 가능한걸 봐야하나?
    
    return None


# 해당 문제의 입력은 10억으로 엄청 크므로 단순한 반복으로는 해결 불가
# 이분 탐색으로 접근이 필요하다.
# 해당 문제는 문제 그대로 이해하면 어렵고, 반대로 생각해야 한다.
# 특정 시간안에 n명을 심사할 수 있는가? 를 판단하는 문제로 바꿔야 한다.
# 특정 시간 mid를 잡고, mid 시간안에 심사할 수 있는 사람 수를 계산
# 그 사람이 n명 이상이면 시간을 줄여보고, n명 이하이면 시간을 늘려본다.
def solution(n, times):

    left = 1
    right = max(times) * n
    answer = right

    while left <= right:
        mid = (left + right) // 2

        # mid 시간안에 심사할 수 있는 사람 수 계산
        total = sum(mid // t for t in times)

        if total >= n:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1

    return answer
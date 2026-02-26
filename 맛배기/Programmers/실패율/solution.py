# 입력으로는 각 유저별 도달한 스테이지를 배열로 제공함.
# 클리어란  해당 스테이지 보다 높은 수를 클리어로 인정함
# 실패율이란 특정 스테이지를 기준으로 머물러있는 이용자를 의미함
# 퍼널로그? 개념 처럼 봐도되지 않을까 싶음

# 누적유저(x) = 1 ~ x 까지 실패한 유적들의 누적합
# 실패율(n) = N번 도달 유저 수 /  (전체 유저수 - 누적유저(N-1))

# 1 ~ N 까지 순회
# 특정 스테이지 x 명 유저수와  잔존 유저수를 가지고 실패율을 계산
# 해당 스테이지의 실패율 기록

# 출력 정렬 순위
# 1. 실패율을 내림차순
# 2. 스테이지 오름차순

def solution(N, stages):

    failures = []
    lookup = {}
    accumulated = 0
    total = len(stages)

    # 특정 스테이지별 유저 분포 (N+1은 모든 스테이지 클리어한 유저)
    for s in stages:
        if s <= N:
            lookup[s] = lookup.get(s, 0) + 1

    # 1 ~ N 까지 순회
    for i in range(1, N+1):
        # 해당 스테이지 유저 수 확인
        users = lookup.get(i, 0)
        remains = total - accumulated
        accumulated += users

        # 실패율 기록 (0으로 나누는 경우 실패율 0 처리)
        if remains == 0:
            failures.append((i, 0))
        else:
            failures.append((i, users/remains))

    # 실패율 정렬 (실패율 내림차순, 스테이지 오름차순)
    failures.sort(key=lambda x : (-x[1], x[0]))

    # 스테이지 번호만 반환
    return [stage for stage, _ in failures]
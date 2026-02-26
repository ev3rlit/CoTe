# 특정 유저는 다른 유저를 신고할 수 있고, 신고를 여러번 해도 1번으로 기록됨
# 특정 유저가 K번 이상 다른 유저들로 부터 신고가 누적될경우 정지 및  신고한 유저들에게 사실을 알림

# 모든 신고 내역이 집계된 결과를 토대로  정지 처리를 하려고함.

# 핵심은 유저 id_list를 기준으로 각 유저가 신고한 유저들이 정지된 유저 수를 반환
# 신고 받은 유저를 중복없이 기록되게 하여, k 정지 횟수를 초과한 유저들을 대상으로 기록후
# 신고한 유저들 중  정지당한 유저 수를 카운팅

# 특정 유저가 신고한 리스트
# 특정 유저가 신고 받은 리스트
# 정지당한 유저 정보

# 
# 총 신고자 report 길이에  조회를 하는 M

from collections import defaultdict

def solution(id_list, report, k):

    # report를 기준으로   신고한 유저, 신고 받은 유저 리스트를 기록
    reporters = defaultdict(set)
    reportees = defaultdict(set)

    for event in report:
        reporter, reportee = event.split(" ")

        reporters[reporter].add(reportee)
        reportees[reportee].add(reporter)

    # 정지 대상자 확인
    blocks = set()

    for reportee, users in reportees.items():
        if len(users) >= k:
            blocks.add(reportee)

    # id_list를 순회하면서  신고자의 대상자 리스트 중 속하면 카운팅
    result = []
    for id in id_list:
        # 교집합으로 카운팅
        count = len(blocks & reporters[id])
        result.append(count)

    return result
    
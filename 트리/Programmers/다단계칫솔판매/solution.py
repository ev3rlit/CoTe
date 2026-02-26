#    N*10^-1, N*10^-2
# 10% 계산시 소수점 부분을 절삭
#  N // (10**x) 
# H = 부모 높이(단계) 차이
# 특정 자식 A가  특정 부모 B에게 지급하는 이익금
# 자식 A의 매출액 X이고 높이 차이가 H라면  Y = X // (10**H)
# 자식 A의 이익은  X - Y,   부모 B의 이익은 Y
# 여기서 1원 미만 절삭금은  자식이 가져감

# seller들이 판매한 총 이익금을 누적하여  enroll 순서대로 각 조직원들의 총 이익금 표시

from collections import defaultdict

def solution(enroll, referral, seller, amount):

    # enroll -> referral을 통해서 추천인을 알 수 있음
    # referral이 - 이면 초기 조직원


    # 특정 조직원이 이익을 발생하면  해당 조직원에 90%을 주고 나머지 10%를  추천인에게 지급
    # 추천인이 '-'이 될때 까지 반복

    parents = {child : parent for (child, parent) in zip(enroll, referral)}
    incomes = defaultdict(int)

    # 판매원과 판매 수량을 순회하면서  가격 누적
    for (person, count) in zip(seller, amount):

        # 해당 조직원의 이익금 우선 누적
        income = count * 100 
        current = person

        # 부모가 '-'가 될 때 까지 순회
        # 이익금이 0원 경우에는 추천인에게 전달하지 않음
        while current != '-' and income > 0:
            incomes[current] +=  income - income // 10
            current = parents[current]
            income //= 10


    result = []
    for person in enroll:
        result.append(incomes.get(person, 0))

    return result
    
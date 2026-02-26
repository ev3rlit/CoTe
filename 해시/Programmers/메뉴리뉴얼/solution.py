from collections import defaultdict
from itertools import combinations

def solution(orders, course):

    # 각 코스별 단품 메뉴가 있는데, 
    # 단품 메뉴 조합이 2개번 이상 나오는 것 중,  코스 단품 메뉴 갯수를 만족하는 것들을 집계
    # 집계된 결과에서  정렬 조건에 따라 반환 

    # 핵심은  코스 단퓸 메뉴 '갯수'에 대응되는  메뉴 조합을 가지고  부분 조합이 가능한 코스가 2번 이상 나오면  해당 코스는 
    # 코스 요리 메뉴 후보임


    # 각 주문건을 순회하면서 길이별로 그룹핑
    # 코스를 순회하면서 길이에 대응되는 메뉴가    다른 메뉴의 부분집합으로 있으면 카운팅
    # 카운팅이 2개 이상인 메뉴는 당첨

    # 코스 요리 메뉴 후보를 정렬

    # 부분집합을 판단하는 핵심은  모든 주문건들을 set으로 관리하면 부분집합으로 관리하기 용이할듯함

    # 내가 문제를 잘못이해하고 있었다. 이 문제는 각 주문건 문자열 집합에서 조합 가능한 코스 요리 갯수 만큼 만들어서 빈도수가 2개 이상인 것들을 추려서 알파벳 오름차순 정렬하여 반환하는 문제였다.
    # 만약 최빈도가 여러개 라면 다 포함하기. 즉, 최빈도가 여러개라면 모두 포함하고 알파벳 오름차순 정렬하여 반환하는 문제였다.

    answer = []

    for c in course:
        menus = defaultdict(int)

        for order in orders:
            for case in combinations(sorted(order), c):
                menus[case] += 1
        
        if len(menus) <= 0:
            continue
    
        max_value = max(menus.values())
        if max_value < 2:
            continue

        for menu, count in menus.items():
            if count == max_value:
                answer.append("".join(menu))
            
    return sorted(answer)
    
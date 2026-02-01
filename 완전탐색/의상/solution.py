# 목표 서로 다른 옷의 조합의 수가 필요함.
# 각 종료별 의상은 최소 한개 입음
# 같은 종류의 의상은 사용하지 않음

# 의상 이름과 종류를 제공함
# 이문제는  의상 종류 별로 0, 1개 사용할때 조합의 갯수가 필요한 문제임.

# 수학적 조합을 이용한 풀이 방법이 가능
# 1. 의상 종류별로 2가지 이가 있는 경우  1번을 입기, 2번을 입기, 안입기 이므로 총 3가지 경우가 가능
# 2. 각 종류별 의상의 갯수를 확인하여  곱하면 전체 가지수를 계산
# 3. 전체 가지수중 아무것도 안입는 경우를 제외하면 정답

from collections import defaultdict

def solution(clothes):

    category_count = defaultdict(int)
    for (name, category) in clothes:
        category_count[category] += 1
            
    result = 1
    for count in category_count.values():
        result *= (count + 1)
            
    # 아무것도 안입는 경우 제외
    return result - 1
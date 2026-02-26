

def solution(want, number, discount):
    result = 0

    want_dict = dict(zip(want, number))

    for i in range(len(discount) - 9):

        # 각 일자별 할인 상품의 수를 카운팅해서 want_dict와 동일하면
        # 10일 동안 모든 할인 상품을 구매가능함

        discount_dict = {}
        for j in range(i, i+10):
            food = discount[j]
            discount_dict[food] = discount_dict.get(food, 0) + 1
        
        # 모두 동일하면 조건 만족
        if want_dict == discount_dict:
            result += 1


    return result
    
# 슬라이딩 윈도우를 이용한 버전
def solutionv2(want, number, discount):
    result = 0

    want_dict = dict(zip(want,number))

    # 첫 인덱스 할인 상품 생서
    discount_dict = {}
    for i in range(10):
        discount_dict[discount[i]] = discount_dict.get(discount[i], 0 )+ 1
    
    # 일치 여부 확인
    if want_dict == discount_dict:
        result += 1

    # 슬라이딩 윈도우
    for i in range(1, len(discount) - 9):
        # 왼쪽 하나 제거
        old = discount[i-1]
        discount_dict[old] -= 1
        if discount_dict[old] == 0:
            del discount_dict[old]

        # 오른쪽 하나 추가
        new = discount[i+9]
        discount_dict[new] = discount_dict.get(new, 0) + 1
    
        if want_dict == discount_dict:
            result += 1

    return result


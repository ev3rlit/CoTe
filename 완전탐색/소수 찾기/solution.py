from itertools import permutations

def is_prime(number):
    # 0과 1은 소수가 아니므로 제외
    if number < 2:
        return False
    
    for i in range(2, int(number**0.5)+1):
        if number % i == 0:
            return False
    return True

def concat_number(numbers):
    return int(''.join(map(str, numbers)))

def concat_numberv2(numbers):
    result = 0
    for number in numbers:
        result = result * 10 + number
    return result

# 1. 숫자 배열 변환
# 2. 순열로 종이 조각의 갯수만큼 경우의 수 찾기
# 3. 모든 경우의수 에서 중복제거
# 4. 경우의 수 마다 소수인지 확인

def solution(numbers):
    
    # 숫자 배열 변환
    numbers = list(map(int, list(numbers)))
    
    # 순열로 종이 조각의 갯수만큼 찾기    
    candidates = set()
    for i in range(1, len(numbers)+1):
        # 순열로 가능한 가능한 경우의 수 생성
        # 모든 경우의수 에서 중복제거
        candidates.update(map(concat_number, permutations(numbers, i)))
        
    
    answer = 0
    # 경우의 수 마다 소수인지 확인
    for value in candidates:
        if is_prime(value):
            answer += 1
    
    return answer
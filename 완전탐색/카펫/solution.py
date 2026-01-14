# 1. 전체 넓이 = 갈색 격자 + 노란색 격자
# 2. 세로 길이 후보 탐색, 세로 길이 최소 3부터, 넓이의 제곱근까지 가능
# 3. height가 total로 나누어 떨어지는지 확인
# 4. 가로가 세로보다 더 큰지 확인
# 5. 노란색 조건을 만족하는지 확인 (width - 2) * (height-2) == yellow
# 6. 조건 만족시 반환
# 7. 없으면 빈배열 반환 (예외 케이스는 없음)

def solution(brown, yellow):
    total = brown + yellow
    
    for height in range(3, int(total**0.5)+1, 1):
        if total % height != 0:
            continue
        
        width = int(total / height)
        if not width >= height:
            continue
        
        if (width-2) * (height-2) == yellow:
            return [width, height]
    
    return []
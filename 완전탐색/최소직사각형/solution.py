# 명함은 최대 1만개
# 문제의 핵심은  가로 세로를 최소로 보관 가능한 크기를 찾는것

# 가로 세로 중  가로가 가장 긴것을 기준으로 찾는것
# 가로, 세로중  가장 긴것을 가로로 사용, 그렇지 않은것을 세로로 사용
# max(size) -> 가로  min(size) -> 세로
# 각 가로와 세로 배열의  최대값이  최소한으로 사용 가능한 면적

def solution(sizes):
    return max((max(size) for size in sizes)) * max((min(size) for size in sizes))
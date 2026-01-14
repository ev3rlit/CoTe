# 입력  가로 2 세로 8 
# 던전의 입장 순서가 중요함
# 던전의 피로도 중요함
# 최대 횟수를 필요로하므로 완전 탐색
# 세로가 최대 8이므로  8! -> 40320 충분

# 1. 던전의 입장 순서를 나열
# 2. 현재 피로도 높으면 입장 및 차감
# 3. 만약 부족하다면 그다음 경우의 수
# 4. 모든 던전 통과시  최대 던전 수 갱신

from itertools import permutations

def solution(k, dungeons):
    
    max_explorer = 0
    for case in permutations(dungeons, len(dungeons)):
        current = k
        count = 0
        
        for (threshold, cost) in case:
            if not current >= threshold:
                break
                
            current -= cost
            count += 1
            
        max_explorer = max(max_explorer, count)
    
    return max_explorer

# ============================================================
# DFS 백트래킹 버전 (permutations 대신 직접 구현)
# ============================================================
# 재귀로 모든 순서를 탐색하며, 방문 체크로 중복 방지
# 시간 복잡도: O(N! × N) - permutations와 동일
# 장점: 가지치기(pruning) 적용 가능

def solutionv2(k, dungeons):
    n = len(dungeons)
    visited = [False] * n
    max_count = [0]  # 리스트로 감싸서 내부 함수에서 수정 가능하게
    
    def dfs(current, count):
        # 현재까지 탐험한 수로 최대값 갱신
        max_count[0] = max(max_count[0], count)
        
        # 가지치기: 이미 모든 던전 탐험 완료
        if count == n:
            return
        
        # 모든 던전에 대해 방문 시도
        for i in range(n):
            if visited[i]:
                continue
                
            threshold, cost = dungeons[i]
            
            # 입장 가능한 경우만 진행
            if current >= threshold:
                visited[i] = True
                dfs(current - cost, count + 1)
                visited[i] = False  # 백트래킹
    
    dfs(k, 0)
    return max_count[0]
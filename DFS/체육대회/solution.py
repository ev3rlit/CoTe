# 학생들중 한 종목당 한명만뽑을 수 있으며 3개 종목이 있으므로 3개명 뽑음
# 목표 : 능력치의 합을 최대화 하는것
# 예시에서는  탁구 준모, 수영 정현, 테니스, 석환 = 40 + 100 + 70
# 완전탐색도 가능하고, 그리디는 안됨
# 학생수는 10명 종목 수는 어쨋든 학생수 보다는 적음
# 그렇다면 10P10 = 10! = 360만
# DFS로 충분히 가능할것으로 보임
# 음 종목수보다 학생수가 많으므로 백트래킹으로 해야하나?
# 종결 조건은  종목수 만큼 학생 수가 확보된 경우임
# 해당 학생을 기준으로  세개를 방문 또는 방문하지 않는 경우
# 핵심은 순서가 중요함

# DFS 함수를 정의, 인자는 depth(종목수)와 current_sum(현재까지 합계)를 상태로 저장
# 종료 조건 = depth == len(ability[0])
# 0 부터 N-1번 학생까지 순회
# - 아직 대표로 선발되지 않았다면  대표 선정 및 DFS(depth+1, current_sum + ability[i][depth]) 호출
# - 방문 체크 해제
# visited = [False] * 학생수로 초기화
# dfs(0,0)으로 호출

def solution(ability):
    
    students = len(ability)
    sports = len(ability[0])
    visited = [False] * students
    max_ability = [0]
    
    def dfs(depth, current_sum):
        if depth == sports:
            max_ability[0] = max(max_ability[0], current_sum)
            return
            
        for i in range(students):
            if visited[i]:
                continue
                
            visited[i] = True
            dfs(depth+1, current_sum + ability[i][depth])
            visited[i] = False
            
    dfs(0,0)
    
    return max_ability[0]

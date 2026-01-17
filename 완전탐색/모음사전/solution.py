# 단어 순서대로 만들때 몇번째 단어인지 확인
# 제시된 문자 5개와  최대 5길이 단어임
# DFS로  사전순대로 순회하면서 일치하면 반환
# 되돌아오려면 백트래킹을 해야하네?
# 최대 5길이를 만족하면 종료

# 입력 크기는 5개 단어중 1 ~ 5자리 일때 이므로  5^1 + 5^2 + ... + 5^5 = 5 + 25 + 125 + 625 + 3125 = 1만 미만
# DFS 완전탐색 방법
# 현재 문자열을 방문할때 마다 카운트 증가
# 현재 문자열 == word라면 카운트 반환
# 종결 조건은  길이 5이면 종료
# 인접 노드 방문은 A, E, I, O, U 순서대로  추가하면서 재귀
# 목표 단어를 찾으면 즉시 반환


def solutionv2(word):
    
    characters = ['A','E','I','O','U']
    
    def dfs(current, count):
        """
        current: 현재까지 만든 문자열
        count: 현재까지 방문한 단어 수
        
        반환값: (찾았는지 여부, 최종 카운트)
        """
    
        if current:
            count +=1
            if current == word:
                return (True, count)
            
        if len(current) == 5:
            return (False, count)
        
        for char in characters:
            found, count = dfs(current+char, count)
            if found:
                return (True, count)
            
        return (False,count)
    
    found, result = dfs('',0)
    return result 

def solutionv1(word):
    
    characters = ['A','E','I','O','U']
    found = [False]
    count = [0]
    
    
    def dfs(current):
        # 현재 문자열 방문
        if current:
            count[0] += 1
            if current == word:
                found[0] = True
                return
            
        # 길이 5 도달시 종료
        if len(current) == 5:
            return
        
        # 문자 탐색
        for char in characters:
            if found[0]:
                return
            
            dfs(current + char)
        
    dfs('')
    return count[0]

def solution(word):
    return solutionv2(word)
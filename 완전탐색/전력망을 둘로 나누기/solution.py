# n은 100이하  wires는 n-1
# 송전탑의 전선들중 하나를 끊어서 네트워크를 2개 만든다 -> 끊는 위치가 중요
# 전선들중 하나를 끊어서 송전탑의 갯수 차이가 가장 적은 경우 
# N-1 전선 끊기와  네트워크 확인 비용 이거는 시간복잡도 측정하는 방법을 몰라서
# 어쨋든  DFS로 하면  시간내에 불수있을걸로 보임

# 1. 송전탑의 최대 차이는 송전탑 하나가 몰린 경우
# 1. 전선줄 리스트를 토대로 그래프를 구성
# 1. 전선들 리스트를 순회하면서 사용 불가능한 전선줄 집합을 표시
# 1. 해당 전선을 끊었을 때 네트워크 갯수를 확인
# 1. 미방문 처리 및 count = 0으로 초기화
# 1. 전체 송전탑을 순회하면서 미방문한 경우 DFS 탐색 및 네트워크 카운팅 증가
# 1. DFS 탐색시 방문처리 및 해당 노드에서 인접 노드들을 순회
# 1. 미방문한 인접 노드인 경우 DFS 탐색
# 1. DFS 상태에는 탐색할 노드 및 현재 송전탑의 갯수를 상태로 저장
# 3. 네트워크가 2개인지 확인, DFS로 네트워크 갯수 및 송전탑 갯수 측정
# 4. 송전탑 갯수 차이의 절대값을 배열에 기록
# 5. 배열에서 가장 작은 값 반환

from collections import defaultdict

def diff_network(n,graph, node, exclude):
    visited = set()
    
    def dfs(node, exclude):
        visited.add(node)
        count = 1
        
        for neighbor in graph[node]:
            if neighbor in visited:
                continue
            
            # 끊어진 전선줄은 무시
            if exclude == set([node, neighbor]):
                continue
            
            count += dfs(neighbor, exclude)
            
        return count
    
    count = dfs(node, exclude)
    diff = abs(count - (n-count))
    
    return diff
            

def solution(n, wires):
    graph = defaultdict(list)
    for (v1, v2) in wires:
        graph[v1].append(v2)
        graph[v2].append(v1)
        
    min_diff = n
    for (v1,v2) in wires:
        diff = diff_network(n,graph, v1, set([v1,v2]))
        min_diff = min(min_diff, diff)
    
    return min_diff
import sys
from collections import defaultdict
sys.setrecursionlimit(10000)
input = sys.stdin.readline

def solution():
    N, M = map(int, input().split())

    # 인접 리스트로 그래프 구성
    graph = defaultdict(list)
    for _ in range(M):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
        
    # 방문 배열
    visited = [False] * N
    
    def dfs(node, depth):
        # 깊이 5 도달 종료
        if depth == 5:
            return True

        # 현재 노드의 이웃 탐색
        for neighbor in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                if dfs(neighbor, depth + 1):
                    return True
                visited[neighbor] = False

        return False

    # 모든 정점에서 DFS 시작
    for start in range(N):
        visited[start] = True
        if dfs(start, 1):
            print(1)
            return
        visited[start] = False
    
    print(0)

if __name__ == "__main__":
    solution()

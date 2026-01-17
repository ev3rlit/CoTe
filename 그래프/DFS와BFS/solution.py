import sys
from collections import deque, defaultdict

def solutiion():
    N, M, V = map(int, sys.stdin.readline().split())

    # 인접 리스트 구성(양방향)
    graph = defaultdict(list)
    for _ in range(M):
        a,b = map(int, sys.stdin.readline().split())
        graph[a].append(b)
        graph[b].append(a)

    # 작은 번호 먼저 방문하도록 정렬
    for key in graph:
        graph[key].sort()

    # DFS(재귀)
    dfs_result = []
    dfs_visited = [False] * (N+1)

    def dfs(node):
        dfs_visited[node] = True
        dfs_result.append(node)
        for neighbor in graph[node]:
            if not dfs_visited[neighbor]:
                dfs(neighbor)
    
    dfs(V)

    # BFS(큐)
    bfs_result = []
    bfs_visited = [False] * (N+1)
    queue = deque([V])
    bfs_visited[V] = True
    
    while queue:
        node = queue.popleft()
        bfs_result.append(node)
        for neighbor in graph[node]:
            if not bfs_visited[neighbor]:
                bfs_visited[neighbor] = True
                queue.append(neighbor)

    return [' '.join(map(str,dfs_result)), ' '.join(map(str,bfs_result))]

if __name__ == "__main__":
    print(*solutiion(), sep='\n')
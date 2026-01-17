# DFS와 BFS

#그래프 #DFS #BFS #알고리즘 #코딩테스트

## 문제 난이도: 하 (Silver II)

## 1. 📊 객관적 분석 및 근거

**제약 조건**
- N = 1,000 (정점 개수)
- M = 10,000 (간선 개수)
- 시간 제한: 2초
- 메모리 제한: 128MB

**시간 복잡도 역산**
- 2초 ≈ 2 × 10^8 연산
- DFS/BFS 각각 O(V + E) = O(1,000 + 10,000) = O(11,000)
- 두 번 수행해도 22,000 연산 → 충분히 여유로움

**알고리즘 선택**
- 선택: 재귀 DFS + 큐 BFS
- 근거: 
  - 문제에서 DFS, BFS 둘 다 명시적으로 요구
  - N이 작아서 재귀 깊이 제한 걱정 없음
  - "정점 번호가 작은 것 먼저 방문" → 인접 리스트 정렬 필요

---

## 2. 🧠 자연어 실행 흐름

**공통 준비**
1. N, M, V를 입력받는다
2. 인접 리스트로 그래프를 구성한다 (양방향)
3. 각 정점의 인접 리스트를 **오름차순 정렬**한다 (작은 번호 먼저 방문 조건)

**DFS 수행**
1. 방문 배열을 초기화한다
2. 시작 정점 V를 방문 처리하고 출력한다
3. 현재 정점의 인접 정점 중 방문하지 않은 곳으로 재귀 호출한다
4. 더 이상 방문할 곳이 없으면 돌아온다

**BFS 수행**
1. 방문 배열을 다시 초기화한다
2. 시작 정점 V를 큐에 넣고 방문 처리한다
3. 큐에서 정점을 꺼내 출력한다
4. 해당 정점의 인접 정점 중 방문하지 않은 곳을 모두 큐에 넣고 방문 처리한다
5. 큐가 빌 때까지 3-4를 반복한다

---

## 3. 💻 Code Implementation

```python
import sys
from collections import deque, defaultdict
input = sys.stdin.readline

def solution():
    N, M, V = map(int, input().split())
    
    # 인접 리스트 구성 (양방향)
    graph = defaultdict(list)
    for _ in range(M):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    
    # 작은 번호 먼저 방문하도록 정렬
    for key in graph:
        graph[key].sort()
    
    # DFS (재귀)
    dfs_result = []
    dfs_visited = [False] * (N + 1)
    
    def dfs(node):
        dfs_visited[node] = True
        dfs_result.append(node)
        for neighbor in graph[node]:
            if not dfs_visited[neighbor]:
                dfs(neighbor)
    
    dfs(V)
    
    # BFS (큐)
    bfs_result = []
    bfs_visited = [False] * (N + 1)
    queue = deque([V])
    bfs_visited[V] = True
    
    while queue:
        node = queue.popleft()
        bfs_result.append(node)
        for neighbor in graph[node]:
            if not bfs_visited[neighbor]:
                bfs_visited[neighbor] = True
                queue.append(neighbor)
    
    # 출력
    print(' '.join(map(str, dfs_result)))
    print(' '.join(map(str, bfs_result)))

if __name__ == "__main__":
    solution()
```

**복잡도 분석**
- 시간: O(V + E) × 2 = O(N + M) ≈ O(11,000)
- 공간: O(V + E) 인접 리스트 + O(V) 방문 배열 ≈ O(N + M)

---

## 4. 🔍 핵심 포인트

| 포인트 | 설명 |
|--------|------|
| **정렬** | 인접 리스트를 정렬해야 "작은 번호 먼저" 조건 충족 |
| **양방향 간선** | 입력받을 때 양쪽 모두 추가 필요 |
| **1-indexed** | 정점 번호가 1부터 시작 → 배열 크기 N+1 |
| **출력 형식** | 공백으로 구분하여 출력 |

# ABCDE (백준 13023)

#그래프 #DFS #백트래킹 #알고리즘 #코딩테스트

## 1. 📊 객관적 분석 및 근거

**제약 조건**
- N = 5 ~ 2,000 (사람 수)
- M = 1 ~ 2,000 (친구 관계 수)
- 시간 제한: 2초
- 메모리 제한: 512MB

**문제 핵심**
- A-B-C-D-E 형태의 **길이 4인 경로(5개의 정점을 거치는 경로)** 가 존재하는지 확인
- 즉, 연속된 친구 관계가 4번 이어지는 경로를 찾아야 함

**시간 복잡도 역산**
- 2초 ≈ 2 × 10^8 연산
- 모든 정점에서 DFS 시작: O(N)
- 각 DFS에서 깊이 5까지만 탐색: 최악의 경우 O(M) 간선 탐색
- 총 시간 복잡도: O(N × M) = O(2000 × 2000) = O(4 × 10^6) ✅ 충분

**알고리즘 선택**
- 선택: **DFS + 백트래킹**
- 근거:
    1. **경로 탐색 문제**: 특정 길이의 경로 존재 여부 → DFS가 적합
    2. **깊이 제한**: 깊이 5로 제한되므로 가지치기 효과적
    3. **백트래킹**: 방문 표시 후 복원하여 다양한 경로 탐색 가능
- 기각된 대안:
    - BFS: 경로 길이보다 최단 거리에 특화, 경로 상태 관리 복잡
    - 브루트포스 (5중 루프): O(N^5) = 매우 느림

---

## 2. 🧠 자연어 실행 흐름

(코드 없이 순수 한글로 작성)

1. **그래프 구성**: 인접 리스트로 친구 관계를 양방향 그래프로 저장한다.

2. **모든 정점에서 DFS 시작**: 0번부터 N-1번까지 각각을 시작점(A)으로 설정한다.

3. **DFS 탐색 (재귀)**:
   - 현재 정점을 방문 처리한다.
   - 현재 깊이가 5이면 (A→B→C→D→E 완성) True를 반환하고 탐색 종료.
   - 현재 정점과 연결된 미방문 이웃 정점으로 재귀 호출한다.
   - 재귀에서 True가 반환되면 바로 True를 전파한다.
   - **백트래킹**: 이웃 탐색이 끝나면 방문 표시를 해제하여 다른 경로에서 재사용 가능하게 한다.

4. **결과 판단**:
   - 어떤 시작점에서든 깊이 5에 도달하면 1 출력
   - 모든 시작점에서 실패하면 0 출력

---

## 3. 💻 Code Implementation

(언어: Python)
```python
import sys
from collections import defaultdict
sys.setrecursionlimit(10000)
input = sys.stdin.readline

def solve():
    N, M = map(int, input().split())
    
    # 인접 리스트로 그래프 구성
    graph = defaultdict(list)
    for _ in range(M):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)  # 양방향 그래프
    
    # 방문 배열
    visited = [False] * N
    
    def dfs(node, depth):
        # 깊이 5 도달 = A-B-C-D-E 경로 완성
        if depth == 5:
            return True
        
        # 현재 노드의 이웃 탐색
        for neighbor in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = True  # 방문 처리
                if dfs(neighbor, depth + 1):
                    return True
                visited[neighbor] = False  # 백트래킹: 방문 해제
        
        return False
    
    # 모든 정점에서 DFS 시작
    for start in range(N):
        visited[start] = True
        if dfs(start, 1):
            print(1)
            return
        visited[start] = False  # 백트래킹
    
    print(0)

solve()
```

**복잡도 분석**
- 시간: O(N × M) — 최악의 경우 모든 시작점에서 모든 간선 탐색
- 공간: O(N + M) — 인접 리스트 O(M), 방문 배열 O(N), 재귀 스택 O(5)

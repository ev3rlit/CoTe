# 그래프 패턴 스타일 가이드

> 그래프 탐색 및 관련 알고리즘 구현 스타일

---

## 사용 시점

다음 키워드가 보이면 그래프를 고려:

- **노드**와 **간선** 관계
- **연결 여부** / **경로 존재**
- **연결 요소** 개수
- **최단 거리** (가중치 있음/없음)
- **인접한** / **이웃한**
- **네트워크** / **관계**

---

## 핵심 패턴

### 인접 리스트 구성

```python
from collections import defaultdict

def solution():
    N, M = map(int, input().split())

    # 인접 리스트로 그래프 구성
    graph = defaultdict(list)
    for _ in range(M):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)  # 무방향 그래프
```

---

## 변수 네이밍

| 용도 | 변수명 | 예시 |
|------|--------|------|
| 그래프 | `graph` | `graph = defaultdict(list)` |
| 노드 개수 | `N`, `n` | `N, M = map(int, input().split())` |
| 간선 개수 | `M`, `m` | `M = len(edges)` |
| 현재 노드 | `node`, `cur` | `def dfs(node, depth)` |
| 이웃 노드 | `neighbor` | `for neighbor in graph[node]` |
| 방문 배열 | `visited` | `visited = [False] * N` |
| 시작 노드 | `start` | `for start in range(N)` |

---

## 그래프 구성 패턴

### defaultdict 사용 (권장)

```python
from collections import defaultdict

graph = defaultdict(list)
for a, b in edges:
    graph[a].append(b)
    graph[b].append(a)  # 무방향
```

### 리스트 사용

```python
graph = [[] for _ in range(N)]
for a, b in edges:
    graph[a].append(b)
    graph[b].append(a)
```

### 가중치 포함

```python
graph = defaultdict(list)
for a, b, cost in edges:
    graph[a].append((b, cost))
    graph[b].append((a, cost))
```

---

## 그래프 DFS 패턴

### 기본 DFS

```python
import sys
sys.setrecursionlimit(10000)

visited = [False] * N

def dfs(node, depth):
    # 종료 조건
    if depth == target:
        return True

    # 이웃 탐색
    for neighbor in graph[node]:
        if not visited[neighbor]:
            visited[neighbor] = True
            if dfs(neighbor, depth + 1):
                return True
            visited[neighbor] = False  # 백트래킹

    return False
```

### 모든 시작점에서 탐색

```python
# 모든 정점에서 DFS 시작
for start in range(N):
    visited[start] = True
    if dfs(start, 1):
        print(1)
        return
    visited[start] = False

print(0)
```

---

## 그래프 BFS 패턴

### 기본 BFS

```python
from collections import deque

def bfs(start, graph, N):
    visited = [False] * N
    visited[start] = True
    queue = deque([start])

    while queue:
        node = queue.popleft()

        for neighbor in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)

    return visited
```

### 최단 거리 BFS

```python
def bfs_distance(start, end, graph, N):
    visited = [False] * N
    visited[start] = True
    queue = deque([(start, 0)])  # (노드, 거리)

    while queue:
        node, dist = queue.popleft()

        if node == end:
            return dist

        for neighbor in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append((neighbor, dist + 1))

    return -1
```

---

## 연결 요소 패턴

```python
def count_components(N, graph):
    visited = [False] * N
    count = 0

    def dfs(node):
        for neighbor in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                dfs(neighbor)

    for i in range(N):
        if not visited[i]:
            visited[i] = True
            dfs(i)
            count += 1

    return count
```

---

## ABCDE 스타일 (경로 길이)

깊이 5인 경로 존재 여부 찾기:

```python
import sys
from collections import defaultdict
sys.setrecursionlimit(10000)

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
        # 깊이 5 도달 시 종료
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
```

---

## 입력 처리 패턴 (백준)

```python
import sys
input = sys.stdin.readline

def solution():
    N, M = map(int, input().split())

    graph = defaultdict(list)
    for _ in range(M):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
```

---

## 체크리스트

구현 시 확인할 항목:

- [ ] 그래프가 **방향/무방향**인지 확인
- [ ] 노드 번호가 **0-based / 1-based**인지 확인
- [ ] `defaultdict(list)` 또는 리스트 초기화
- [ ] 방문 배열 크기: `[False] * N`
- [ ] 재귀 깊이 제한: `sys.setrecursionlimit()`
- [ ] 시작점 방문 처리
- [ ] 백트래킹 필요 여부

---

## 관련 문제 유형

| 유형 | 특징 |
|------|------|
| ABCDE | 경로 깊이 5 찾기 |
| DFS와 BFS | 기본 탐색 순서 출력 |
| 연결 요소 | 컴포넌트 개수 세기 |
| 촌수 계산 | 두 노드 간 최단 거리 |
| 양과 늑대 | 상태 포함 그래프 탐색 |

---

## 참고

- `/GEMINI.md` - 전체 스타일 가이드
- `/BFS/GEMINI.md` - BFS 패턴
- `/DFS/GEMINI.md` - DFS/백트래킹 패턴

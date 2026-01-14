# DFS Pattern Skeleton

> 생성일: 2026-01-12

---

## Why & What (이 패턴은 왜/무엇)
- **목적**: 그래프/트리를 끝까지 깊이 들어가며 탐색. 경로 탐색, 연결 요소 찾기, 백트래킹에 필수
- **본질**: "갈 수 있는 데까지 가보고, 막히면 돌아온다"
- **장점**: BFS 대비 메모리 효율적 (재귀 스택만 사용). 경로/상태 복원이 자연스러움. 백트래킹과 결합 용이

## When to Use (이럴 때 사용)
문제에서 다음 키워드가 보이면 이 패턴을 떠올리세요:
- `모든 경로`: 모든 가능한 경로를 탐색
- `연결 요소`: 그래프에서 연결된 컴포넌트 개수
- `사이클 탐지`: 그래프에 사이클이 있는지 확인
- `백트래킹`: 조건을 만족하는 모든 조합/순열 탐색
- `깊이 우선`: 트리/그래프 순회 (전위, 중위, 후위)
- `섬의 개수`: 연결된 영역 카운팅
- `ABCDE 관계`: 연속된 친구 관계 N개 존재 여부

---

## 핵심 구조

```python
import sys
sys.setrecursionlimit(10000)  # Python 재귀 제한 해제

def dfs(node, graph, visited):
    # 1. [Mark Visit] 현재 노드 방문 처리
    visited[node] = True
    
    # 2. [Process] 현재 노드에서 할 일 (선택적)
    process(node)
    
    # 3. [Explore Neighbors] 인접 노드 탐색
    for neighbor in graph[node]:
        # 4. [Validity Check] 방문 가능 여부 판정
        if not visited[neighbor] and is_valid(neighbor):
            # 5. [Recurse] 재귀 호출
            dfs(neighbor, graph, visited)
    
    # 6. [Backtrack] (선택적) 백트래킹 시 상태 복원
    # visited[node] = False  # 다른 경로에서 재방문 허용

# 시작점에서 DFS 호출
visited = [False] * (n + 1)
dfs(start, graph, visited)
```

---

## Customization Points

| Hook | 설명 | 예시 |
|------|------|------|
| `process(node)` | 노드 방문 시 처리 | 결과 저장, 카운트 증가 |
| `is_valid(neighbor)` | 방문 가능 조건 | 범위 체크, 조건 판정 |
| `visited` 복원 여부 | 백트래킹 필요 시 | 경로 탐색, 순열 생성 |
| 반환값 | 탐색 결과 전달 | True/False, 깊이, 경로 |

---

## Variations (응용 유형)

### 변형 A: 반복문 DFS (스택 사용)
**상황**: 재귀 깊이가 너무 깊거나, 스택 오버플로우 방지가 필요할 때
**핵심 변화**: 재귀 대신 명시적 스택 사용

```python
def dfs_iterative(start, graph):
    stack = [start]
    visited = set()
    result = []
    
    while stack:
        node = stack.pop()
        
        if node in visited:
            continue
        
        visited.add(node)
        result.append(node)
        
        # 역순으로 넣어야 순서 유지 (작은 번호 먼저 방문)
        for neighbor in reversed(graph[node]):
            if neighbor not in visited:
                stack.append(neighbor)
    
    return result
```

### 변형 B: 경로 찾기 + 조기 종료
**상황**: 특정 깊이/조건 만족 시 즉시 종료 (예: ABCDE 문제)
**핵심 변화**: 재귀 함수가 True/False 반환, 찾으면 즉시 전파

```python
def dfs_find_path(node, graph, visited, depth, target_depth):
    # 목표 깊이 도달 시 성공
    if depth == target_depth:
        return True
    
    visited[node] = True
    
    for neighbor in graph[node]:
        if not visited[neighbor]:
            if dfs_find_path(neighbor, graph, visited, depth + 1, target_depth):
                return True  # 찾으면 즉시 종료
    
    visited[node] = False  # 백트래킹
    return False

# 모든 시작점에서 시도
for start in range(n):
    visited = [False] * n
    if dfs_find_path(start, graph, visited, 1, 5):
        print(1)
        exit()
print(0)
```

### 변형 C: 연결 요소 카운팅
**상황**: 그래프에서 연결된 컴포넌트 개수 세기 (섬의 개수)
**핵심 변화**: 모든 노드를 순회하며 미방문 노드에서 DFS 시작

```python
def count_components(n, graph):
    visited = [False] * n
    count = 0
    
    def dfs(node):
        visited[node] = True
        for neighbor in graph[node]:
            if not visited[neighbor]:
                dfs(neighbor)
    
    for node in range(n):
        if not visited[node]:
            dfs(node)
            count += 1  # 새로운 컴포넌트 발견
    
    return count
```

### 변형 D: 2D 그리드 DFS
**상황**: 격자에서 연결된 영역 탐색 (섬의 개수, 영역 넓이)
**핵심 변화**: 4방향/8방향 이동, 좌표 기반 방문 체크

```python
def dfs_grid(grid, x, y, visited):
    rows, cols = len(grid), len(grid[0])
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]  # 상하좌우
    
    visited[x][y] = True
    area = 1
    
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < rows and 0 <= ny < cols:
            if not visited[nx][ny] and grid[nx][ny] == 1:
                area += dfs_grid(grid, nx, ny, visited)
    
    return area

# 모든 섬의 넓이 계산
def count_islands(grid):
    rows, cols = len(grid), len(grid[0])
    visited = [[False] * cols for _ in range(rows)]
    islands = []
    
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1 and not visited[i][j]:
                area = dfs_grid(grid, i, j, visited)
                islands.append(area)
    
    return len(islands), islands
```

### 변형 E: 백트래킹 (순열/조합 생성)
**상황**: 모든 가능한 조합, 순열, 부분집합 탐색
**핵심 변화**: 방문 해제로 다른 경로에서 재사용 허용

```python
def generate_permutations(nums):
    result = []
    used = [False] * len(nums)
    
    def backtrack(path):
        if len(path) == len(nums):
            result.append(path[:])
            return
        
        for i in range(len(nums)):
            if used[i]:
                continue
            
            # 선택
            used[i] = True
            path.append(nums[i])
            
            # 탐색
            backtrack(path)
            
            # 선택 해제 (백트래킹)
            path.pop()
            used[i] = False
    
    backtrack([])
    return result
```

### 변형 F: 사이클 탐지
**상황**: 방향 그래프에서 사이클 존재 여부 확인
**핵심 변화**: 3가지 상태 (미방문, 탐색중, 완료)로 구분

```python
def has_cycle(n, graph):
    # 0: 미방문, 1: 탐색 중, 2: 탐색 완료
    state = [0] * n
    
    def dfs(node):
        state[node] = 1  # 탐색 시작
        
        for neighbor in graph[node]:
            if state[neighbor] == 1:  # 탐색 중인 노드 재방문 = 사이클
                return True
            if state[neighbor] == 0:
                if dfs(neighbor):
                    return True
        
        state[node] = 2  # 탐색 완료
        return False
    
    for node in range(n):
        if state[node] == 0:
            if dfs(node):
                return True
    
    return False
```

### 변형 G: 위상 정렬 (DFS 기반)
**상황**: DAG에서 의존성 순서 결정 (작업 순서, 빌드 순서)
**핵심 변화**: 후위 순회 결과를 역순으로 반환

```python
def topological_sort(n, graph):
    visited = [False] * n
    result = []
    
    def dfs(node):
        visited[node] = True
        for neighbor in graph[node]:
            if not visited[neighbor]:
                dfs(neighbor)
        result.append(node)  # 후위 순회
    
    for node in range(n):
        if not visited[node]:
            dfs(node)
    
    return result[::-1]  # 역순이 위상 정렬 결과
```

---

## 핵심 인사이트

### DFS vs BFS 선택 기준

| 상황 | DFS | BFS |
|------|-----|-----|
| 모든 경로 탐색 | ✅ | ❌ |
| 최단 거리 보장 | ❌ | ✅ |
| 메모리 효율 (깊은 트리) | ✅ | ❌ |
| 연결 요소 카운팅 | ✅ | ✅ |
| 백트래킹 | ✅ | ❌ |
| 레벨 단위 처리 | ❌ | ✅ |

### 시간/공간 복잡도
- **시간**: O(V + E) - 모든 정점과 간선을 한 번씩 탐색
- **공간**: O(V) - 재귀 스택 + visited (최악: O(V) 깊이)

### Python 재귀 제한 주의
```python
import sys
sys.setrecursionlimit(10000)  # 기본값 1000 → 필요시 증가
```

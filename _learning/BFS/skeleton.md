# BFS Pattern Skeleton

> 생성일: 2026-01-12

---

## 암기 카드 (필수 4요소)

- **트리거 문장**
  - "최단 거리/최소 이동 횟수"
  - "가장 가까운", "레벨 순서", "미로 탈출"
- **핵심 불변식**
  - 큐에서 먼저 나오는 상태가 항상 더 짧은 거리(가중치 없는 그래프)
  - 노드는 큐에 넣는 순간 방문 처리해야 중복 삽입이 없다
- **실수 포인트**
  - `pop()` 사용(DFS처럼 동작) / 방문 처리를 꺼낼 때 함 / 범위 체크 누락
- **템플릿 위치**
  - 이 문서의 `핵심 구조` 코드 블록

## 예제 문제 (입문 → 확장)

- 백준 2178 미로 탐색
- 백준 7576 토마토 (다중 시작점)
- 프로그래머스 게임 맵 최단거리

---

## Why & What (이 패턴은 왜/무엇)
- **목적**: 시작점에서 가까운 순서대로 탐색하며, **최단 거리/최소 비용**을 보장
- **본질**: "가까운 것부터 차례대로 방문한다" — 큐를 사용하여 FIFO 순서로 탐색
- **장점**: 가중치 없는 그래프에서 최단 경로가 **수학적으로 보장**됨. DFS와 달리 깊이 우선이 아닌 너비 우선으로 레벨 단위 처리 가능

## When to Use (이럴 때 사용)
문제에서 다음 키워드가 보이면 이 패턴을 떠올리세요:
- `최단 거리`: 시작점에서 도착점까지 최소 이동 횟수
- `최소 횟수`: 버튼 누르기 최소 횟수, 최소 연산 횟수 등
- `레벨 순서`: 트리/그래프의 레벨별 순회
- `가까운 것부터`: "가장 가까운 X를 찾아라"
- `미로 탈출`: 격자에서 출구까지 최단 경로
- `상태 공간 탐색`: 현재 상태에서 목표 상태까지 최소 변환

---

## 핵심 구조

```python
from collections import deque

def bfs(start, graph):
    # 1. [Init Queue] ─────────────────────────────────
    #    역할: 시작점을 큐에 삽입
    #    ADAPT: 시작점이 여러 개면 모두 큐에 넣음 (다중 시작점 BFS)
    queue = deque([start])
    
    # 2. [Mark Visit] ─────────────────────────────────
    #    역할: 방문 처리 (중복 삽입 방지)
    #    WHY: 큐에 넣을 때 방문 처리해야 같은 노드가 여러 번 큐에 들어가는 것을 방지
    #    PITFALL: 꺼낼 때 방문 처리하면 같은 노드가 여러 번 큐에 들어가 TLE 발생
    visited = set()
    visited.add(start)
    
    # 3. [Level Tracking] ─────────────────────────────────
    #    역할: 거리/레벨 기록 (선택적)
    #    ADAPT: 필요 없으면 생략, 경로 복원 필요하면 parent dict 추가
    distance = {start: 0}
    
    # 4. [Main Loop] ─────────────────────────────────
    #    역할: 큐가 빌 때까지 반복
    #    WHY: 큐가 비면 모든 도달 가능한 노드를 방문했다는 의미
    #    COMPLEXITY: 각 노드는 한 번씩만 큐에 들어감 → O(V)
    while queue:
        # 5. [Extract] ─────────────────────────────────
        #    역할: 현재 노드 꺼내기
        #    WHY: popleft()로 앞에서 꺼내야 FIFO 유지 → 최단 거리 보장
        #    PITFALL: pop()으로 뒤에서 꺼내면 DFS처럼 동작함
        current = queue.popleft()
        
        # 6. [Goal Check] ─────────────────────────────────
        #    역할: 목표 도달 시 즉시 반환
        #    WHY: BFS는 처음 도달한 순간이 최단 거리이므로 바로 반환 가능
        #    ADAPT: 목표가 없으면 생략 (전체 탐색)
        if is_goal(current):
            return distance[current]  # 최단 거리 보장
        
        # 7. [Explore Neighbors] ─────────────────────────────────
        #    역할: 인접 노드 탐색
        #    COMPLEXITY: 모든 간선을 한 번씩 탐색 → O(E)
        for neighbor in get_neighbors(current, graph):
            # 8. [Validity Check] ─────────────────────────────────
            #    역할: 방문 가능 여부 판정
            #    ADAPT: 그리드면 범위 체크, 조건에 따라 벽/장애물 체크 추가
            if is_valid(neighbor) and neighbor not in visited:
                # 9. [Enqueue & Mark] ─────────────────────────────────
                #    역할: 큐 삽입 + 즉시 방문 처리
                #    PITFALL: 반드시 "넣을 때" 방문 처리 — 꺼낼 때 하면 중복 발생
                queue.append(neighbor)
                visited.add(neighbor)
                distance[neighbor] = distance[current] + 1
    
    # 10. [Not Found] ─────────────────────────────────
    #    역할: 목표 도달 불가
    #    ADAPT: 전체 탐색이면 visited 반환, 거리면 distance dict 반환
    return -1
```

---

## Customization Points

| Hook | 설명 | 예시 |
|------|------|------|
| `get_neighbors(node, graph)` | 다음 노드들 반환 | 인접 리스트, 4방향/8방향 |
| `is_valid(neighbor)` | 방문 가능 조건 | 범위 체크, 벽 체크 |
| `is_goal(node)` | 목표 도달 여부 | 도착점, 특정 상태 |
| `visited` 구조 | 방문 상태 저장 | set, 2D 배열, dict |

---

## Variations (응용 유형)

### 변형 A: 2D 그리드 탐색
**상황**: 미로, 게임 맵에서 최단 경로를 찾을 때
**핵심 변화**: 좌표를 노드로, 4방향/8방향을 이웃으로
**추천 문제**: 
- [백준 2178 미로 탐색](https://www.acmicpc.net/problem/2178)
- [백준 7576 토마토](https://www.acmicpc.net/problem/7576)
- [프로그래머스 게임 맵 최단거리](https://programmers.co.kr/learn/courses/30/lessons/1844)

```python
from collections import deque

def bfs_grid(grid, start, end):
    rows, cols = len(grid), len(grid[0])
    # [Direction Vector] ─────────────────────────────────
    #    ADAPT: 8방향이면 대각선 추가: (-1,-1), (-1,1), (1,-1), (1,1)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)] # 상하좌우
    
    # [Init] ─────────────────────────────────
    #    ADAPT: 거리만 필요하면 (x, y, dist) 튜플로, 경로 필요하면 parent 배열
    queue = deque([(start[0], start[1], 0)])  # (x, y, distance)
    visited = [[False] * cols for _ in range(rows)]
    visited[start[0]][start[1]] = True
    
    while queue:
        x, y, dist = queue.popleft()
        
        # [Goal Check] ─────────────────────────────────
        if (x, y) == end:
            return dist
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            # [Boundary Check] ─────────────────────────────────
            #    PITFALL: 범위 체크 안 하면 IndexError
            if not(0 <= nx < rows) or not(0 <= ny < cols):
                continue

            # [Wall Check] ─────────────────────────────────
            #    ADAPT: 벽 표시 방식에 따라 조건 변경 (1이 벽 vs 0이 벽)
            if grid[nx][ny] == 1:
                continue

            # [Visited Check] ─────────────────────────────────
            #    PITFALL: 이미 방문한 노드를 다시 방문하면 무한 루프
            if visited[nx][ny]:
                continue

            visited[nx][ny] = True
            queue.append((nx, ny, dist + 1))
    
    return -1
```                         

### 변형 B: 레벨 단위 처리
**상황**: 트리 레벨 순회, BFS 깊이별 처리가 필요할 때
**핵심 변화**: `len(queue)`로 현재 레벨 크기 저장 후 그만큼만 처리
**추천 문제**: 
- [백준 2644 촌수계산](https://www.acmicpc.net/problem/2644)
- [백준 16236 아기 상어](https://www.acmicpc.net/problem/16236)
- [LeetCode 102 Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/)

```python
from collections import deque

def bfs_level_order(root):
    if not root:
        return []
    
    result = []
    queue = deque([root])
    
    while queue:
        # [Level Size Capture] ─────────────────────────────────
        #    WHY: 루프 도중 queue 크기가 변하므로 미리 저장해야 함
        #    PITFALL: for _ in range(len(queue)) 안에서 len() 재호출하면 버그
        level_size = len(queue)
        level_nodes = []
        
        for _ in range(level_size):
            node = queue.popleft()
            level_nodes.append(node.val)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        result.append(level_nodes)
    
    return result
```

### 변형 C: 다차원 상태 BFS
**상황**: 벽 부수기, 열쇠 수집 등 추가 상태가 필요할 때
**핵심 변화**: 상태를 (x, y, 추가정보) 튜플로 표현, visited도 다차원
**추천 문제**: 
- [백준 2206 벽 부수고 이동하기](https://www.acmicpc.net/problem/2206)
- [백준 1600 말이 되고픈 원숭이](https://www.acmicpc.net/problem/1600)
- [백준 9328 열쇠](https://www.acmicpc.net/problem/9328)

```python
from collections import deque

def bfs_with_state(grid, start, end, max_break):
    """벽을 최대 max_break번 부술 수 있는 최단 경로"""
    rows, cols = len(grid), len(grid[0])
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    
    # [Multi-dimensional Visited] ─────────────────────────────────
    #    WHY: (x, y)만으로는 상태 구분 불가 — 벽 부순 횟수도 함께 기록
    #    PITFALL: 메모리 초과 주의 — 상태 공간이 N*M*K로 증가
    visited = [[[False] * (max_break + 1) for _ in range(cols)] for _ in range(rows)]
    
    queue = deque([(start[0], start[1], 0, 0)])  # (x, y, broken, dist)
    visited[start[0]][start[1]][0] = True
    
    while queue:
        x, y, broken, dist = queue.popleft()
        
        if (x, y) == end:
            return dist
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < rows and 0 <= ny < cols:
                # [State Transition] ─────────────────────────────────
                #    ADAPT: 벽이 아니면 그대로, 벽이면 부순 횟수 +1
                if grid[nx][ny] == 0 and not visited[nx][ny][broken]:
                    visited[nx][ny][broken] = True
                    queue.append((nx, ny, broken, dist + 1))
                elif grid[nx][ny] == 1 and broken < max_break and not visited[nx][ny][broken + 1]:
                    visited[nx][ny][broken + 1] = True
                    queue.append((nx, ny, broken + 1, dist + 1))
    
    return -1
```

### 변형 D: 0-1 BFS
**상황**: 간선 가중치가 0 또는 1인 그래프의 최단 경로
**핵심 변화**: deque 사용, 가중치 0이면 앞에, 1이면 뒤에 삽입
**추천 문제**: 
- [백준 13549 숨바꼭질 3](https://www.acmicpc.net/problem/13549)
- [백준 1261 알고스팟](https://www.acmicpc.net/problem/1261)
- [백준 2665 미로만들기](https://www.acmicpc.net/problem/2665)

```python
from collections import deque

def bfs_01(graph, start, end):
    """가중치가 0 또는 1인 그래프의 최단 경로"""
    n = len(graph)
    dist = [float('inf')] * n
    dist[start] = 0
    
    queue = deque([start])
    
    while queue:
        current = queue.popleft()
        
        for neighbor, weight in graph[current]:
            new_dist = dist[current] + weight
            # [Relaxation] ─────────────────────────────────
            #    WHY: 다익스트라와 달리 weight가 0 또는 1이라 deque로 충분
            #    PITFALL: weight > 1이면 이 방법 사용 불가 → 다익스트라 필요
            if new_dist < dist[neighbor]:
                dist[neighbor] = new_dist
                # [Priority by Weight] ─────────────────────────────────
                #    WHY: 가중치 0은 "거리 같음" → 먼저 처리해야 최단 보장
                #    COMPLEXITY: 다익스트라 O(E log V) 대비 O(V + E)로 빠름
                if weight == 0:
                    queue.appendleft(neighbor)  # 앞에 삽입
                else:
                    queue.append(neighbor)      # 뒤에 삽입
    
    return dist[end]
```

### 변형 E: 양방향 BFS (Bidirectional BFS)
**상황**: 시작점과 도착점이 명확하고, 탐색 공간이 매우 클 때
**핵심 변화**: 양쪽에서 동시에 탐색, 중간에서 만나면 종료
**추천 문제**: 
- [백준 1963 소수 경로](https://www.acmicpc.net/problem/1963)
- [백준 9019 DSLR](https://www.acmicpc.net/problem/9019)
- [LeetCode 127 Word Ladder](https://leetcode.com/problems/word-ladder/)

```python
from collections import deque

def bidirectional_bfs(graph, start, end):
    """양쪽에서 동시에 BFS — 탐색 공간 O(b^d) → O(2 * b^(d/2))로 감소"""
    if start == end:
        return 0
    
    # [Two Queues & Visited] ─────────────────────────────────
    #    WHY: 양쪽에서 탐색하면 탐색 공간이 제곱근으로 줄어듦
    queue_start = deque([start])
    queue_end = deque([end])
    visited_start = {start: 0}
    visited_end = {end: 0}
    
    while queue_start and queue_end:
        # [Expand Smaller Side] ─────────────────────────────────
        #    WHY: 작은 쪽을 확장해야 균형 잡힌 탐색 가능
        #    COMPLEXITY: 한쪽만 확장하면 양방향 장점 사라짐
        if len(queue_start) <= len(queue_end):
            result = expand(queue_start, visited_start, visited_end, graph)
        else:
            result = expand(queue_end, visited_end, visited_start, graph)
        
        if result != -1:
            return result
    
    return -1

def expand(queue, visited_self, visited_other, graph):
    current = queue.popleft()
    current_dist = visited_self[current]
    
    for neighbor in graph[current]:
        if neighbor not in visited_self:
            visited_self[neighbor] = current_dist + 1
            queue.append(neighbor)
            
            # [Meet in Middle] ─────────────────────────────────
            #    WHY: 반대쪽에서 이미 방문 = 경로 발견
            if neighbor in visited_other:
                return visited_self[neighbor] + visited_other[neighbor]
    
    return -1
```

### 변형 F: 다중 시작점 BFS
**상황**: 여러 시작점에서 동시에 BFS를 수행할 때 (예: 불이 여러 곳에서 번짐)
**핵심 변화**: 초기 큐에 모든 시작점을 한꺼번에 삽입
**추천 문제**: 
- [백준 7576 토마토](https://www.acmicpc.net/problem/7576)
- [백준 4179 불!](https://www.acmicpc.net/problem/4179)
- [백준 5427 불](https://www.acmicpc.net/problem/5427)

```python
from collections import deque

def multi_source_bfs(grid, sources):
    """모든 시작점에서 동시에 BFS — 각 칸까지의 최단 거리"""
    rows, cols = len(grid), len(grid[0])
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    
    # [Multi-source Init] ─────────────────────────────────
    #    WHY: 모든 시작점을 거리 0으로 초기화 → 동시에 퍼져나감
    #    ADAPT: 불 번지기, 바이러스 전파, 최단 거리 전처리
    dist = [[float('inf')] * cols for _ in range(rows)]
    queue = deque()
    
    for x, y in sources:
        queue.append((x, y))
        dist[x][y] = 0
    
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < rows and 0 <= ny < cols:
                if dist[nx][ny] == float('inf') and grid[nx][ny] != 1:
                    dist[nx][ny] = dist[x][y] + 1
                    queue.append((nx, ny))
    
    return dist
```

---

## 핵심 인사이트

### 왜 "큐에 넣을 때" 방문 처리하는가?
```python
# ❌ 잘못된 방식: 꺼낼 때 방문 처리
current = queue.popleft()
visited.add(current)  # 이미 같은 노드가 여러 번 큐에 들어감

# ✅ 올바른 방식: 넣을 때 방문 처리
if neighbor not in visited:
    visited.add(neighbor)  # 중복 삽입 원천 차단
    queue.append(neighbor)
```

### 시간/공간 복잡도
- **시간**: O(V + E) — 모든 정점과 간선을 한 번씩 탐색
- **공간**: O(V) — 큐 + visited

### BFS vs DFS 선택 기준
| 조건 | BFS | DFS |
|------|-----|-----|
| 최단 거리 필요 | ✅ | ❌ |
| 경로 존재 여부만 | ▲ | ✅ |
| 탐색 공간이 넓음 | ❌ (메모리) | ✅ |
| 탐색 공간이 깊음 | ✅ | ❌ (스택 오버플로우) |

## 암기 카드 (필수 4요소)

- **트리거 문장**
  - "가중치가 있는 최단 경로", "최소 비용"
  - "음수 간선 없음"
- **핵심 불변식**
  - 우선순위 큐에서 꺼낸 최소 비용 후보를 기준으로 완화(relax)하면 최단거리 수렴
  - 현재 기록 거리보다 큰 stale 항목은 버려도 정답 영향 없음
- **실수 포인트**
  - 힙 원소 순서 실수 `(node, cost)` / 음수 간선 문제에 오적용 / stale 체크 누락
- **템플릿 위치**
  - 이 문서의 `핵심 구조` 코드 블록

## 예제 문제 (입문 → 확장)

- 백준 1753 최단경로
- 백준 1916 최소비용 구하기
- 프로그래머스 배달

---

# Dijkstra Pattern Skeleton

> 생성일: 2026-01-26

## Why & What (이 패턴은 왜/무엇)
- **목적**: 가중치가 양수인 그래프에서 시작점으로부터 모든 정점까지의 최단 거리를 구합니다.
- **본질**: "현재까지 발견된 최단 거리가 가장 짧은 노드를 확정하고, 그 노드를 거쳐 갈 수 있는 주변 노드들의 거리를 갱신(Relaxation)한다."
- **장점**: BFS와 달리 가중치가 다른 간선을 처리하며, O(E log V) 시간 복잡도로 빠릅니다.

## When to Use (이럴 때 사용)
- `가중치 그래프`: 간선마다 비용(거리, 시간 등)이 다를 때
- `최단 경로`: 특정 지점에서 다른 지점으로 가는 최소 비용
- `음수 간선 없음`: 음수 가중치가 있으면 벨만-포드를 써야 함

## 핵심 구조

```python
import heapq

def dijkstra(graph, start):
    # 1. [Init Distance Table] ───────────────────────────
    #    역할: 시작점에서 각 노드까지의 최단 거리를 저장
    #    WHY: 처음엔 아무 경로도 모르므로 무한대(INF)로 초기화
    #    ADAPT: 노드 개수(N) 또는 범위에 맞춰 배열이나 딕셔너리 사용
    distances = {node: float('inf') for node in graph}
    distances[start] = 0  # 시작점의 거리는 0
    
    # 2. [Init Priority Queue] ────────────────────────────
    #    역할: 방문할 노드 예약 (비용 순 정렬)
    #    WHY: 비용이 가장 작은 간선부터 탐색해야 최적해 보장 (Greedy)
    #    PITFALL: (비용, 노드) 순서로 넣어야 비용 기준 정렬됨
    pq = []
    heapq.heappush(pq, (0, start))  # (cost, node)

    # 3. [Loop Priority Queue] ────────────────────────────
    #    역할: 최소 비용 노드 꺼내서 처리
    #    COMPLEXITY: 큐가 빌 때까지 반복. 모든 간선을 한 번씩 확인 -> O(E log V)
    while pq:
        
        # 4. [Pop Min Node] ──────────────────────────────
        #    역할: 가장 가까운 노드 선택
        #    WHY: min-heap이므로 O(log N)으로 최소값 추출
        curr_cost, curr_node = heapq.heappop(pq)

        # 5. [Lazy Discard] ──────────────────────────────
        #    역할: 이미 처리된(더 짧은 경로가 발견된) 노드 스킵
        #    WHY: 힙에는 같은 노드가 여러 번 들어갈 수 있음(갱신될 때마다).
        #         꺼낸 비용이 현재 기록된 최단 거리보다 크다면,
        #         이미 더 짧은 경로로 방문한 것이므로 무시해야 함.
        #    PITFALL: 이 처리가 없으면 시간 복잡도가 악화됨 O(E log E)
        if distances[curr_node] < curr_cost:
            continue

        # 6. [Relax Edges] ───────────────────────────────
        #    역할: 현재 노드를 거쳐가는 경로가 더 짧으면 갱신
        for neighbor, weight in graph[curr_node].items():
            new_cost = curr_cost + weight
            
            # 7. [Update Condition] ──────────────────────
            #    역할: 새로운 경로가 기존 경로보다 효율적인지 판단
            #    WHY: 더 적은 비용일 때만 갱신하고 큐에 추가
            #    PITFALL: < 가 아닌 <= 를 쓰면 무한 루프 가능성(0 가중치 등)
            if new_cost < distances[neighbor]:
                distances[neighbor] = new_cost
                heapq.heappush(pq, (new_cost, neighbor))
                
    return distances
```

## Customization Points
- `graph`: 인접 리스트(dict or list of lists) 형태여야 효율적
- `state`: 단순 노드 번호뿐만 아니라 `(y, x, direction)` 같은 복합 상태일 수 있음 (예: 경주로 건설)
- `distance structure`: 노드가 정수면 리스트, 문자열이나 희소하면 딕셔너리 사용

## Variations (응용 유형)

### 변형 A: 경로 역추적 (Path Reconstruction)
**상황**: 최단 거리 값만 필요한 게 아니라, 그 경로(어디를 거쳐왔는지)가 필요할 때
**핵심 변화**: 거리를 갱신할 때 `parent` 정보도 함께 저장

```python
    # [Init Parent]
    parent = {node: None for node in graph}
    
    # ... inside Relax loop ...
            if new_cost < distances[neighbor]:
                distances[neighbor] = new_cost
                parent[neighbor] = curr_node  # [Track] 어디서 왔는지 기록
                heapq.heappush(pq, (new_cost, neighbor))
    
    # [Reconstruct Path]
    # 도착점부터 parent를 타고 역으로 거슬러 올라감
```

### 변형 B: 2D 격자 / 상태 기반 다익스트라
**상황**: 맵 위에서 이동하며, 이동 방향이나 상태에 따라 비용이 달라질 때 (예: 프로그래머스 경주로 건설)
**핵심 변화**: 노드 하나가 `(y, x)`가 아니라 `(y, x, state)`가 됨. 거리 배열도 3차원 등으로 확장.

```python
    # [3D Distance Array]
    # distances[y][x][direction]
    costs = [[[INF] * 4 for _ in range(N)] for _ in range(N)]
    
    # ... loop ...
        # [State Push]
        # 큐에 다음 상태 정보(좌표, 방향 등)를 모두 넣음
        heapq.heappush(pq, (new_cost, ny, nx, new_dir))
```

### 변형 C: 최대 확률 / 병목 용량 (Max-Heap)
**상황**: 곱해서 최대가 되는 확률 구하기, 혹은 경로상 최소 너비의 최대화 등
**핵심 변화**: 기본 `heapq`는 min-heap이므로, 비용을 음수(`-prob`)로 넣어서 max-heap처럼 동작하게 함.

```python
    # [Max-Heap Trick]
    # 최대값을 먼저 꺼내야 하므로 부호를 반대로 넣음
    heapq.heappush(pq, (-prob, node))
    
    # [Pop]
    curr_prob, curr_node = heapq.heappop(pq)
    curr_prob = -curr_prob  # 다시 원래대로 복구
```

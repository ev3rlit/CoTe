# 전력망을 둘로 나누기

#완전탐색 #그래프 #트리 #알고리즘 #코딩테스트

# 문제 난이도 중

## 1. 📊 객관적 분석 및 근거

### 1.1 제약 조건 파악

| 항목 | 값 | 의미 |
|------|-----|------|
| n (송전탑 개수) | 2 ~ 100 | 노드 수가 매우 작음 → 완전탐색 가능 |
| wires 길이 | n-1 | 트리 구조 (사이클 없음) |
| 시간 제한 | - | 통상 1초 가정 |
| 메모리 제한 | - | 특별한 제약 없음 |

### 1.2 시간 복잡도 역산

**기준**: 1초 ≈ 10^8 연산

**완전탐색 분석**:
- 간선 개수: n-1개 (최대 99개)
- 각 간선을 끊었을 때: 두 서브트리의 노드 수 계산 필요
- 서브트리 노드 수 계산: BFS/DFS로 O(N)

| 복잡도 | N=100 | 가능 여부 |
|--------|-------|----------|
| O(N²) | 10,000 | ✅ 매우 여유로움 |
| O(N × E) | 100 × 99 ≈ 9,900 | ✅ 매우 여유로움 |

**전체 복잡도**: O(E × N) = 99 × 100 ≈ 1만 연산 → ✅ 통과

### 1.3 문제 패턴 인식

**핵심 질문**: 이 문제가 요구하는 것은 무엇인가?

| 관찰 포인트 | 이 문제에서 | 시사점 |
|-------------|-------------|--------|
| 자료구조 | 트리 (사이클 없는 연결 그래프) | 간선 하나 끊으면 두 컴포넌트로 분리 |
| 최적해 vs 모든 경우 | 두 서브트리 차이 최소화 (최적해) | 모든 간선 시도 후 최소 차이 선택 |
| 순서가 중요한가 | 아니오 | 끊는 간선만 선택하면 됨 |
| 입력 크기 | N ≤ 100 (작음) | 완전탐색 확정 |

### 1.4 알고리즘 선택 및 논증

#### 🎯 최종 선택: 완전탐색 + BFS/DFS

**선택 근거 (Why this algorithm?)**

1. **문제 구조와의 적합성**
   - 트리에서 간선 하나를 끊으면 정확히 두 개의 연결 컴포넌트 생성
   - 각 간선을 순회하며 끊었을 때 두 컴포넌트의 크기 차이 계산
   - 모든 경우 중 최소 차이 선택

2. **제약 조건 충족**
   - 시간 복잡도: O(E × N) → 최대 1만 연산 (✅ 통과)
   - 공간 복잡도: O(N) → 인접 리스트 및 방문 배열 (✅ 통과)

3. **핵심 인사이트**
   - 트리 구조이므로 간선 하나를 끊으면 반드시 두 컴포넌트로 분리
   - 한 쪽 컴포넌트의 노드 수를 알면 다른 쪽은 `n - count`로 계산 가능
   - 차이 = |count - (n - count)| = |2 × count - n|

#### ❌ 기각된 대안들

| 대안 | 복잡도 | 기각 이유 |
|------|--------|-----------|
| Union-Find | O(E × α(N)) | 가능하지만 간선 하나 제거 후 컴포넌트 크기 계산이 복잡 |
| 서브트리 크기 DP | O(N) | 더 효율적이지만 N ≤ 100이면 완전탐색으로 충분 |

#### 💡 비슷한 문제에서 이 패턴을 인식하는 법

- **키워드**: "트리", "간선 끊기", "두 그룹으로 나누기", "균등 분할"
- **문제 유형**: 트리 분할, 그래프 컴포넌트 분석
- **주의사항**:
    - 인접 리스트 구성 시 양방향 간선 추가 필수
    - 끊을 간선을 BFS/DFS에서 제외 처리 필요
    - 노드 번호가 1부터 시작하는지 0부터 시작하는지 확인

---

## 2. 🧠 자연어 실행 흐름

1. **그래프 구성**: wires 배열로 인접 리스트 생성 (양방향)
2. **모든 간선 순회**: 각 간선 (v1, v2)에 대해:
   - 해당 간선을 제외한 그래프에서 BFS/DFS 수행
   - v1에서 시작하여 방문 가능한 노드 수(count) 계산
3. **차이 계산**: |count - (n - count)| = |2 × count - n|
4. **최소값 갱신**: 현재 차이와 기존 최소값 비교
5. **결과 반환**: 모든 간선 탐색 후 최소 차이 반환

---

## 3. 💻 Code Implementation

(언어: Python)
```python
from collections import deque, defaultdict

def solution(n, wires):
    # 1. 인접 리스트 생성
    graph = defaultdict(list)
    for v1, v2 in wires:
        graph[v1].append(v2)
        graph[v2].append(v1)
    
    # 2. 특정 간선을 제외하고 한 쪽 컴포넌트의 노드 수 계산
    def count_nodes(start, exclude_v1, exclude_v2):
        visited = set([start])
        queue = deque([start])
        
        while queue:
            node = queue.popleft()
            for neighbor in graph[node]:
                # 끊을 간선인 경우 건너뜀
                if (node == exclude_v1 and neighbor == exclude_v2) or \
                   (node == exclude_v2 and neighbor == exclude_v1):
                    continue
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        
        return len(visited)
    
    # 3. 모든 간선을 끊어보며 최소 차이 탐색
    min_diff = float('inf')
    
    for v1, v2 in wires:
        # v1 쪽 컴포넌트의 노드 수
        count = count_nodes(v1, v1, v2)
        # 차이 계산: |count - (n - count)|
        diff = abs(2 * count - n)
        min_diff = min(min_diff, diff)
    
    return min_diff
```

**복잡도 분석**
- 시간: O(E × N) — 각 간선마다 BFS로 O(N) 탐색
- 공간: O(N) — 인접 리스트 및 visited 집합

---

## 4. 💻 DFS 버전 구현

BFS 대신 DFS(재귀)로 구현한 버전입니다.

```python
from collections import defaultdict

def solution_dfs(n, wires):
    # 1. 인접 리스트 생성
    graph = defaultdict(list)
    for v1, v2 in wires:
        graph[v1].append(v2)
        graph[v2].append(v1)
    
    # 2. DFS로 컴포넌트 노드 수 계산
    def dfs(node, visited, exclude_v1, exclude_v2):
        visited.add(node)
        count = 1
        
        for neighbor in graph[node]:
            # 끊을 간선인 경우 건너뜀
            if (node == exclude_v1 and neighbor == exclude_v2) or \
               (node == exclude_v2 and neighbor == exclude_v1):
                continue
            if neighbor not in visited:
                count += dfs(neighbor, visited, exclude_v1, exclude_v2)
        
        return count
    
    # 3. 모든 간선을 끊어보며 최소 차이 탐색
    min_diff = float('inf')
    
    for v1, v2 in wires:
        visited = set()
        count = dfs(v1, visited, v1, v2)
        diff = abs(2 * count - n)
        min_diff = min(min_diff, diff)
    
    return min_diff
```

**BFS vs DFS 비교**

| 항목 | BFS | DFS |
|------|-----|-----|
| 구현 방식 | 큐(deque) 사용 | 재귀 호출 |
| 코드 길이 | 약간 김 | 더 간결함 |
| 스택 오버플로우 | 없음 | N이 크면 위험 (N≤100은 안전) |
| 시간 복잡도 | O(N) | O(N) |
| 선호 상황 | 최단 경로 문제 | 단순 연결 컴포넌트 탐색 |

이 문제에서는 N ≤ 100이므로 DFS 재귀도 안전하게 사용 가능합니다.

---

# 평가

## 개선할 점
- **set 비교 방식 개선**: `exclude == set([node, neighbor])` 대신 `{node, neighbor} == exclude` 또는 `frozenset` 사용이 더 효율적입니다. `set([...])` 생성은 매번 새 객체를 만들어 오버헤드가 발생합니다.
- **함수명 명확화**: `diff_network`보다 `calculate_component_diff` 또는 `get_split_difference`가 함수의 역할을 더 명확히 드러냅니다.
- **차이 계산 간소화**: `abs(count - (n - count))`는 `abs(2 * count - n)`과 동일합니다. 후자가 연산이 한 번 적습니다.
- **조건 순서 최적화**: 끊어진 간선 체크를 방문 체크보다 먼저 하면, set 비교를 먼저 거르고 visited 체크를 나중에 할 수 있습니다.

## 잘한 점
- **상세한 사고 과정 주석**: 코드 상단의 1~18줄에 걸친 주석이 문제 분석과 알고리즘 설계 과정을 잘 보여줍니다.
- **함수 분리**: `diff_network`를 별도 함수로 분리하여 테스트와 디버깅이 용이합니다.
- **중첩 함수 활용**: `dfs`를 내부 함수로 정의하여 `visited`를 클로저로 공유, 불필요한 파라미터 전달을 줄였습니다.
- **set으로 간선 제외 처리**: 양방향 간선을 간단하게 처리하는 좋은 아이디어입니다.

## 다른 응용 방안
- **네트워크 분할 문제**: 서버 클러스터를 두 그룹으로 나누기
- **그래프 컷**: 최소 비용으로 그래프를 분할하는 문제
- **조직도 분할**: 팀을 두 그룹으로 균등 분배

## 추천 문제
- **백준 11724: 연결 요소의 개수** — DFS로 컴포넌트 카운팅
- **백준 1991: 트리 순회** — 트리 DFS 기초
- **프로그래머스: 네트워크** — 연결 컴포넌트 탐색
- **백준 2606: 바이러스** — 연결된 노드 수 세기

## 종합 평가
트리 구조에서 간선을 끊어 두 컴포넌트로 분할하는 핵심 아이디어를 정확히 파악했습니다.
주석에서 "시간복잡도 측정하는 방법을 몰라서"라고 적었는데, 이 문제의 복잡도는 O(E × N) = O(N²)로 분석할 수 있습니다.
디버깅 과정에서 `if neighbor not in visited`를 `if neighbor in visited`로 수정한 경험은 
**조건문 논리를 꼼꼼히 검토하는 습관**의 중요성을 보여줍니다.
전체적으로 DFS 패턴을 잘 이해하고 적용한 풀이입니다.

---

# 변형 문제: 일반 그래프에서 컴포넌트 분석

## 문제 상황
트리가 아닌 **일반 그래프**(사이클이 있을 수 있음)에서 간선 하나를 제거했을 때:
- 컴포넌트 개수가 몇 개인지?
- 각 컴포넌트의 노드 수는 얼마인지?

## 트리 vs 일반 그래프 비교

| 상황 | 트리 | 일반 그래프 (사이클 존재) |
|------|------|-------------------------|
| 간선 제거 시 결과 | **항상 2개** 컴포넌트 | **1개 또는 2개** 컴포넌트 |
| 분석 방법 | 한 쪽에서 DFS만 하면 됨 | 모든 노드 순회하며 DFS 필요 |
| 컴포넌트 수 세기 | 불필요 (항상 2개) | **필요** |

## 해결 방법

모든 노드를 순회하면서 **미방문 노드를 발견할 때마다** 새로운 컴포넌트로 카운트합니다.

```python
from collections import defaultdict

def analyze_components(n, graph, exclude_edge=None):
    """
    n: 노드 개수
    graph: 인접 리스트
    exclude_edge: 제외할 간선 (v1, v2) 또는 None
    
    Returns: 
        - 컴포넌트 개수
        - 각 컴포넌트의 노드 개수 리스트
    """
    visited = set()
    components = []  # 각 컴포넌트의 노드 수를 저장
    
    def dfs(node):
        visited.add(node)
        count = 1
        
        for neighbor in graph[node]:
            # 제외할 간선 처리
            if exclude_edge:
                if {node, neighbor} == set(exclude_edge):
                    continue
            
            if neighbor not in visited:
                count += dfs(neighbor)
        
        return count
    
    # 핵심: 모든 노드를 순회하면서 미방문 노드 발견 시 DFS
    for node in range(1, n + 1):  # 노드가 1부터 시작하는 경우
        if node not in visited and node in graph:
            component_size = dfs(node)
            components.append(component_size)
    
    return len(components), components


# 변형 문제용 solution
def solution_general_graph(n, edges):
    """일반 그래프에서 간선 제거 후 정확히 2개 컴포넌트가 되는 경우의 최소 차이"""
    graph = defaultdict(list)
    for v1, v2 in edges:
        graph[v1].append(v2)
        graph[v2].append(v1)
    
    min_diff = float('inf')
    valid_count = 0  # 정확히 2개로 나뉘는 경우의 수
    
    for v1, v2 in edges:
        num_components, sizes = analyze_components(n, graph, (v1, v2))
        
        # 컴포넌트가 정확히 2개인 경우만 유효
        if num_components == 2:
            diff = abs(sizes[0] - sizes[1])
            min_diff = min(min_diff, diff)
            valid_count += 1
        # else: 사이클 때문에 여전히 1개인 경우
    
    print(f"정확히 2개로 나뉘는 경우: {valid_count}/{len(edges)}")
    return min_diff if min_diff != float('inf') else -1
```

## 이 패턴이 필요한 문제들
- **백준 11724: 연결 요소의 개수** — 그래프의 컴포넌트 수 세기
- **프로그래머스: 네트워크** — 컴퓨터 네트워크 수 세기
- **백준 2606: 바이러스** — 특정 노드와 연결된 컴포넌트 크기

## 핵심 인사이트
처음에 생각했던 "모든 노드를 순회하며 컴포넌트 분석" 방식이 **더 일반적인 해법**입니다.
트리의 특성(간선 제거 시 항상 2개 분리)을 활용하면 최적화할 수 있지만,
일반 그래프에서는 "모든 노드 순회" 방식이 필수입니다.

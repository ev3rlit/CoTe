# DFS/백트래킹 패턴 스타일 가이드

> 깊이 우선 탐색 (Depth-First Search) 및 백트래킹 구현 스타일

---

## 사용 시점

다음 키워드가 보이면 DFS/백트래킹을 고려:

- **모든 경우의 수** 탐색
- **조합/순열** 생성
- **경로 찾기** (최단 아님)
- **연결 요소** 탐색
- **부분집합** 생성
- N이 작을 때 (**N ≤ 20**)

---

## 핵심 패턴

### 기본 백트래킹 템플릿

```python
def solution(data):
    n = len(data)
    visited = [False] * n
    result = [0]  # mutable 객체로 결과 저장

    def dfs(depth, current_value):
        # 종료 조건
        if depth == target_depth:
            result[0] = max(result[0], current_value)
            return

        # 모든 선택지 탐색
        for i in range(n):
            if visited[i]:
                continue

            # 선택
            visited[i] = True

            # 재귀 호출
            dfs(depth + 1, current_value + data[i])

            # 선택 해제 (백트래킹)
            visited[i] = False

    dfs(0, 0)
    return result[0]
```

---

## 변수 네이밍

| 용도 | 변수명 | 예시 |
|------|--------|------|
| 탐색 깊이 | `depth` | `dfs(depth + 1, ...)` |
| 현재 값/합 | `current_sum`, `current_value` | `current_sum + ability[i][depth]` |
| 방문 체크 | `visited` | `visited = [False] * n` |
| 결과 저장 | `result`, `max_value` | `result[0] = max(...)` |
| 현재 노드 | `node`, `cur` | `def dfs(node, depth)` |
| 이웃 노드 | `neighbor` | `for neighbor in graph[node]` |

---

## 방문 처리 패턴

### 리스트 방식 (인덱스 기반)

```python
visited = [False] * n

# 방문 처리
visited[i] = True
dfs(...)
visited[i] = False  # 백트래킹
```

### 그래프 탐색 (노드 기반)

```python
visited = [False] * N

def dfs(node, depth):
    if depth == target:
        return True

    for neighbor in graph[node]:
        if not visited[neighbor]:
            visited[neighbor] = True
            if dfs(neighbor, depth + 1):
                return True
            visited[neighbor] = False

    return False
```

---

## 결과 저장 패턴

### mutable 객체 사용 (권장)

```python
max_ability = [0]  # 리스트로 감싸서 내부 함수에서 수정 가능

def dfs(depth, current_sum):
    if depth == target:
        max_ability[0] = max(max_ability[0], current_sum)
        return
```

### nonlocal 사용

```python
answer = 0

def dfs(depth, current_sum):
    nonlocal answer
    if depth == target:
        answer = max(answer, current_sum)
        return
```

---

## 백트래킹 구조

### 선택 - 탐색 - 해제 패턴

```python
for i in range(n):
    if visited[i]:
        continue

    # 1. 선택 (방문 처리)
    visited[i] = True

    # 2. 탐색 (재귀 호출)
    dfs(depth + 1, current + data[i])

    # 3. 해제 (백트래킹)
    visited[i] = False
```

### 가지치기 (Pruning)

```python
def dfs(depth, current_sum):
    # 가지치기: 남은 것 다 더해도 최댓값 못 넘으면 종료
    if current_sum + remaining_max <= result[0]:
        return

    # 종료 조건
    if depth == target:
        result[0] = max(result[0], current_sum)
        return
```

---

## 종료 조건 패턴

### 깊이 기반 종료

```python
def dfs(depth, ...):
    # 목표 깊이 도달
    if depth == target_depth:
        # 결과 처리
        return
```

### 조건 기반 조기 종료

```python
def dfs(node, depth):
    # 목표 도달 시 즉시 True 반환
    if depth == 5:
        return True

    for neighbor in graph[node]:
        if dfs(neighbor, depth + 1):
            return True  # 찾으면 즉시 종료

    return False
```

---

## 그래프 DFS 패턴

### 인접 리스트 탐색

```python
from collections import defaultdict

graph = defaultdict(list)
for a, b in edges:
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * N

def dfs(node, depth):
    for neighbor in graph[node]:
        if not visited[neighbor]:
            visited[neighbor] = True
            dfs(neighbor, depth + 1)
            visited[neighbor] = False
```

### 모든 시작점 탐색

```python
# 모든 노드에서 DFS 시작
for start in range(N):
    visited[start] = True
    if dfs(start, 1):
        return True
    visited[start] = False
```

---

## 체육대회 스타일 (선택 문제)

N명 중 K명을 선택해서 최댓값 찾기:

```python
def solution(ability):
    students = len(ability)
    sports = len(ability[0])
    visited = [False] * students
    max_ability = [0]

    def dfs(depth, current_sum):
        # 종목 수만큼 선택 완료
        if depth == sports:
            max_ability[0] = max(max_ability[0], current_sum)
            return

        # 모든 학생 순회
        for i in range(students):
            if visited[i]:
                continue

            visited[i] = True
            dfs(depth + 1, current_sum + ability[i][depth])
            visited[i] = False

    dfs(0, 0)
    return max_ability[0]
```

---

## 체크리스트

구현 시 확인할 항목:

- [ ] 종료 조건이 명확한가?
- [ ] 방문 처리 후 **반드시** 해제하는가? (백트래킹)
- [ ] 결과 저장 방식이 올바른가? (mutable 또는 nonlocal)
- [ ] 가지치기 조건이 있다면 정확한가?
- [ ] 시작점에서 방문 처리를 했는가?
- [ ] 재귀 깊이 제한 필요한가? (`sys.setrecursionlimit`)

---

## 재귀 깊이 설정

백준 등에서 재귀 깊이 제한 필요시:

```python
import sys
sys.setrecursionlimit(10000)
```

---

## 관련 문제 유형

| 유형 | 특징 |
|------|------|
| 체육대회 | N명 중 K명 선택, 최댓값 |
| ABCDE | 그래프에서 깊이 5 경로 찾기 |
| 피로도 | 순열 + 조건부 선택 |
| N-Queen | 백트래킹 + 가지치기 |

---

## 참고

- `/GEMINI.md` - 전체 스타일 가이드
- `/완전탐색/GEMINI.md` - 완전탐색 패턴

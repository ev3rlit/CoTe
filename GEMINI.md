# GEMINI.md - 코딩 테스트 풀이 스타일 가이드

> Gemini AI가 코드 작성 시 참고하는 개인 풀이 스타일 문서

---

## 기본 원칙

| 항목 | 규칙 |
|------|------|
| 언어 | Python 3 |
| 문서화 | 한국어 |
| 라이브러리 | 표준 라이브러리만 사용 (collections, itertools, heapq, bisect) |
| 외부 의존성 | 없음 (순수 Python 구현) |

---

## 변수 네이밍 규칙

### 좌표 및 크기

| 용도 | 변수명 | 예시 |
|------|--------|------|
| 좌표 | `y, x` | `y, x = 0, 0` |
| 다음 좌표 | `ny, nx` | `ny, nx = y + dy, x + dx` |
| 방향 델타 | `dy, dx` | `dy, dx = directions[i]` |
| 그리드 크기 | `height, width` | `height, width = len(grid), len(grid[0])` |
| 행/열 개수 | `rows, cols` | `rows, cols = len(board), len(board[0])` |
| 노드 개수 | `N`, `n` | `N = len(nodes)` |

### 결과 및 상태

| 용도 | 변수명 | 예시 |
|------|--------|------|
| 결과값 | `answer`, `result` | `return answer` |
| 방문 체크 | `visited` | `visited = set()` |
| BFS 큐 | `queue` | `queue = deque([start])` |
| DFS 스택 | `stack` | `stack = [start]` |
| 이동 횟수 | `moves`, `dist` | `moves + 1` |
| 현재 값 | `current`, `cur` | `current = queue.popleft()` |

### DP 관련

| 용도 | 변수명 | 예시 |
|------|--------|------|
| DP 테이블 | `dp` | `dp = [row[:] for row in triangle]` |
| 이전 상태 | `prev1, prev2` | `prev2, prev1 = prev1, max(...)` |
| 누적 합 | `current_sum` | `current_sum + value` |

---

## 자료구조 선택 기준

### 상황별 자료구조

| 상황 | 자료구조 | 코드 |
|------|----------|------|
| 빈도수 카운팅 | `defaultdict(int)` | `counts = defaultdict(int)` |
| 그룹핑/인접 리스트 | `defaultdict(list)` | `graph = defaultdict(list)` |
| 방문 처리 (좌표) | `set()` with tuple | `visited = set(); visited.add((y,x))` |
| 방문 처리 (인덱스) | `list` | `visited = [False] * N` |
| BFS 큐 | `deque` | `from collections import deque` |
| 스택 | `list` | `stack = []` |
| 우선순위 큐 | `heapq` | `import heapq` |
| 중복 제거 | `set()` | `candidates = set()` |

### Import 패턴

```python
# 가장 자주 사용하는 import
from collections import deque
from collections import defaultdict
from itertools import permutations, combinations
import heapq
```

---

## 코드 구조 패턴

### 기본 구조

```python
def solution(input_data):
    # 1. 초기화
    # - 변수 선언
    # - 크기 계산

    # 2. 전처리 (필요시)
    # - 데이터 변환
    # - 그래프/맵 구성

    # 3. 메인 로직
    # - 알고리즘 수행

    # 4. 결과 반환
    return answer
```

### 헬퍼 함수 패턴

```python
def solution(data):
    # 외부 변수 참조를 위해 solution 내부에 정의
    def helper(param):
        # nonlocal 또는 mutable 객체로 상태 공유
        return result

    # 헬퍼 함수 호출
    return helper(initial_value)
```

---

## 주석 스타일

### 원칙

1. **한국어**로 작성
2. 알고리즘 **설계 단계**부터 주석으로 기록
3. **실행 흐름**을 단계별로 명시
4. 입력 크기/제약 조건을 **상단에 명시**

### 예시

```python
# 입력 크기는 100 * 100 이므로 최대 1만
# 목표는?  위치 G로 이동하는데 최소 움직임
# BFS로 탐색, 각 경우마다 방문 여부 필요

# 실행 흐름
# 1. 초기화
# - 보드에서 시작점 R과 G의 좌표를 확인
# - BFS 큐에 ((시작위치), 이동횟수)
# - 방문 set[(y,x)]에 시작점을 방문처리
# 2. 큐가 비어있을때 까지 순회
# 3. 현재 상태 pop
# 4. 현재 위치가 목표 위치면 현재 이동 횟수 반환
# 5. 4방향 탐색
# - 조건 확인 후 큐에 추가
```

---

## 방향 벡터 패턴

### 4방향 (상하좌우)

```python
# 방식 1: 튜플 리스트
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# 방식 2: 이름 있는 방향 (문제에서 방향 키워드 사용시)
directions = {'N': (-1, 0), 'E': (0, 1), 'S': (1, 0), 'W': (0, -1)}

# 사용
for dy, dx in directions:
    ny, nx = y + dy, x + dx
```

### 8방향 (대각선 포함)

```python
directions = [
    (-1, 0), (1, 0), (0, -1), (0, 1),  # 상하좌우
    (-1, -1), (-1, 1), (1, -1), (1, 1)  # 대각선
]
```

---

## 범위 체크 패턴

### 그리드 경계 확인

```python
# 방식 1: 복합 조건
if 0 <= ny < height and 0 <= nx < width:
    # 유효한 좌표

# 방식 2: 헬퍼 함수
def is_valid(y, x):
    return 0 <= y < height and 0 <= x < width

# 방식 3: 벽 포함 체크 (리코쳇 로봇 스타일)
def is_wall(y, x):
    if y < 0 or y >= height:
        return True
    if x < 0 or x >= width:
        return True
    if board[y][x] == 'D':
        return True
    return False
```

---

## 정렬 패턴

### 다중 키 정렬

```python
# 튜플 + lambda: 첫 번째 키 내림차순, 두 번째 키 오름차순
items.sort(key=lambda x: (-x[1], x[0]))

# dict 정렬
sorted_items = sorted(dict.items(), key=lambda x: x[1], reverse=True)
```

---

## 알고리즘별 스타일 가이드

각 알고리즘 폴더의 GEMINI.md를 참조:

| 폴더 | 내용 |
|------|------|
| `/BFS/GEMINI.md` | BFS 패턴 (방향벡터, 방문처리, 큐 사용법) |
| `/DFS/GEMINI.md` | DFS/백트래킹 패턴 (재귀, 방문처리, 가지치기) |
| `/DP/GEMINI.md` | 다이나믹 프로그래밍 패턴 (1D/2D DP, 상태 정의, 원형 배열) |
| `/구현/GEMINI.md` | 시뮬레이션/구현 패턴 (방향 이동, 시간 기반 처리) |
| `/그래프/GEMINI.md` | 그래프 탐색 패턴 (인접 리스트, 경로 탐색) |
| `/완전탐색/GEMINI.md` | 완전탐색 패턴 (itertools, 백트래킹, 소수 판별) |

---

## 자주 사용하는 코드 스니펫

### 시작점 찾기 (그리드)

```python
for y in range(height):
    for x in range(width):
        if board[y][x] == 'S':
            start = (y, x)
            break
```

### defaultdict 카운팅

```python
from collections import defaultdict

counts = defaultdict(int)
for item in items:
    counts[item] += 1
```

### 그래프 인접 리스트 구성

```python
graph = defaultdict(list)
for a, b in edges:
    graph[a].append(b)
    graph[b].append(a)  # 무방향 그래프
```

### 2D 배열 복사

```python
# 깊은 복사
dp = [row[:] for row in original]
```

---

## 피해야 할 패턴

| 피해야 할 것 | 대신 사용할 것 |
|--------------|----------------|
| `[[0] * cols] * rows` (얕은 복사) | `[[0] * cols for _ in range(rows)]` |
| `from math import *` | 필요한 것만 import |
| 불명확한 변수명 (`tmp`, `num`) | 의미 있는 이름 (`next_pos`, `count`) |
| 영어 주석 | 한국어 주석 |

---

## 참고

- `/SOLVING.md` - 문제 풀이 가이드
- `/_learning/` - 알고리즘 패턴 학습 자료
- `/CLAUDE.md` - 저장소 가이드

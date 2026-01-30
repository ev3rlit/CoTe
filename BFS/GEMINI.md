# BFS 패턴 스타일 가이드

> 너비 우선 탐색 (Breadth-First Search) 구현 스타일

---

## 사용 시점

다음 키워드가 보이면 BFS를 고려:

- **최단 거리** / **최소 이동 횟수**
- **미로 탈출** / **게임 맵**
- **레벨 순서** 탐색
- **가까운 것부터** 찾기
- 가중치가 **동일한** 그래프에서의 탐색

---

## 핵심 패턴

### 기본 BFS 템플릿

```python
from collections import deque

def solution(board):
    height, width = len(board), len(board[0])

    # 시작점 찾기
    start = (0, 0)
    goal = (0, 0)
    for y in range(height):
        for x in range(width):
            if board[y][x] == 'R':
                start = (y, x)
            elif board[y][x] == 'G':
                goal = (y, x)

    # 방향 벡터 (상, 하, 좌, 우)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # BFS 초기화
    # 큐에는 ((y, x), 이동횟수) 형태로 저장
    queue = deque([(start, 0)])
    visited = set([start])

    while queue:
        (y, x), moves = queue.popleft()

        # 목표 도달 체크
        if (y, x) == goal:
            return moves

        # 4방향 탐색
        for dy, dx in directions:
            ny, nx = y + dy, x + dx

            # 범위 체크
            if not (0 <= ny < height and 0 <= nx < width):
                continue

            # 벽 체크
            if board[ny][nx] == 'D':
                continue

            # 방문 체크
            if (ny, nx) in visited:
                continue

            # 방문 처리 및 큐에 추가
            visited.add((ny, nx))
            queue.append(((ny, nx), moves + 1))

    return -1  # 도달 불가
```

---

## 변수 네이밍

| 용도 | 변수명 | 예시 |
|------|--------|------|
| 현재 좌표 | `y, x` | `y, x = queue.popleft()` |
| 다음 좌표 | `ny, nx` | `ny, nx = y + dy, x + dx` |
| 방향 델타 | `dy, dx` | `for dy, dx in directions` |
| 그리드 크기 | `height, width` | `height, width = len(board), len(board[0])` |
| 이동 횟수 | `moves` | `moves + 1` |
| 방문 체크 | `visited` | `visited = set()` |
| BFS 큐 | `queue` | `queue = deque()` |

---

## 방향 벡터

### 4방향 (상하좌우)

```python
# 기본 형태
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# 주석 포함
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # 북 동 남 서
```

### 문자열 방향 매핑

```python
directions = {'N': (-1, 0), 'E': (0, 1), 'S': (1, 0), 'W': (0, -1)}
```

---

## 방문 처리 패턴

### set 사용 (좌표 튜플)

```python
visited = set()
visited.add((y, x))

# 초기화 시 시작점 포함
visited = set([start])

# 체크
if (ny, nx) in visited:
    continue
```

### 2D 배열 사용

```python
visited = [[False] * width for _ in range(height)]
visited[y][x] = True

if visited[ny][nx]:
    continue
```

---

## 범위 체크 패턴

### 인라인 조건

```python
if not (0 <= ny < height and 0 <= nx < width):
    continue
```

### 헬퍼 함수 (벽 포함)

```python
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

## 변형 패턴

### 슬라이딩 BFS (리코쳇 로봇 스타일)

벽에 부딪힐 때까지 미끄러지는 경우:

```python
for dy, dx in directions:
    # 현재 위치에서 슬라이딩
    ny, nx = y, x

    # 벽에 부딪히기 전까지 이동
    while not is_wall(ny + dy, nx + dx):
        ny += dy
        nx += dx

    # 이동이 없는 경우 무시
    if (ny, nx) == (y, x):
        continue

    # 방문 체크 및 큐 추가
    if (ny, nx) not in visited:
        visited.add((ny, nx))
        queue.append(((ny, nx), moves + 1))
```

### 다중 시작점 BFS

```python
# 모든 시작점을 큐에 초기화
queue = deque()
visited = set()

for y in range(height):
    for x in range(width):
        if board[y][x] == 'S':
            queue.append(((y, x), 0))
            visited.add((y, x))
```

### 상태 포함 BFS

추가 상태가 필요한 경우 (예: 열쇠 수집):

```python
# 상태: (y, x, 추가정보)
queue = deque([((y, x, state), 0)])
visited = set([(y, x, state)])
```

---

## 큐 상태 저장 형식

### 기본 형태

```python
# ((y, x), moves) - 좌표와 이동횟수 분리
queue = deque([(start, 0)])
(y, x), moves = queue.popleft()
```

### 튜플 플랫 형태

```python
# (y, x, moves) - 하나의 튜플로
queue = deque([(y, x, 0)])
y, x, moves = queue.popleft()
```

---

## 체크리스트

구현 시 확인할 항목:

- [ ] `deque` import 했는가?
- [ ] 시작점을 `visited`에 추가했는가?
- [ ] 방향 벡터가 올바른가? (y가 행, x가 열)
- [ ] 범위 체크: `0 <= ny < height and 0 <= nx < width`
- [ ] 큐에 넣을 때 방문 처리 (꺼낼 때 X)
- [ ] 목표 도달 시 즉시 반환
- [ ] 도달 불가 시 `-1` 반환

---

## 관련 문제 유형

| 유형 | 특징 |
|------|------|
| 미로 탐색 | 기본 BFS, 최단 경로 |
| 토마토 | 다중 시작점 BFS |
| 리코쳇 로봇 | 슬라이딩 BFS |
| 벽 부수기 | 상태 포함 BFS |
| 숨바꼭질 | 0-1 BFS |

---

## 참고

- `/_learning/BFS/skeleton.md` - 상세 BFS 스켈레톤
- `/GEMINI.md` - 전체 스타일 가이드

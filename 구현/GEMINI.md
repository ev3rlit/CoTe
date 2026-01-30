# 구현/시뮬레이션 패턴 스타일 가이드

> 시뮬레이션 및 구현 문제 스타일

---

## 사용 시점

다음 특징이 보이면 구현/시뮬레이션을 고려:

- **규칙대로 시뮬레이션** 수행
- **상태 변화**를 추적
- 특별한 알고리즘보다 **정확한 구현**이 핵심
- **방향 이동**, **시간 기반 처리**
- 조건이 많고 **예외 처리**가 필요

---

## 핵심 패턴

### 기본 시뮬레이션 템플릿

```python
def solution(data, commands):
    # 1. 값 초기화
    # - 상태 변수 설정
    # - 시작 위치/값 확인

    # 2. 명령/이벤트 순회
    for command in commands:
        # - 조건 확인
        # - 상태 업데이트
        # - 예외 처리
        pass

    # 3. 최종 결과 반환
    return result
```

---

## 변수 네이밍

| 용도 | 변수명 | 예시 |
|------|--------|------|
| 현재 좌표 | `current_y, current_x` | `current_y, current_x = y, x` |
| 다음 좌표 | `ny, nx` | `ny, nx = current_y + dy, current_x + dx` |
| 방향 정보 | `direction`, `dir_y, dir_x` | `dir_y, dir_x = directions[direction]` |
| 그리드 크기 | `width, height` | `width, height = len(park[0]), len(park)` |
| 이동 횟수 | `steps` | `steps = int(steps_str)` |
| 플래그 | `found_obstacle` | `found_obstacle = False` |

---

## 방향 이동 패턴

### 방향 딕셔너리 (문자열 키)

```python
# 북동남서 좌표계 (y, x)
directions = {
    'N': (-1, 0),
    'E': (0, 1),
    'S': (1, 0),
    'W': (0, -1)
}

# 사용
dir_y, dir_x = directions[direction]
ny, nx = current_y + dir_y * steps, current_x + dir_x * steps
```

### 방향 리스트 (인덱스 기반)

```python
# 상우하좌 (시계방향)
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

# 방향 전환
direction = (direction + 1) % 4  # 오른쪽 회전
direction = (direction - 1) % 4  # 왼쪽 회전
direction = (direction + 2) % 4  # 180도 회전
```

---

## 시작점 찾기 패턴

```python
width, height = len(park[0]), len(park)
current_x, current_y = 0, 0

for y in range(height):
    for x in range(width):
        if park[y][x] == 'S':
            current_y, current_x = y, x
            break
```

---

## 명령 파싱 패턴

### map + str.split 사용

```python
# routes = ["E 2", "S 3", "W 1"]
for direction, steps_str in map(str.split, routes):
    steps = int(steps_str)
    dir_y, dir_x = directions[direction]
```

### 직접 파싱

```python
for route in routes:
    direction, steps = route.split()
    steps = int(steps)
```

---

## 범위 및 장애물 체크 패턴

### 최종 위치 범위 체크

```python
ny, nx = current_y + dir_y * steps, current_x + dir_x * steps

if not (0 <= ny < height and 0 <= nx < width):
    continue  # 명령 무시
```

### 이동 경로 장애물 체크

```python
found_obstacle = False
for s in range(1, steps + 1):
    temp_y = current_y + dir_y * s
    temp_x = current_x + dir_x * s

    # 범위 체크
    if not (0 <= temp_y < height and 0 <= temp_x < width):
        found_obstacle = True
        break

    # 장애물 체크
    if park[temp_y][temp_x] == 'X':
        found_obstacle = True
        break

if found_obstacle:
    continue  # 명령 무시
```

---

## 공원 산책 스타일

전체 구현 예시:

```python
def solution(park, routes):
    # 방향 정의
    directions = {'N': (-1, 0), 'E': (0, 1), 'S': (1, 0), 'W': (0, -1)}

    # 1. 초기화
    width, height = len(park[0]), len(park)
    current_x, current_y = 0, 0
    for y in range(height):
        for x in range(width):
            if park[y][x] == 'S':
                current_y, current_x = y, x
                break

    # 2. 명령 순회
    for direction, steps_str in map(str.split, routes):
        steps = int(steps_str)
        dir_y, dir_x = directions[direction]
        ny, nx = current_y + dir_y * steps, current_x + dir_x * steps

        # 범위 체크
        if not (0 <= ny < height and 0 <= nx < width):
            continue

        # 경로 장애물 체크
        found_obstacle = False
        for s in range(1, steps + 1):
            temp_y = current_y + dir_y * s
            temp_x = current_x + dir_x * s
            if park[temp_y][temp_x] == 'X':
                found_obstacle = True
                break

        if found_obstacle:
            continue

        # 이동
        current_y, current_x = ny, nx

    # 3. 결과 반환
    return [current_y, current_x]
```

---

## 시간 기반 처리 패턴

### 시간 순회

```python
for time in range(total_time):
    # 이벤트 처리
    if time in events:
        process_event(events[time])

    # 상태 업데이트
    update_state()
```

### 타임스탬프 이벤트

```python
# 이벤트를 시간순으로 정렬 후 처리
events.sort(key=lambda x: x[0])  # 시간 기준 정렬

for time, action in events:
    # 이전 시간까지의 상태 업데이트
    process_until(time)
    # 현재 이벤트 처리
    apply_action(action)
```

---

## 주석 스타일 예시

```python
# 명령 대로 처리하지만, 2가지를 만족하지 않는 경우 해당 명령은 무시됨
# 좌표는 0 base
# 공원 그리드와 명령이 배열로 제공

# 주어진 방향으로 이동할때 공원을 벗어나는지 확인
# 주어진 방향으로 이동중 장애물을 만나는지 확인

# 1. 값 초기화
# - 시작 위치 확인
# - 현재 위치 초기화
# 2. routes 순회
# - 이동한 위치가 범위 안에 있는지 확인
# - 이동한 위치 사이에 장애물 확인
# - 두 조건을 만족하면 이동
# 3. 최종 좌표 반환
```

---

## 체크리스트

구현 시 확인할 항목:

- [ ] 좌표계가 명확한가? (y가 행, x가 열)
- [ ] 방향 벡터가 좌표계와 일치하는가?
- [ ] 범위 체크: `0 <= ny < height and 0 <= nx < width`
- [ ] 장애물 체크 시 **경로 전체**를 확인했는가?
- [ ] 예외 케이스 처리했는가? (이동 없음, 범위 초과)
- [ ] 명령 무시 조건이 정확한가?

---

## 관련 문제 유형

| 유형 | 특징 |
|------|------|
| 공원 산책 | 방향 이동 + 장애물 체크 |
| 붕대 감기 | 시간 기반 상태 관리 |
| 로봇 청소기 | 방향 전환 + 시뮬레이션 |
| 뱀 | 큐를 이용한 상태 관리 |
| 경주로 건설 | BFS + 방향 상태 |

---

## 참고

- `/GEMINI.md` - 전체 스타일 가이드

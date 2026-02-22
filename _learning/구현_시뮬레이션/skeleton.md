# 구현 & 시뮬레이션 Pattern Skeleton

> 생성일: 2026-01-14

// [Implementation & Simulation Pattern]
// 문제에서 주어진 규칙/조건을 그대로 코드로 옮기는 패턴

---

## 암기 카드 (필수 4요소)

- **트리거 문장**
  - "규칙대로 진행", "시뮬레이션", "격자/방향/회전"
- **핵심 불변식**
  - 한 스텝의 상태 전이가 문제 규칙과 1:1로 대응되어야 한다
  - 동시 업데이트 문제는 next 배열 분리로 순서 의존 버그를 막는다
- **실수 포인트**
  - 좌표계 혼동 / 경계 체크 누락 / 종료 조건 부재 / in-place 갱신 버그
- **템플릿 위치**
  - 이 문서의 `핵심 구조` 코드 블록

## 예제 문제 (입문 → 확장)

- 프로그래머스 공원 산책
- 백준 14503 로봇 청소기
- 프로그래머스 프렌즈4블록

---

## Why & What (이 패턴은 왜/무엇)

- **목적**: 복잡한 조건/규칙을 정확하게 코드로 변환하여 시뮬레이션
- **본질**: "문제가 시키는 대로 정확히 따라한다"
- **장점**: 알고리즘 지식보다 **구현력**과 **디버깅 능력**이 핵심. 문제 이해만 정확하면 풀 수 있음

## When to Use (이럴 때 사용)

문제에서 다음 키워드가 보이면 이 패턴을 떠올리세요:

- `시뮬레이션`: "~한 과정을 반복한다", "~할 때까지 수행"
- `구현`: 특별한 알고리즘 없이 조건이 복잡한 문제
- `방향 전환`: "위/아래/좌/우로 이동", "시계/반시계 회전"
- `격자/보드`: 2D 배열에서 규칙에 따라 움직이는 문제
- `상태 변화`: 시간에 따라 상태가 변하는 문제

---

## 핵심 구조

```python
# ============================================================
# 1. [State Definition] ─────────────────────────────────
#    역할: 시뮬레이션에 필요한 상태 변수 정의
#    ADAPT: 문제에서 "추적해야 하는 것"이 상태가 됨
#           (위치, 방향, 시간, 점수, 체력 등)
#    PITFALL: 필요한 상태를 빠뜨리면 나중에 대규모 수정 필요
# ============================================================

position = (0, 0)       # 현재 위치
direction = 0           # 현재 방향 (0:상, 1:우, 2:하, 3:좌)
time = 0                # 경과 시간
visited = set()         # 방문 기록 (필요시)

# ============================================================
# 2. [Direction Vector] ─────────────────────────────────
#    역할: 방향 이동을 위한 델타 배열
#    WHY: 조건문 없이 방향 기반 이동 가능 → 코드 간결화
#    ADAPT: 문제의 좌표계에 따라 순서 조정
#           - 상/우/하/좌 vs 북/동/남/서
#           - 행 증가 = 아래 vs 위
#    PITFALL: 좌표계 혼동 주의 (y축 방향)
# ============================================================

# 상(북), 우(동), 하(남), 좌(서) - 시계 방향
DR = [-1, 0, 1, 0]  # row 변화량
DC = [0, 1, 0, -1]  # col 변화량

# 방향 회전 함수
def turn_right(d):
    return (d + 1) % 4

def turn_left(d):
    return (d - 1) % 4

def turn_back(d):
    return (d + 2) % 4

# ============================================================
# 3. [Boundary Check] ─────────────────────────────────
#    역할: 격자 범위 유효성 검사
#    WHY: 범위 밖 접근 → IndexError 또는 잘못된 결과
#    PITFALL: 0-indexed vs 1-indexed 혼동
#    ADAPT: 원형 격자면 모듈러 연산 사용
# ============================================================

def is_valid(r, c, rows, cols):
    return 0 <= r < rows and 0 <= c < cols

# ============================================================
# 4. [Main Simulation Loop] ─────────────────────────────────
#    역할: 종료 조건까지 상태를 갱신하며 반복
#    WHY: 시뮬레이션의 핵심 - 매 단계 규칙 적용
#    PITFALL: 무한 루프 방지 (종료 조건 확실히)
#    COMPLEXITY: O(시뮬레이션 횟수 × 각 단계 비용)
# ============================================================

def simulate(board, commands):
    rows, cols = len(board), len(board[0])
    r, c = 0, 0          # 시작 위치
    direction = 0        # 시작 방향
    result = 0           # 결과값
    
    for cmd in commands:
        # ─────────────────────────────────
        # 4-1. [Command Parse]
        #      역할: 명령어 해석
        #      ADAPT: 문제마다 명령어 형식이 다름
        # ─────────────────────────────────
        if cmd == 'L':
            direction = turn_left(direction)
        elif cmd == 'R':
            direction = turn_right(direction)
        elif cmd == 'F':
            # ─────────────────────────────────
            # 4-2. [Move & Validate]
            #      역할: 이동 후 유효성 검사
            #      WHY: 유효하지 않으면 이동 취소 or 종료
            #      PITFALL: 이동 전 검사 vs 이동 후 검사 구분
            # ─────────────────────────────────
            nr, nc = r + DR[direction], c + DC[direction]
            
            if is_valid(nr, nc, rows, cols):
                if board[nr][nc] != 'X':  # 장애물 체크
                    r, c = nr, nc
                    result += 1
            else:
                break  # 범위 밖이면 종료 (문제에 따라 다름)
    
    return result

# ============================================================
# 5. [Result Extraction] ─────────────────────────────────
#    역할: 시뮬레이션 결과에서 정답 추출
#    ADAPT: 최종 위치, 이동 횟수, 상태값 등 문제에 따라 다름
#    PITFALL: 마지막 상태도 결과에 포함되는지 확인
# ============================================================
```

---

## Customization Points

- `State Variables`: 문제에서 추적해야 하는 상태 (위치, 방향, HP, 점수 등)
- `Direction Vector`: 좌표계와 이동 방향 정의
- `is_valid()`: 유효성 검사 조건 (범위, 장애물, 방문 여부 등)
- `Command Parse`: 명령어 해석 로직
- `Termination Condition`: 시뮬레이션 종료 조건

---

## Variations (응용 유형)

### 변형 A: 로봇 청소기 / 방향 기반 이동

**상황**: 현재 방향에 따라 이동하고, 조건에 따라 회전하는 문제
**핵심 변화**: 방향 상태가 중요, 회전 로직 필수
**추천 문제**:
- 백준 14503: 로봇 청소기
- 백준 14499: 주사위 굴리기
- **[프로그래머스]**
  - Lv1: 공원 산책 (기본 방향 이동)
  - Lv2: 리코쳇 로봇 (미끄러지는 이동)
  - Lv3: 블록 이동하기 (회전 포함 복잡 이동)

```python
def robot_cleaner(room, start_r, start_c, start_d):
    """
    로봇 청소기 시뮬레이션
    규칙: 청소 → 왼쪽 회전 후 전진 시도 → 4방향 모두 안되면 후진
    """
    DR = [-1, 0, 1, 0]
    DC = [0, 1, 0, -1]
    
    r, c, d = start_r, start_c, start_d
    cleaned = 0
    
    while True:
        # [Clean Current] ─────────────────────────────────
        #    WHY: 현재 위치가 청소 안 됐으면 청소
        #    PITFALL: 청소 여부 표시 놓치면 중복 카운트
        if room[r][c] == 0:
            room[r][c] = 2  # 청소 완료 표시
            cleaned += 1
        
        # [Try 4 Directions] ─────────────────────────────────
        #    WHY: 왼쪽부터 4방향 모두 시도
        #    ADAPT: 회전 순서가 문제마다 다를 수 있음
        found = False
        for _ in range(4):
            d = turn_left(d)
            nr, nc = r + DR[d], c + DC[d]
            
            if is_valid(nr, nc, len(room), len(room[0])):
                if room[nr][nc] == 0:  # 청소 안 된 곳
                    r, c = nr, nc
                    found = True
                    break
        
        if not found:
            # [Back Move] ─────────────────────────────────
            #    WHY: 4방향 모두 막힘 → 방향 유지한 채 후진
            #    PITFALL: 후진도 못하면 종료
            br, bc = r - DR[d], c - DC[d]
            if is_valid(br, bc, len(room), len(room[0])) and room[br][bc] != 1:
                r, c = br, bc
            else:
                break  # 종료
    
    return cleaned
```

### 변형 B: 뱀 게임 / 큐 기반 몸통 관리

**상황**: 이동하면서 몸통이 늘어나고, 자기 몸에 부딪히면 종료
**핵심 변화**: deque로 몸통 좌표 관리, 충돌 검사
**추천 문제**:
- 백준 3190: 뱀
- **[프로그래머스]**
  - Lv2: 다리를 지나는 트럭 (1D 큐 시뮬레이션)
  - Lv3: 경주로 건설 (비용 계산 포함 bfs)

```python
from collections import deque

def snake_game(n, apples, turns):
    """
    뱀 게임 시뮬레이션
    규칙: 매초 이동, 사과 먹으면 길이 증가, 자기 몸이나 벽에 부딪히면 종료
    """
    DR = [-1, 0, 1, 0]
    DC = [0, 1, 0, -1]
    
    # [State Init] ─────────────────────────────────
    #    ADAPT: 뱀의 몸통을 deque로 관리 (머리/꼬리 추가/제거 O(1))
    snake = deque([(0, 0)])  # 뱀 몸통 좌표 (머리가 앞)
    snake_set = {(0, 0)}     # O(1) 충돌 검사용
    direction = 1            # 시작: 오른쪽
    time = 0
    
    apple_set = set(apples)
    turn_dict = dict(turns)  # {시간: 방향}
    
    while True:
        time += 1
        
        # [Move Head] ─────────────────────────────────
        #    WHY: 먼저 머리 이동
        head_r, head_c = snake[0]
        nr, nc = head_r + DR[direction], head_c + DC[direction]
        
        # [Collision Check] ─────────────────────────────────
        #    WHY: 벽 또는 자기 몸에 부딪히면 종료
        #    PITFALL: 꼬리 제거 전에 충돌 검사해야 함
        if not (0 <= nr < n and 0 <= nc < n):
            break
        if (nr, nc) in snake_set:
            break
        
        # [Update Body] ─────────────────────────────────
        snake.appendleft((nr, nc))
        snake_set.add((nr, nc))
        
        if (nr, nc) in apple_set:
            apple_set.remove((nr, nc))  # 사과 먹음 → 꼬리 유지
        else:
            # [Remove Tail] ─────────────────────────────────
            #    WHY: 사과 안 먹으면 꼬리 제거 (길이 유지)
            tail = snake.pop()
            snake_set.remove(tail)
        
        # [Direction Change] ─────────────────────────────────
        #    ADAPT: 시간에 따른 방향 변경
        if time in turn_dict:
            if turn_dict[time] == 'L':
                direction = turn_left(direction)
            else:
                direction = turn_right(direction)
    
    return time
```

### 변형 C: 격자 상태 변화 / 동시 업데이트

**상황**: 모든 칸이 동시에 상태 변화하는 문제 (게임 오브 라이프 등)
**핵심 변화**: 현재 상태 기반으로 다음 상태를 별도 배열에 저장 후 교체
**추천 문제**:
- 백준 16234: 인구 이동
- 백준 14891: 톱니바퀴
- **[프로그래머스]**
  - Lv2: 프렌즈4블록 (블록 삭제 + 중력 작용)
  - Lv3: 기둥과 보 설치 (설치/삭제 후 일관성 검사)

```python
def simultaneous_update(board, steps):
    """
    동시 상태 변화 시뮬레이션
    규칙: 모든 칸이 동시에 규칙에 따라 변화
    """
    rows, cols = len(board), len(board[0])
    DR = [-1, 0, 1, 0]
    DC = [0, 1, 0, -1]
    
    for _ in range(steps):
        # [Create Next State] ─────────────────────────────────
        #    WHY: 현재 상태를 보고 다음 상태 결정 → 별도 배열 필요
        #    PITFALL: 같은 배열에서 수정하면 순서에 따라 결과 달라짐
        next_board = [[0] * cols for _ in range(rows)]
        
        for r in range(rows):
            for c in range(cols):
                # 주변 이웃 카운트
                neighbors = 0
                for d in range(4):
                    nr, nc = r + DR[d], c + DC[d]
                    if is_valid(nr, nc, rows, cols):
                        neighbors += board[nr][nc]
                
                # [Apply Rule] ─────────────────────────────────
                #    ADAPT: 문제의 상태 변화 규칙
                if board[r][c] == 1:  # 살아있음
                    if 2 <= neighbors <= 3:
                        next_board[r][c] = 1
                else:  # 죽어있음
                    if neighbors == 3:
                        next_board[r][c] = 1
        
        # [Swap] ─────────────────────────────────
        #    WHY: 다음 상태를 현재 상태로 교체
        board = next_board
    
    return board
```

---

## 디버깅 팁

1. **상태 출력**: 매 단계 상태를 print로 출력하여 흐름 확인
2. **작은 케이스**: 손으로 계산할 수 있는 작은 입력으로 테스트
3. **경계 조건**: 격자 끝, 첫/마지막 명령, 특수 케이스 확인
4. **좌표계 그리기**: 문제의 좌표계를 그림으로 그려서 확인

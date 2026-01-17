# 다이나믹 프로그래밍 Pattern Skeleton

> 생성일: 2026-01-16

---

## Why & What (이 패턴은 왜/무엇)
- **목적**: 중복되는 부분 문제(Overlapping Subproblems)를 한 번만 계산하여 지수 시간을 다항 시간으로 줄임
- **본질**: "큰 문제를 작은 문제로 쪼개고, 작은 문제의 답을 저장(메모)하여 재활용한다"
- **장점**: 
  - 완전탐색의 중복 계산을 제거 → 시간 복잡도 대폭 감소
  - 최적 부분 구조(Optimal Substructure)를 가진 문제에서 최적해 보장

## When to Use (이럴 때 사용)
문제에서 다음 키워드가 보이면 이 패턴을 떠올리세요:
- `최솟값/최댓값 구하기`: "~하는 최소 비용", "~하는 최대 이익"
- `경우의 수 세기`: "~하는 방법의 수", "~에 도달하는 경로의 수"
- `가능/불가능 판단`: "~가 가능한가?", "~를 만들 수 있는가?"
- `최적화 문제`: "~를 최대화/최소화하라"
- `연속/부분 수열`: LIS, LCS, 부분합 관련 문제
- `배낭 문제 변형`: 물건 선택, 용량 제한, 조합 최적화

## 💡 Core Insight: DP는 캐싱이다

> **"멱등성(Idempotency)이 보장되면 캐싱할 수 있다"**

### DP가 캐싱인 이유

DP의 메모이제이션은 본질적으로 **함수 호출 결과를 캐싱**하는 것입니다.

```python
# 웹 개발에서의 캐싱
cache = {}
def get_user_data(user_id):
    if user_id in cache:
        return cache[user_id]       # 캐시 히트!
    data = expensive_db_query(user_id)
    cache[user_id] = data           # 저장
    return data

# DP에서의 메모이제이션 (완전히 동일한 구조!)
memo = {}
def fib(n):
    if n in memo:
        return memo[n]              # 캐시 히트!
    if n <= 1:
        return n
    result = fib(n-1) + fib(n-2)
    memo[n] = result                # 저장
    return result
```

### 왜 캐싱이 가능한가? → 멱등성

| 개념 | 정의 | DP에서의 의미 |
|------|------|--------------|
| **멱등성 (Idempotency)** | 같은 입력 → 항상 같은 출력 | `fib(5)`는 언제 호출해도 항상 `5` |
| **부작용 없음 (No Side Effects)** | 함수가 외부 상태를 변경하지 않음 | 순수 함수로 작성된 점화식 |
| **결정론적 (Deterministic)** | 결과가 랜덤이 아님 | 입력이 같으면 계산 과정도 동일 |

**이 세 가지가 보장되기 때문에**, 한 번 계산한 결과는 영원히 유효합니다.

### 캐싱이 불가능한 경우 (반례)

```python
# ❌ 멱등성이 없는 경우 - 캐싱 불가
import random
def random_fib(n):
    if n <= 1:
        return n
    return random_fib(n-1) + random_fib(n-2) + random.randint(0, 1)
# → 같은 n에 대해 매번 다른 결과 → 캐싱 의미 없음

# ❌ 부작용이 있는 경우 - 캐싱 위험
counter = 0
def counting_fib(n):
    global counter
    counter += 1  # 부작용!
    if n <= 1:
        return n
    return counting_fib(n-1) + counting_fib(n-2)
# → 캐싱하면 counter가 정확하지 않게 됨
```

### 실무와의 연결

| 영역 | 캐싱 대상 | 멱등성 보장 방법 |
|------|----------|-----------------|
| **DP (알고리즘)** | 재귀 함수 결과 | 순수 함수로 점화식 작성 |
| **웹 서버** | API 응답 (GET) | REST 규약 준수, 상태 변경 없는 조회 |
| **프론트엔드** | 컴포넌트 렌더링 | React.memo, useMemo |
| **데이터베이스** | 쿼리 결과 | 읽기 전용 쿼리, 스냅샷 격리 |

> 💡 **한 줄 요약**: DP는 "멱등성이 보장된 재귀 함수에 캐싱을 적용한 것"

---

## 핵심 구조

### 접근법 1: Top-Down (Memoization)

```python
# [Dynamic Programming - Top-Down Pattern]
# 재귀 + 메모이제이션으로 필요한 부분만 계산합니다

def solve(problem):
    memo = {}  # 또는 배열로 초기화
    
    def dp(state):
        # 1. [Base Case] ─────────────────────────────────
        #    역할: 더 이상 쪼갤 수 없는 가장 작은 문제의 답을 정의
        #    WHY: 재귀의 종료 조건. 없으면 무한 재귀 발생
        #    PITFALL: 모든 경계 조건을 빠짐없이 처리해야 함
        if is_base_case(state):
            return base_value(state)
        
        # 2. [Memo Check] ─────────────────────────────────
        #    역할: 이미 계산한 상태인지 확인
        #    WHY: 중복 계산 방지 → 시간 복잡도 개선의 핵심
        #    PITFALL: 상태 표현이 잘못되면 메모가 제대로 작동 안 함
        if state in memo:
            return memo[state]
        
        # 3. [State Transition] ─────────────────────────────────
        #    역할: 현재 상태에서 가능한 모든 선택/전이를 시도
        #    WHY: "현재 문제 = 작은 문제들의 조합"이라는 DP의 핵심
        #    ADAPT: 이 부분이 문제마다 가장 크게 달라짐
        #           - 선택지가 무엇인가?
        #           - 각 선택이 어떤 하위 상태로 이어지는가?
        result = initial_value  # min이면 float('inf'), max면 float('-inf'), 합이면 0
        
        for choice in get_choices(state):
            # 4. [Recurrence Relation] ─────────────────────────────────
            #    역할: 점화식 적용 - 하위 문제의 답으로 현재 답 계산
            #    WHY: 최적 부분 구조 활용
            #    ADAPT: 문제 유형에 따라 min, max, sum, or 등 사용
            next_state = transition(state, choice)
            sub_result = dp(next_state)
            result = combine(result, sub_result, choice)
        
        # 5. [Memoize] ─────────────────────────────────
        #    역할: 계산 결과를 저장하여 재사용
        #    WHY: 이 저장이 없으면 일반 재귀와 다를 바 없음
        #    PITFALL: 반드시 return 전에 저장해야 함
        memo[state] = result
        return result
    
    # 6. [Entry Point] ─────────────────────────────────
    #    역할: 원래 문제의 초기 상태로 DP 시작
    #    ADAPT: 문제가 요구하는 "최종 답"이 무엇인지 정의
    return dp(initial_state)
```

---

### 접근법 2: Bottom-Up (Tabulation)

```python
# [Dynamic Programming - Bottom-Up Pattern]
# 작은 문제부터 큰 문제로 테이블을 채워나갑니다

def solve(problem):
    # 1. [Table Init] ─────────────────────────────────
    #    역할: DP 테이블 초기화 - 크기와 초기값 설정
    #    WHY: 상태 공간을 미리 정의해야 점화식 적용 가능
    #    ADAPT: 상태 변수 개수에 따라 1D, 2D, 3D 배열 결정
    #    PITFALL: 초기값을 잘못 설정하면 전체 답이 틀림
    #             min 문제: float('inf')로 초기화, max 문제: float('-inf') 또는 0
    dp = [initial_value] * (n + 1)  # 1D 예시
    # dp = [[initial_value] * (m + 1) for _ in range(n + 1)]  # 2D 예시
    
    # 2. [Base Case] ─────────────────────────────────
    #    역할: 가장 작은 부분 문제의 답을 테이블에 직접 기록
    #    WHY: 점화식의 시작점 - 이것이 없으면 채워나갈 수 없음
    #    ADAPT: 문제에 따라 dp[0], dp[0][0] 등 다양
    dp[0] = base_value
    
    # 3. [Fill Table] ─────────────────────────────────
    #    역할: 점화식에 따라 테이블을 순차적으로 채움
    #    WHY: 작은 문제 → 큰 문제 순서로 의존성 해결
    #    COMPLEXITY: 상태 수 × 전이 수 = 전체 시간 복잡도
    #    PITFALL: 순회 순서가 의존성을 만족해야 함
    #             (이전 상태가 먼저 계산되어 있어야 함)
    for state in range(1, n + 1):
        
        # 4. [State Transition] ─────────────────────────────────
        #    역할: 현재 상태로 올 수 있는 모든 이전 상태 고려
        #    WHY: "현재 = 이전 상태들의 조합"
        #    ADAPT: Push 방식 vs Pull 방식 선택
        #           Push: dp[curr] → dp[next] 갱신
        #           Pull: dp[prev]들 → dp[curr] 계산
        for choice in get_choices(state):
            prev_state = get_previous(state, choice)
            
            # 5. [Recurrence Relation] ─────────────────────────────────
            #    역할: 점화식 적용
            #    ADAPT: dp[i] = f(dp[i-1], dp[i-2], ...)
            dp[state] = combine(dp[state], dp[prev_state], choice)
    
    # 6. [Answer Extraction] ─────────────────────────────────
    #    역할: 테이블에서 최종 답 추출
    #    WHY: 원래 문제에 해당하는 상태의 값이 답
    #    PITFALL: 답의 위치가 dp[n]인지, dp[target]인지, 
    #             max(dp)인지 문제를 잘 읽어야 함
    return dp[answer_state]
```

---

## Customization Points

- `state`: 현재 상태를 정의하는 변수들 (위치, 남은 용량, 이전 선택 등)
- `is_base_case()` / `base_indices`: 재귀 종료 조건 또는 테이블 시작점
- `get_choices()`: 현재 상태에서 가능한 선택지 목록
- `transition()`: 선택에 따른 상태 전이 규칙
- `combine()`: 하위 문제 결과를 현재 문제에 합치는 방법 (min, max, +, or)
- `initial_state` / `answer_state`: 시작과 끝 상태 정의

---

## 🧭 Top-Down vs Bottom-Up 선택 가이드

### 핵심 차이

| 구분 | Top-Down (Memoization) | Bottom-Up (Tabulation) |
|------|----------------------|----------------------|
| **방향** | 큰 문제 → 작은 문제 (재귀) | 작은 문제 → 큰 문제 (반복문) |
| **구현** | 재귀 함수 + 딕셔너리/배열 캐싱 | for 루프 + 배열 채우기 |
| **초기화** | 필요한 상태만 계산 (lazy) | 모든 상태 미리 계산 (eager) |
| **스택** | 재귀 깊이 제한 있음 (Python 기본 1000) | 스택 사용 안 함 |
| **공간** | 필요한 것만 저장 (sparse) | 전체 테이블 저장 (dense) |

### 언제 어떤 걸 쓸까?

#### ✅ Top-Down을 선택하는 경우

```
1. 모든 상태를 방문하지 않아도 될 때
   예: 가지치기가 많은 문제, 희소한 상태 공간
   
2. 점화식을 자연스럽게 재귀로 표현할 수 있을 때
   예: 트리 DP, 복잡한 상태 전이
   
3. 빠르게 구현하고 싶을 때
   예: 코테에서 시간이 부족할 때 (재귀가 직관적)
   
4. 상태가 연속적이지 않을 때
   예: dp[(x, y, dir, cnt)] 같은 복잡한 키
```

#### ✅ Bottom-Up을 선택하는 경우

```
1. 모든 상태를 반드시 채워야 할 때
   예: 격자 DP, 문자열 DP (LCS, LIS)
   
2. 재귀 깊이가 너무 깊을 때
   예: N이 10^5 이상이면 스택 오버플로우 위험
   
3. 공간 최적화가 필요할 때
   예: dp[i]가 dp[i-1]에만 의존 → 1D 압축 가능
   
4. 상수 시간 최적화가 중요할 때
   예: 재귀 호출 오버헤드 제거
```

### 실전 판단 플로우차트

```
                    ┌─────────────────┐
                    │  DP 문제 발견!   │
                    └────────┬────────┘
                             ▼
              ┌──────────────────────────┐
              │ 상태 공간이 희소한가?     │
              │ (방문할 상태 << 전체 상태) │
              └──────────┬───────────────┘
                    ┌────┴────┐
                    │         │
                   YES       NO
                    │         │
                    ▼         ▼
           ┌────────────┐  ┌──────────────────┐
           │ Top-Down   │  │ N이 10만 이상?    │
           │ 추천       │  └────────┬─────────┘
           └────────────┘      ┌────┴────┐
                              YES       NO
                               │         │
                               ▼         ▼
                    ┌────────────┐  ┌────────────────┐
                    │ Bottom-Up  │  │ 둘 다 OK       │
                    │ 필수       │  │ 편한 것 선택   │
                    │ (스택제한) │  └────────────────┘
                    └────────────┘
```

---

## 🧠 DP 문제 접근 사고 순서

### Step 1: DP인지 판단하기

```
□ 최적화 문제인가? (최소/최대/경우의 수)
□ 중복 부분 문제가 있는가? (같은 계산이 반복되는가?)
□ 최적 부분 구조가 있는가? (작은 문제의 최적해 → 큰 문제의 최적해)

위 세 가지 중 두 개 이상 YES면 DP를 고려!
```

### Step 2: 상태(State) 정의하기

> **"dp[???]가 의미하는 것은 무엇인가?"**

```python
# 나쁜 예: 모호한 정의
dp[i] = "i번째까지의 뭔가"

# 좋은 예: 명확한 정의
dp[i] = "arr[i]로 끝나는 LIS의 최대 길이"
dp[i][j] = "s1[:i]와 s2[:j]의 LCS 길이"
dp[i][w] = "처음 i개 물건으로 용량 w를 채울 때 최대 가치"
```

**팁**: 상태 정의가 어려우면 "무엇을 반환해야 하는가?"를 먼저 생각하세요.

### Step 3: 점화식(Recurrence) 도출하기

> **"dp[현재]를 dp[이전들]로 어떻게 표현하는가?"**

```
현재 상태에서 가능한 선택지를 나열:
  - 선택 A를 하면 → dp[상태A]
  - 선택 B를 하면 → dp[상태B]
  - ...

결과 = 선택지들의 조합 (min, max, +, or)
```

**예시 (계단 오르기)**:
```python
# i번째 계단에 도달하는 방법:
# - (i-1)번째에서 1칸 올라옴
# - (i-2)번째에서 2칸 올라옴
dp[i] = max(dp[i-1], dp[i-2]) + cost[i]
```

### Step 4: 기저 조건(Base Case) 정의하기

> **"더 이상 쪼갤 수 없는 가장 작은 문제의 답은?"**

```python
# 일반적인 기저 조건들
dp[0] = 0           # 아무것도 없을 때
dp[0] = 1           # 빈 집합도 하나의 경우의 수
dp[0][0] = True     # 시작점
dp[i][0] = ???      # 첫 번째 열의 경계 조건
```

**PITFALL**: 기저 조건을 빠뜨리면 쓰레기 값 참조 또는 무한 재귀!

### Step 5: 계산 순서 결정하기

> **"어떤 순서로 채워야 의존성이 만족되는가?"**

```
Bottom-Up일 때:
  - dp[i]가 dp[i-1]에 의존 → 작은 i부터 큰 i 순서로
  - dp[i][j]가 dp[i-1][j], dp[i][j-1]에 의존 → 왼쪽 위에서 오른쪽 아래로
  
Top-Down일 때:
  - 재귀가 알아서 처리 (단, 메모 체크 필수)
```

### Step 6: 답 추출하기

> **"최종 답은 테이블의 어디에 있는가?"**

```python
# 케이스별 답 위치
return dp[n]              # 마지막 상태가 답
return dp[n][target]      # 특정 목표에 도달한 상태
return max(dp)            # 모든 상태 중 최댓값 (LIS)
return dp[0][0]           # 시작점이 답 (역방향 DP의 경우)
```

### 🎯 실전 체크리스트

```
□ 1. DP 문제인지 확인했다
□ 2. dp[상태]의 의미를 한 문장으로 정의했다
□ 3. 점화식을 세웠다 (dp[현재] = f(dp[이전들]))
□ 4. 기저 조건을 모두 정의했다
□ 5. 순회 순서가 의존성을 만족한다
□ 6. 답의 위치를 파악했다
□ 7. (Bottom-Up) 공간 최적화 가능 여부를 검토했다
□ 8. (Top-Down) sys.setrecursionlimit() 설정을 확인했다
```

---

## Variations (응용 유형)

### 변형 A: 1차원 DP (선형 점화식)

**상황**: 상태가 하나의 인덱스로 표현될 때 (피보나치, 계단 오르기 등)
**핵심 변화**: dp[i]가 dp[i-1], dp[i-2] 등 이전 몇 개 값에만 의존

**추천 문제**
- 백준 1463 - 1로 만들기
- 백준 2579 - 계단 오르기
- 프로그래머스 - N으로 표현 (Lv.3)
- 프로그래머스 - 정수 삼각형 (Lv.3)
- 프로그래머스 - 도둑질 (Lv.4)

```python
# 1차원 DP 핵심 구조
def linear_dp(n):
    # [Table Init] ─────────────────────────────────
    #    ADAPT: 문제에 따라 크기 n+1 또는 상황에 맞게
    dp = [0] * (n + 1)
    
    # [Base Case] ─────────────────────────────────
    #    WHY: dp[0], dp[1] 등 시작점 정의
    dp[0] = base_value_0
    dp[1] = base_value_1
    
    # [Fill] ─────────────────────────────────
    #    WHY: i=2부터 시작하는 이유 - 0,1은 이미 정의됨
    #    COMPLEXITY: O(N)
    for i in range(2, n + 1):
        # [Recurrence] ─────────────────────────────────
        #    ADAPT: dp[i] = dp[i-1] + dp[i-2] (피보나치)
        #           dp[i] = min(dp[i-1], dp[i-2]) + cost[i] 등
        dp[i] = dp[i-1] + dp[i-2]  # 예시: 피보나치
    
    return dp[n]
```

**공간 최적화 팁**:
```python
# [Space Optimization] ─────────────────────────────────
#    WHY: dp[i]가 직전 k개 값에만 의존하면 O(N) → O(k) 가능
#    PITFALL: 갱신 순서 주의 - 덮어쓰기 전에 사용해야 함
prev2, prev1 = base_0, base_1
for i in range(2, n + 1):
    curr = prev1 + prev2  # 예시: 피보나치
    prev2, prev1 = prev1, curr
return prev1
```

---

### 변형 B: 2차원 DP (격자/문자열 문제)

**상황**: 두 개의 상태 변수가 필요할 때 (격자 이동, 두 문자열 비교)
**핵심 변화**: dp[i][j]가 인접 상태들 dp[i-1][j], dp[i][j-1] 등에 의존

**추천 문제**
- 백준 1149 - RGB거리
- 백준 9251 - LCS
- 프로그래머스 - 등굣길 (Lv.3)
- 프로그래머스 - 정수 삼각형 (Lv.3)
- 프로그래머스 - 사칙연산 (Lv.3)

```python
# 2차원 DP 핵심 구조
def grid_dp(rows, cols, grid):
    # [Table Init] ─────────────────────────────────
    #    ADAPT: 경계 조건 처리를 위해 (rows+1) x (cols+1) 사용하기도 함
    dp = [[0] * cols for _ in range(rows)]
    
    # [Base Case] ─────────────────────────────────
    #    WHY: 첫 행/열은 이전 상태가 하나뿐
    #    PITFALL: 경계 초기화를 빠뜨리면 쓰레기 값 참조
    dp[0][0] = grid[0][0]
    for i in range(1, rows):
        dp[i][0] = dp[i-1][0] + grid[i][0]
    for j in range(1, cols):
        dp[0][j] = dp[0][j-1] + grid[0][j]
    
    # [Fill] ─────────────────────────────────
    #    WHY: 왼쪽 위에서 오른쪽 아래로 채워야 의존성 만족
    #    COMPLEXITY: O(rows × cols)
    for i in range(1, rows):
        for j in range(1, cols):
            # [Recurrence] ─────────────────────────────────
            #    ADAPT: 격자 이동, 문자열 매칭 등에 따라 다름
            #           격자 최단거리: dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + cost
            #           경로 수: dp[i][j] = dp[i-1][j] + dp[i][j-1]
            dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
    
    return dp[rows-1][cols-1]
```

---

### 변형 C: Knapsack (배낭 문제)

**상황**: 용량 제한 하에서 최대 가치/최소 비용을 구하는 문제
**핵심 변화**: 상태에 "남은 용량"이 포함됨

**추천 문제**
- 백준 12865 - 평범한 배낭 (0/1 Knapsack)
- 백준 2293 - 동전 1 (Unbounded Knapsack)
- 프로그래머스 - 정수 삼각형 (Lv.3)
- 프로그래머스 - 거스름돈 (Lv.2)
- 프로그래머스 - N으로 표현 (Lv.3)

```python
# 0/1 Knapsack 핵심 구조
def knapsack_01(items, capacity):
    n = len(items)
    # [Table Init] ─────────────────────────────────
    #    WHY: dp[i][w] = 처음 i개 물건으로 용량 w 배낭을 채울 때 최대 가치
    #    ADAPT: 최대 가치 → 0으로 초기화, 최소 비용 → float('inf')
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        weight_i, value_i = items[i-1]
        
        for w in range(capacity + 1):
            # [Choice: Skip] ─────────────────────────────────
            #    WHY: i번째 물건을 안 넣는 경우 = 이전 상태 그대로
            dp[i][w] = dp[i-1][w]
            
            # [Choice: Take] ─────────────────────────────────
            #    WHY: i번째 물건을 넣을 수 있으면 비교
            #    PITFALL: w >= weight_i 조건 확인 필수
            if w >= weight_i:
                # [Recurrence] ─────────────────────────────────
                #    ADAPT: 0/1은 dp[i-1][w-weight]
                #           Unbounded는 dp[i][w-weight] (같은 물건 재사용 가능)
                dp[i][w] = max(dp[i][w], dp[i-1][w - weight_i] + value_i)
    
    return dp[n][capacity]
```

**공간 최적화 (1D 배열)**:
```python
# [Space Optimization] ─────────────────────────────────
#    WHY: dp[i]가 dp[i-1]에만 의존 → 1D로 압축 가능
#    PITFALL: 0/1은 역순, Unbounded는 정순으로 순회해야 함!
#             역순: 같은 물건을 한 번만 사용 (덮어쓰기 전에 참조)
#             정순: 같은 물건을 여러 번 사용 가능

# 0/1 Knapsack (역순 순회)
def knapsack_01_optimized(items, capacity):
    dp = [0] * (capacity + 1)
    for weight_i, value_i in items:
        for w in range(capacity, weight_i - 1, -1):  # 역순!
            dp[w] = max(dp[w], dp[w - weight_i] + value_i)
    return dp[capacity]

# Unbounded Knapsack (정순 순회)
def knapsack_unbounded(items, capacity):
    dp = [0] * (capacity + 1)
    for w in range(1, capacity + 1):  # 정순!
        for weight, value in items:
            if w >= weight:
                dp[w] = max(dp[w], dp[w - weight] + value)
    return dp[capacity]
```

---

### 변형 D: LCS (최장 공통 부분 수열)

**상황**: 두 수열에서 공통으로 나타나는 가장 긴 부분 수열 찾기
**핵심 변화**: 두 문자열의 인덱스가 상태, 문자 일치 여부로 분기

**추천 문제**
- 백준 9251 - LCS
- 백준 9252 - LCS 2 (역추적)
- 프로그래머스 - 사치연산 (Lv.3)
- 프로그래머스 - 편집 거리 (Lv.2-3, 커스텀 문제)

```python
# LCS 핵심 구조
def lcs(s1, s2):
    n, m = len(s1), len(s2)
    # [Table Init] ─────────────────────────────────
    #    WHY: dp[i][j] = s1[:i]와 s2[:j]의 LCS 길이
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            # [Match] ─────────────────────────────────
            #    WHY: 두 문자가 같으면 LCS에 포함 가능
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            # [No Match] ─────────────────────────────────
            #    WHY: 다르면 둘 중 하나를 스킵한 결과 중 큰 것
            #    PITFALL: max를 빼먹으면 잘못된 값 저장
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    return dp[n][m]
```

---

### 변형 E: LIS (최장 증가 부분 수열)

**상황**: 주어진 수열에서 증가하는 순서를 유지하는 가장 긴 부분 수열
**핵심 변화**: 이분 탐색과 결합하면 O(N log N)으로 최적화 가능

**추천 문제**
- 백준 11053 - 가장 긴 증가하는 부분 수열
- 백준 12015 - 가장 긴 증가하는 부분 수열 2 (이분탐색)
- 프로그래머스 - 스티커 모으기(2) (Lv.3)
- 프로그래머스 - 도둑질 (Lv.4)

```python
# LIS 기본 (O(N²))
def lis_basic(arr):
    n = len(arr)
    # [Table Init] ─────────────────────────────────
    #    WHY: dp[i] = arr[i]로 끝나는 LIS의 길이
    #    ADAPT: 모든 원소는 최소 자기 자신만으로 길이 1
    dp = [1] * n
    
    for i in range(1, n):
        for j in range(i):
            # [Transition] ─────────────────────────────────
            #    WHY: arr[j] < arr[i]이면 j 뒤에 i를 붙일 수 있음
            if arr[j] < arr[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    
    # [Answer] ─────────────────────────────────
    #    PITFALL: 답은 dp[n-1]이 아니라 max(dp)!
    #             LIS가 마지막 원소로 끝나지 않을 수 있음
    return max(dp)

# LIS 최적화 (O(N log N))
from bisect import bisect_left

def lis_optimized(arr):
    # [Idea] ─────────────────────────────────
    #    WHY: tails[i] = 길이가 i+1인 증가 수열의 최소 마지막 원소
    #         이분 탐색으로 tails 관리 → O(log N) 갱신
    tails = []
    
    for x in arr:
        # [Binary Search] ─────────────────────────────────
        #    WHY: x가 들어갈 수 있는 위치를 찾음
        #    ADAPT: bisect_left 사용 (lower_bound)
        pos = bisect_left(tails, x)
        
        if pos == len(tails):
            tails.append(x)   # 새로운 길이의 LIS 발견
        else:
            tails[pos] = x    # 같은 길이에서 더 작은 끝값으로 갱신
    
    return len(tails)
```

---

## DP 문제 접근 체크리스트

1. **상태 정의**: "dp[state]가 의미하는 것은 무엇인가?"
2. **점화식 도출**: "dp[state]는 어떤 하위 상태들로부터 계산되는가?"
3. **기저 조건**: "가장 작은 문제의 답은 무엇인가?"
4. **계산 순서**: "어떤 순서로 채워야 의존성이 만족되는가?"
5. **답 추출**: "최종 답은 테이블의 어디에 있는가?"

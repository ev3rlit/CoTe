# DP 패턴 스타일 가이드

> 다이나믹 프로그래밍 (Dynamic Programming) 구현 스타일

---

## 사용 시점

다음 키워드가 보이면 DP를 고려:

- **최댓값/최솟값** (부분 문제로 분해 가능)
- **경우의 수** / **방법의 수**
- **~까지의 최적해**
- **연속된** / **부분 수열**
- 문제가 **겹치는 부분 문제**를 가짐
- **최적 부분 구조** 존재

---

## 핵심 패턴

### Bottom-Up DP 템플릿

```python
def solution(data):
    n = len(data)

    # DP 테이블 초기화
    dp = [0] * n
    # 또는 2D: dp = [[0] * cols for _ in range(rows)]

    # 기저 조건 설정
    dp[0] = data[0]

    # 점화식 적용
    for i in range(1, n):
        dp[i] = max(dp[i-1], dp[i-2] + data[i])

    return dp[n-1]
```

---

## 변수 네이밍

| 용도 | 변수명 | 예시 |
|------|--------|------|
| DP 테이블 | `dp` | `dp = [0] * n` |
| 이전 상태 | `prev1, prev2` | `prev2, prev1 = prev1, max(...)` |
| 현재 인덱스 | `i, j` | `for i in range(n)` |
| 데이터 길이 | `n` | `n = len(data)` |

---

## DP 테이블 초기화

### 1D DP

```python
# 기본
dp = [0] * n

# 초기값 설정
dp = [float('inf')] * n  # 최솟값 찾을 때
dp = [float('-inf')] * n  # 최댓값 찾을 때
```

### 2D DP

```python
# 기본
dp = [[0] * cols for _ in range(rows)]

# 입력 배열 복사
dp = [row[:] for row in triangle]
```

---

## 공간 최적화 패턴

### prev1, prev2 방식

연속된 이전 값만 필요한 경우:

```python
def solution(money):
    n = len(money)

    def rob_linear(start, end):
        prev2, prev1 = 0, 0
        for m in range(start, end + 1):
            prev2, prev1 = prev1, max(prev1, prev2 + money[m])
        return prev1

    return max(rob_linear(0, n-2), rob_linear(1, n-1))
```

### 설명

```python
# prev1, prev2 상태 변화
# 1. prev2=0, prev1=0
# 2. prev2=0, prev1=money[0]
# 3. prev2=money[0], prev1=max(...)
# ...
# 변수 2개로 O(1) 공간에서 처리 가능
```

---

## 원형 배열 DP 패턴 (도둑질)

첫 번째와 마지막이 연결된 경우:

```python
def solution(money):
    n = len(money)

    if n == 3:
        return max(money)

    def rob_linear(start, end):
        prev2, prev1 = 0, 0
        for m in range(start, end + 1):
            prev2, prev1 = prev1, max(prev1, prev2 + money[m])
        return prev1

    # 경우 1: 첫 번째 집 포함, 마지막 집 제외
    case1 = rob_linear(0, n - 2)

    # 경우 2: 첫 번째 집 제외, 마지막 집 포함
    case2 = rob_linear(1, n - 1)

    return max(case1, case2)
```

---

## 2D DP 패턴 (정수 삼각형)

### Bottom-Up (아래에서 위로)

```python
def solution(triangle):
    # 입력 배열 복사
    dp = [row[:] for row in triangle]

    # 아래에서 위로 올라가면서 최대값 누적
    for i in range(len(dp) - 2, -1, -1):
        for j in range(i + 1):
            # 아래 두 자식 중 큰 값을 선택해서 현재에 더함
            dp[i][j] += max(dp[i+1][j], dp[i+1][j+1])

    return dp[0][0]
```

### 인덱스 관계

```python
# 정수 삼각형에서 부모-자식 관계
# dp[i][j]의 자식: dp[i+1][j], dp[i+1][j+1]

# 격자에서 이동
# dp[i][j] = dp[i-1][j] + dp[i][j-1]  # 왼쪽, 위에서 오는 경우
```

---

## 점화식 패턴

### 선택/비선택 패턴

```python
# i번째를 선택하는 경우 vs 선택하지 않는 경우
dp[i] = max(dp[i-1], dp[i-2] + value[i])
```

### 경로 패턴

```python
# 위 또는 왼쪽에서 오는 경우
dp[i][j] = dp[i-1][j] + dp[i][j-1]
```

### RGB 거리 패턴 (선택 제약)

```python
# 이전에 선택한 것과 다른 것 선택
dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + cost[i][0]
dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + cost[i][1]
dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + cost[i][2]
```

---

## 상태 정의 주석 패턴

```python
# dp[i] = i번째까지 고려했을 때 최대값
# dp[i][j] = i행 j열까지의 최소 비용
# dp[i][k] = i번째 집에서 k색을 선택했을 때 최소 비용
```

---

## 주석 스타일 예시

```python
# 2칸마다 한집을 선택할 수 있음
# 원형이므로 첫번째 집을 선택하는 경우 마지막집은 못함
# 첫번째 집을 건너띄는 경우 마지막집 선택 가능

# dp[i] = i번째 집에서 최대값
# dp[i] = max(dp[i-1], dp[i-2] + money[i])
# 1칸전 집의 최대값을 하거나, 2칸전 집에서 도둑질을 하는 경우
```

---

## 체크리스트

구현 시 확인할 항목:

- [ ] 상태 정의가 명확한가? (`dp[i]`의 의미)
- [ ] 기저 조건이 올바른가?
- [ ] 점화식이 정확한가?
- [ ] 순회 방향이 맞는가? (의존성 고려)
- [ ] 인덱스 범위 체크 (`i-1`, `i-2` 등)
- [ ] 공간 최적화 가능한가?

---

## DP 유형별 패턴

| 유형 | 특징 | 예시 |
|------|------|------|
| 1D DP | 선형 배열 | 도둑질, 계단 오르기 |
| 2D DP | 격자/테이블 | 정수 삼각형, 등굣길 |
| 원형 DP | 처음과 끝 연결 | 도둑질 |
| 구간 DP | 구간 분할 | 행렬 곱셈 |
| 비트마스크 DP | 상태를 비트로 표현 | 외판원 문제 |

---

## 관련 문제 유형

| 문제 | 패턴 |
|------|------|
| 도둑질 | 1D DP + 원형 배열 |
| 정수 삼각형 | 2D DP (Bottom-Up) |
| RGB 거리 | 선택 제약 DP |
| 등굣길 | 경로 카운팅 DP |
| N으로 표현 | BFS/Set 기반 DP |

---

## 참고

- `/GEMINI.md` - 전체 스타일 가이드

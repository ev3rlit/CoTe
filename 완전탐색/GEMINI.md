# 완전탐색 패턴 스타일 가이드

> 완전탐색 (Brute Force) 및 조합 탐색 구현 스타일

---

## 사용 시점

다음 조건이 보이면 완전탐색을 고려:

- **N이 작음** (N ≤ 10: O(N!), N ≤ 20: O(2^N))
- **모든 경우의 수** 탐색
- **조합/순열** 생성
- **최적해**를 찾지만 그리디/DP가 안 될 때
- 시간 복잡도를 계산해도 **1억 이하**

---

## 핵심 패턴

### itertools 활용

```python
from itertools import permutations, combinations

def solution(data):
    candidates = set()

    # 모든 길이의 순열 생성
    for length in range(1, len(data) + 1):
        for perm in permutations(data, length):
            candidates.add(process(perm))

    # 조건에 맞는 것 카운트
    answer = 0
    for value in candidates:
        if is_valid(value):
            answer += 1

    return answer
```

---

## 변수 네이밍

| 용도 | 변수명 | 예시 |
|------|--------|------|
| 후보 집합 | `candidates` | `candidates = set()` |
| 결과값 | `answer`, `result` | `answer = 0` |
| 순열/조합 | `perm`, `comb` | `for perm in permutations(...)` |
| 캐시 | `cache`, `prime_cache` | `prime_cache = set()` |
| 길이/개수 | `length`, `n` | `for length in range(1, n+1)` |

---

## itertools 사용 패턴

### 순열 (permutations)

순서가 중요한 경우:

```python
from itertools import permutations

# 모든 길이의 순열
for length in range(1, len(data) + 1):
    for perm in permutations(data, length):
        # perm은 튜플: (a, b, c)
        process(perm)
```

### 조합 (combinations)

순서가 중요하지 않은 경우:

```python
from itertools import combinations

# 길이 r의 모든 조합
for comb in combinations(data, r):
    process(comb)
```

### 중복 순열/조합

```python
from itertools import product, combinations_with_replacement

# 중복 순열 (길이 r)
for perm in product(data, repeat=r):
    process(perm)

# 중복 조합 (길이 r)
for comb in combinations_with_replacement(data, r):
    process(comb)
```

---

## 소수 판별 패턴

### 기본 소수 판별

```python
def is_prime(number):
    if number < 2:
        return False

    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False

    return True
```

### 캐시 활용 소수 판별

```python
prime_cache = set()

def is_prime(number):
    if number < 2:
        return False

    if number in prime_cache:
        return True

    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False

    prime_cache.add(number)
    return True
```

---

## 숫자 조합 패턴 (소수 찾기)

```python
from itertools import permutations

def solution(numbers):
    # 숫자 배열 변환
    numbers = list(map(int, list(numbers)))

    # 순열로 가능한 모든 숫자 생성
    candidates = set()
    for length in range(1, len(numbers) + 1):
        # set으로 중복 제거
        candidates.update(map(concat_number, permutations(numbers, length)))

    # 소수 카운트
    answer = 0
    for value in candidates:
        if is_prime(value):
            answer += 1

    return answer

def concat_number(numbers):
    return int(''.join(map(str, numbers)))
```

---

## 백트래킹 완전탐색 패턴

itertools 대신 재귀로 구현:

```python
def solution(data):
    n = len(data)
    visited = [False] * n
    result = []

    def backtrack(current):
        if len(current) == n:
            result.append(calculate(current))
            return

        for i in range(n):
            if visited[i]:
                continue

            visited[i] = True
            current.append(data[i])
            backtrack(current)
            current.pop()
            visited[i] = False

    backtrack([])
    return max(result)
```

---

## 소수 찾기 전체 예시

```python
from itertools import permutations

prime_cache = set()

def is_prime(number):
    if number < 2:
        return False

    if number in prime_cache:
        return True

    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False

    prime_cache.add(number)
    return True

def concat_number(numbers):
    return int(''.join(map(str, numbers)))

def solution(numbers):
    # 1. 숫자 배열 변환
    numbers = list(map(int, list(numbers)))

    # 2. 순열로 종이 조각의 갯수만큼 경우의 수 찾기
    # 3. 모든 경우의수 에서 중복제거
    candidates = set()
    for i in range(1, len(numbers) + 1):
        candidates.update(map(concat_number, permutations(numbers, i)))

    # 4. 경우의 수 마다 소수인지 확인
    answer = 0
    for value in candidates:
        if is_prime(value):
            answer += 1

    return answer
```

---

## 주석 스타일 예시

```python
# 1. 숫자 배열 변환
# 2. 순열로 종이 조각의 갯수만큼 경우의 수 찾기
# 3. 모든 경우의수 에서 중복제거
# 4. 경우의 수 마다 소수인지 확인
```

---

## 시간복잡도 판단

| N | 복잡도 | 연산 수 | 가능 여부 |
|---|--------|---------|-----------|
| 10 | O(N!) | 3,628,800 | O |
| 11 | O(N!) | 39,916,800 | O |
| 12 | O(N!) | 479,001,600 | 조심 |
| 13+ | O(N!) | 60억+ | X |
| 20 | O(2^N) | 1,048,576 | O |
| 25 | O(2^N) | 33,554,432 | 조심 |

---

## 체크리스트

구현 시 확인할 항목:

- [ ] 입력 크기가 완전탐색 가능한가?
- [ ] 순열 vs 조합: 순서가 중요한가?
- [ ] 중복 제거: `set()` 사용했는가?
- [ ] 캐시 활용: 반복 계산 줄였는가?
- [ ] 가지치기: 불필요한 탐색 줄였는가?

---

## 관련 문제 유형

| 문제 | 패턴 |
|------|------|
| 소수 찾기 | 순열 + 소수 판별 |
| 카펫 | 약수 탐색 |
| 모의고사 | 순환 패턴 매칭 |
| 피로도 | 순열 + 조건부 탐색 |
| 모음사전 | 중복 순열 |

---

## 참고

- `/GEMINI.md` - 전체 스타일 가이드
- `/DFS/GEMINI.md` - DFS/백트래킹 패턴

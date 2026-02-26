# [괄호 회전하기]
- 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/76502

#스택 #문자열회전 #완전탐색

## 풀이 과정

### 핵심 아이디어
- 문자열 슬라이싱으로 회전 구현
- 스택으로 괄호 유효성 검증
- 모든 회전 경우의 수를 완전 탐색

### 접근 방법
1. 0부터 문자열 길이-1까지 회전
2. 각 회전마다 `s[i:] + s[:i]`로 회전된 문자열 생성
3. `validate()` 함수로 괄호 짝 맞는지 검증
4. 유효한 경우 카운트 증가

### 코드

```python
def validate(s) -> bool:
    mapping = {')': '(', ']': '[', '}': '{'}
    opens = set(['(', '{', '['])
    stack = []

    for char in s:
        if char in opens:
            stack.append(char)
            continue
        if len(stack) == 0:
            return False
        popped = stack.pop()
        if mapping.get(char) != popped:
            return False
    return len(stack) == 0

def solution(s):
    count = 0
    for i in range(len(s)):
        shifted = s[i:] + s[:i]
        if validate(shifted):
            count += 1
    return count
```

## 회고

### 배운 점
- 문자열 슬라이싱을 활용한 회전 구현

### 어려웠던 부분
- 여러 종류의 괄호를 처리하는 validate 함수 설계

### 개선할 점
- 전역 상수로 중복 생성 제거 필요

---

## 코드 리뷰 평가

### 🔍 개선이 필요한 부분

1. **불필요한 자료구조 생성**
   ```python
   opens = set(['(', '{', '['])  # ← 매 validate 호출마다 생성
   ```
   - `validate`가 여러 번 호출되는데 매번 동일한 set을 생성
   - 전역 상수로 선언하면 메모리와 시간 절약
   - 더 나아가 `char in '({['` 문자열 검사가 더 간단함

2. **중복된 길이 체크**
   ```python
   if len(stack) == 0:
       return False
   # ...
   return len(stack) == 0  # ← 마지막에도 len() 호출
   ```
   - `len(stack) == 0`는 `not stack`으로 간결하게 표현 가능
   - Python에서 빈 리스트는 False, 비어있지 않으면 True

3. **불필요한 continue 문**
   ```python
   if char in opens:
       stack.append(char)
       continue  # ← 어차피 다음 if는 실행 안 됨

   if len(stack) == 0:  # ← else로 처리 가능
       return False
   ```
   - `continue` 대신 `else`를 사용하면 의도가 더 명확
   - 열린 괄호가 아니면 닫힌 괄호라는 로직이 분명해짐

4. **중복 조회 연산**
   ```python
   popped = stack.pop()
   found = mapping.get(char)  # ← char는 닫힌 괄호 확정
   if found != popped:
   ```
   - `mapping.get(char)`를 변수에 저장했지만 이름이 `found`로 부적절
   - `get`보다 `mapping[char]`가 직접적 (어차피 닫힌 괄호만 옴)

### ✅ 구조적 개선 방안

**1. 상수를 전역으로 분리**
```python
# 현재 방식 (문제있음)
def validate(s) -> bool:
    mapping = {')': '(', ']': '[', '}': '{'}
    opens = set(['(', '{', '['])  # 매번 생성
    # ...

# 개선안: 전역 상수
MAPPING = {')': '(', ']': '[', '}': '{'}
OPENS = '({['  # set보다 문자열이 간단

def validate(s) -> bool:
    stack = []
    for char in s:
        if char in OPENS:
            stack.append(char)
        # ...
```
→ 반복 생성 제거, 메모리 효율 향상

**2. Pythonic한 표현 활용**
```python
# 현재 방식 (문제있음)
if len(stack) == 0:
    return False
return len(stack) == 0

# 개선안
if not stack:
    return False
return not stack
```
→ 가독성 향상, Python 관례 준수

**3. 논리 흐름 명확화**
```python
def validate(s) -> bool:
    stack = []
    for char in s:
        if char in '({[':
            stack.append(char)
        else:  # 닫힌 괄호
            if not stack or MAPPING[char] != stack.pop():
                return False
    return not stack
```
→ continue 제거, if-else로 명확한 분기

**4. 최적화된 버전 (추천)**
```python
PAIRS = {')': '(', ']': '[', '}': '{'}

def validate(s):
    stack = []
    for char in s:
        if char in '({[':
            stack.append(char)
        elif not stack or PAIRS[char] != stack.pop():
            return False
    return not stack

def solution(s):
    return sum(validate(s[i:] + s[:i]) for i in range(len(s)))
```
→ 제너레이터 표현식으로 count 로직 간결화
→ 전역 상수로 중복 생성 제거

### 💡 다른 활용 아이디어

1. **회전 없이 O(1) 공간으로 검증**
   ```python
   # 문자열을 실제로 복사하지 않고 인덱스만 조정
   def validate_rotated(s, offset):
       stack = []
       n = len(s)
       for i in range(n):
           char = s[(i + offset) % n]
           # ... 검증 로직
   ```

2. **특정 회전 위치만 검사 (휴리스틱)**
   ```python
   # 열린 괄호로 시작하는 위치만 검사
   def solution_optimized(s):
       count = 0
       for i in range(len(s)):
           if s[i] in '({[':  # 열린 괄호로만 시작
               if validate(s[i:] + s[:i]):
                   count += 1
       return count
   ```

3. **괄호 균형 미리 체크**
   ```python
   from collections import Counter

   def solution_with_precheck(s):
       # 각 괄호 쌍의 개수가 맞지 않으면 0 반환
       c = Counter(s)
       if c['('] != c[')'] or c['['] != c[']'] or c['{'] != c['}']:
           return 0
       # 이후 회전 검사
   ```

4. **괄호 종류별 깊이 추적**
   ```python
   def validate_with_depth(s):
       depths = {'(': 0, '[': 0, '{': 0}
       pairs = {')': '(', ']': '[', '}': '{'}

       for char in s:
           if char in depths:
               depths[char] += 1
           else:
               opener = pairs[char]
               if depths[opener] == 0:
                   return False
               depths[opener] -= 1
       return all(d == 0 for d in depths.values())
   ```

### 🎯 복잡도 분석

**시간 복잡도**: O(N²)
- 외부 루프: N번 회전 (N = 문자열 길이)
- 내부 validate: 각 O(N) 순회
- 문자열 슬라이싱: O(N) (새 문자열 생성)
- 총합: N × (N + N) = O(N²)

**공간 복잡도**: O(N)
- 슬라이싱으로 생성되는 문자열: O(N)
- 스택 최대 크기: O(N) (모두 열린 괄호일 때)
- 총 O(N)

**개선 가능성**:
- 문자열 복사 없이 인덱스로 회전 처리: 공간 O(N) → O(N/2) (스택만)
- 하지만 시간복잡도는 여전히 O(N²) (회전 × 검증)

### 📊 종합 평가

문제 해결 접근은 정확하고 코드도 잘 작동합니다. 문자열 슬라이싱을 활용한 회전 구현은 Python다운 방법입니다.

**자료구조 낭비**: 가장 큰 문제는 `validate` 함수가 호출될 때마다 `mapping`과 `opens` 자료구조를 새로 생성한다는 점입니다. 최악의 경우 N번 호출되므로 불필요한 메모리 할당이 N번 발생합니다. 전역 상수로 선언하면 단 한 번만 생성됩니다.

**Pythonic 표현 부족**: `len(stack) == 0` 대신 `not stack`을 사용하는 것이 Python 관례입니다. 더 짧고 가독성도 좋습니다. 또한 `continue` 없이 `if-else`로 처리하면 논리 흐름이 더 명확해집니다.

**불필요한 변수**: `found = mapping.get(char)` 부분에서 변수를 만들 필요가 없습니다. 어차피 닫힌 괄호만 오므로 `mapping[char]`로 직접 접근해도 안전하고, 비교문에서 바로 사용하면 더 간결합니다.

**슬라이싱 활용**: 회전 구현에서 `s[i:] + s[:i]`를 사용한 것은 훌륭합니다. 회고에서 "슬라이싱 활용하면 좋겠다"고 써놨는데, 이미 완벽하게 활용하고 있습니다!

전반적으로 문제를 정확히 이해하고 해결했지만, Python 관례와 효율성 측면에서 개선 여지가 있습니다. 전역 상수 활용과 Pythonic 표현만 적용해도 훨씬 깔끔한 코드가 될 것입니다.

---
**복잡도**: O(N²) 시간, O(N) 공간
**풀이 날짜**: 2025-11-01

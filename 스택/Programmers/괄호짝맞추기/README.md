# [괄호 짝 맞추기]

#스택 #카운터 #조기종료

## 풀이 과정

### 핵심 아이디어
- 스택 자료구조 대신 카운터 변수로 단순화
- 조기 종료 조건으로 불필요한 순회 방지

### 접근 방법
1. `opens` 카운터로 열린 괄호 개수 추적
2. 여는 괄호 `(` 만나면 +1
3. 닫는 괄호 `)` 만나면 -1
4. **조기 종료**: 카운터가 0인데 닫는 괄호가 나오면 즉시 False 반환
5. 순회 완료 후 카운터가 0이면 True, 아니면 False

### 코드

```python
def solution(s):
    opens = 0
    for char in s:
        if opens == 0 and char == ')':
            return False
        if char == '(':
            opens += 1
        if char == ')':
            opens -= 1
    return opens == 0
```

---

## 코드 리뷰 평가

### 🔍 개선이 필요한 부분

1. **중복된 문자 검사**
   ```python
   if char == '(':
       opens += 1
   if char == ')':  # ← 위에서 '('를 체크했는데 또 검사
       opens -= 1
   ```
   - 괄호는 `(` 또는 `)` 둘 중 하나인데, 두 번 비교하고 있음
   - `elif`를 사용하거나 삼항 연산자로 개선 가능

2. **불필요한 조건 검사 순서**
   ```python
   if opens == 0 and char == ')':  # 조기 종료
       return False
   if char == '(':  # ← 위에서 이미 ')'가 아님을 확인했는데 또 검사
       opens += 1
   ```
   - 조기 종료 조건을 통과했으면 `char != ')'` 임이 확정
   - 하지만 다시 `char == '('`를 검사하는 비효율 존재

3. **변수명의 문법적 오류**
   ```python
   opens = 0  # ← 동사를 명사처럼 사용
   ```
   - `opens`는 "연다"는 동사인데 카운터 변수명으로 부적절
   - `open_count`, `open_brackets`, `depth` 등이 더 명확

### ✅ 구조적 개선 방안

**1. elif로 중복 검사 제거**
```python
# 현재 방식 (문제있음)
if char == '(':
    opens += 1
if char == ')':  # 항상 검사됨
    opens -= 1

# 개선안: elif 사용
if char == '(':
    opens += 1
elif char == ')':  # '('가 아닐 때만 검사
    opens -= 1
```
→ 불필요한 비교 연산 50% 감소

**2. 삼항 연산자로 간결화**
```python
def solution(s):
    depth = 0
    for char in s:
        if depth == 0 and char == ')':
            return False
        depth += 1 if char == '(' else -1
    return depth == 0
```
→ 코드 라인 수 감소, 가독성 향상

**3. 논리적으로 더 명확한 구조**
```python
def solution(s):
    depth = 0
    for char in s:
        if char == '(':
            depth += 1
        else:  # char == ')'
            if depth == 0:
                return False
            depth -= 1
    return depth == 0
```
→ 조기 종료 조건을 자연스러운 흐름에 배치
→ 닫는 괄호 처리 시점에 검사하므로 논리적으로 명확

**4. 더 극단적인 최적화 (가독성 trade-off)**
```python
def solution(s):
    depth = 0
    for char in s:
        depth += 1 if char == '(' else -1
        if depth < 0:
            return False
    return depth == 0
```
→ 조기 종료를 `depth < 0`로 통합
→ 가장 짧지만 의도 파악이 약간 어려울 수 있음

### 💡 다른 활용 아이디어

1. **여러 종류의 괄호 처리**
   ```python
   # {}, [], () 모두 처리
   def solution(s):
       stack = []
       pairs = {'(': ')', '{': '}', '[': ']'}
       for char in s:
           if char in pairs:
               stack.append(char)
           elif not stack or pairs[stack.pop()] != char:
               return False
       return len(stack) == 0
   ```

2. **괄호 깊이 추적**
   ```python
   def max_depth(s):
       depth = max_depth_seen = 0
       for char in s:
           depth += 1 if char == '(' else -1
           max_depth_seen = max(max_depth_seen, depth)
       return max_depth_seen
   ```

3. **괄호 자동 완성**
   ```python
   def auto_complete(s):
       # "(()" → "(())"
       opens = 0
       result = []
       for char in s:
           result.append(char)
           opens += 1 if char == '(' else -1
       result.extend([')'] * opens)  # 남은 열린 괄호 닫기
       return ''.join(result)
   ```

4. **괄호 제거 최소 개수**
   ```python
   def min_remove(s):
       # 유효하게 만들기 위해 제거해야 할 최소 괄호 개수
       opens = closes = 0
       for char in s:
           if char == '(':
               opens += 1
           elif char == ')':
               if opens > 0:
                   opens -= 1
               else:
                   closes += 1
       return opens + closes
   ```

### 🎯 복잡도 분석

**시간 복잡도**: O(N)
- N = 문자열 길이
- 각 문자를 정확히 한 번씩 순회
- 최악의 경우에도 전체 문자열 순회 (조기 종료 없을 때)

**공간 복잡도**: O(1)
- 카운터 변수 하나만 사용
- 입력 크기와 무관하게 일정한 메모리

### 📊 종합 평가

핵심 아이디어는 훌륭합니다. 스택 문제를 카운터로 단순화한 것은 매우 영리한 접근이고, 조기 종료 최적화도 적절합니다.

**논리적 비효율**: 가장 큰 문제는 `if-if` 구조입니다. 조기 종료 검사 후에도 모든 문자에 대해 두 번의 비교 연산을 수행하고 있습니다. 괄호는 항상 `(` 또는 `)`이므로 첫 번째 검사가 거짓이면 두 번째는 자동으로 참입니다. `elif`를 사용하면 불필요한 비교를 50% 줄일 수 있습니다.

**변수명 문제**: `opens`는 동사형으로 "연다"는 의미인데, 숫자를 저장하는 카운터로 사용했습니다. `open_count`, `depth`, `balance` 등 명사형이 더 자연스럽습니다.

**조기 종료 위치**: 현재는 루프 시작 부분에서 검사하지만, 닫는 괄호를 만났을 때 검사하는 것이 논리적으로 더 명확합니다. "`)`를 처리하는데 짝이 없네? → False" 흐름이 자연스럽습니다.

시간복잡도는 최적이고 공간복잡도도 O(1)로 완벽합니다. 구조만 조금 다듬으면 코딩테스트 모범 답안 수준이 될 것입니다.

---
**복잡도**: O(N) 시간, O(1) 공간
**풀이 날짜**: 2025-10-31

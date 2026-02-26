# [문제명]
- 링크 : 

```
#태그1 #태그2 #태그3
```

## 풀이 과정

### 핵심 아이디어
-

### 접근 방법
1.
2.

### 코드

```python
def solution():
    pass
```

## 회고

### 배운 점
-

### 어려웠던 부분
-

### 개선할 점
-

## 평가

### 개선할 점

1. **해시 충돌 처리 부재**
   - 현재 구현은 Rolling Hash를 사용하지만, 해시 충돌 가능성을 완전히 무시하고 있습니다
   - `hash_list`를 리스트로 관리하면서 `in` 연산자로 검색하면 O(n) 시간이 소요됩니다
   - 해시 테이블(set)을 사용하면 O(1)로 개선 가능: `hash_set = set(hash_list)`
   - 하지만 더 근본적인 문제는 해시 충돌 시 원본 문자열 비교 없이 True를 반환한다는 점입니다

2. **불필요한 해시 함수 사용**
   - Python의 내장 자료구조를 사용하면 더 간단하고 안전합니다
   - `set(string_list)`를 사용하여 직접 문자열을 저장하고 검색하면 해시 충돌 걱정 없이 정확한 결과를 얻을 수 있습니다
   - 커스텀 해시 함수가 필요한 특별한 제약이 없다면 Python의 내장 해시를 사용하는 것이 더 안전합니다

3. **비효율적인 결과 리스트 구성**
   - `result.append(True)` / `result.append(False)` 대신 리스트 컴프리헨션 사용 가능
   - `return [query_hash in hash_set for query in query_list]` 형태로 간결하게 작성 가능

4. **복잡도 분석 누락**
   - 현재 시간 복잡도: O(n*m + q*m) (n: string_list 길이, m: 평균 문자열 길이, q: query_list 길이)
   - hash_list에서 `in` 연산이 O(n)이므로 전체 복잡도는 O(n*m + q*(m+n))
   - set을 사용하면 O(n*m + q*m)로 개선 가능

### 잘한 점

1. **표준 Rolling Hash 구현**
   - p=31, m=1_000_000_007을 사용한 것은 문자열 해싱의 표준 관행입니다
   - 소수를 base와 modulo로 사용하여 해시 분포를 균등하게 유지했습니다

2. **코드 구조 분리**
   - `hash_string` 함수를 별도로 분리하여 재사용성과 가독성을 높였습니다
   - 단일 책임 원칙을 잘 따르고 있습니다

3. **명확한 변수명**
   - `hash_value`, `query_hash` 등 변수명이 의도를 명확하게 전달합니다

### 다른 응용 방안

1. **Rabin-Karp 알고리즘 (패턴 매칭)**

   이 Rolling Hash 기법은 문자열 패턴 매칭의 Rabin-Karp 알고리즘의 핵심입니다.

   **문제**: 텍스트 T에서 패턴 P를 찾기
   - 예: T = "abcdefgh", P = "cde" → 인덱스 2에서 발견

   **핵심 아이디어**:
   1. 패턴 P의 해시값을 미리 계산: `hash(P)`
   2. 텍스트 T를 슬라이딩 윈도우로 이동하며 각 부분 문자열의 해시 계산
   3. 해시값이 같으면 실제 문자열 비교 (해시 충돌 검증)

   **슬라이딩 윈도우 최적화**:
   ```python
   # 기존 윈도우: "abc" (hash = h1)
   # 새 윈도우:  "bcd" (hash = h2)
   # h2 = (h1 - hash('a')) * p + hash('d')  ← O(1) 시간!
   ```

   일반적인 방법은 매번 O(m)씩 해시를 재계산해야 하지만,
   Rolling Hash는 이전 해시값을 재활용하여 **O(1)에 업데이트**합니다.

   **시간 복잡도**:
   - 전처리: O(m) - 패턴 해시 계산
   - 검색: O(n) - 텍스트를 한 번만 순회
   - 총: **O(n+m)** (최악의 경우 O(nm)이지만 평균적으로 매우 빠름)

   **활용 사례**:
   - 문서에서 키워드 검색
   - 표절 검사 (긴 텍스트에서 복사된 부분 찾기)
   - DNA 서열 분석 (특정 유전자 패턴 찾기)
   - 바이러스 백신 (악성코드 시그니처 검색)

2. **중복 문자열 찾기**
   - 긴 텍스트에서 반복되는 부분 문자열을 찾을 때 유용합니다
   - 예: 표절 검사, DNA 시퀀스 분석

3. **문자열 비교 최적화**
   - 매우 긴 문자열들을 비교할 때 먼저 해시값을 비교하고, 같을 때만 실제 문자열 비교를 수행
   - 이를 통해 평균 시간을 크게 단축할 수 있습니다

4. **슬라이딩 윈도우 해싱 (Rolling Hash의 핵심)**

   고정 길이 부분 문자열의 해시를 **O(1) 시간**에 업데이트하는 기법입니다.

   **문제 상황**:
   ```
   텍스트: "abcdefgh"
   윈도우 크기: 3

   윈도우1: "abc" → hash1 계산
   윈도우2: "bcd" → hash2를 처음부터 계산? NO!
   윈도우3: "cde" → hash3를 처음부터 계산? NO!
   ```

   **일반적인 방법 (비효율)**:
   ```python
   def hash_string(s):
       hash_value = 0
       for char in s:  # O(m) 시간!
           hash_value = (hash_value * p + ord(char)) % mod
       return hash_value

   # 매번 O(m) → 총 O(n*m)
   for i in range(len(text) - m + 1):
       window = text[i:i+m]
       h = hash_string(window)  # 매번 3글자 전부 계산
   ```

   **슬라이딩 윈도우 방법 (효율적)**:

   핵심 공식: **이전 해시값을 재활용!**
   ```
   hash("abc") = a*p² + b*p¹ + c*p⁰
   hash("bcd") = b*p² + c*p¹ + d*p⁰

   관계식:
   hash("bcd") = (hash("abc") - a*p²) * p + d
                = (hash("abc") - 첫글자 기여분) * p + 새글자
   ```

   **구현 코드**:
   ```python
   def rabin_karp(text, pattern):
       p = 31
       m = 1_000_000_007
       n, k = len(text), len(pattern)

       # p^k 미리 계산 (첫 글자 제거용)
       p_pow = pow(p, k, m)  # p^k % m

       # 패턴 해시 계산
       pattern_hash = 0
       for char in pattern:
           pattern_hash = (pattern_hash * p + ord(char)) % m

       # 첫 윈도우 해시 계산
       window_hash = 0
       for i in range(k):
           window_hash = (window_hash * p + ord(text[i])) % m

       result = []
       if window_hash == pattern_hash:
           # 해시 충돌 검증
           if text[0:k] == pattern:
               result.append(0)

       # 슬라이딩 윈도우 (핵심!)
       for i in range(1, n - k + 1):
           # 이전 윈도우: text[i-1:i-1+k]
           # 새 윈도우:   text[i:i+k]

           old_char = text[i - 1]  # 제거할 문자
           new_char = text[i + k - 1]  # 추가할 문자

           # O(1) 해시 업데이트!
           window_hash = (window_hash - ord(old_char) * p_pow) % m
           window_hash = (window_hash * p + ord(new_char)) % m
           window_hash = (window_hash + m) % m  # 음수 방지

           if window_hash == pattern_hash:
               # 해시 충돌 검증
               if text[i:i+k] == pattern:
                   result.append(i)

       return result
   ```

   **시각적 이해**:
   ```
   text = "abcdefgh", pattern = "cde"

   Step 1: window = "abc"
           hash = a*31² + b*31¹ + c*31⁰

   Step 2: window = "bcd"
           1) 'a' 제거: hash - a*31²
           2) 왼쪽 시프트: (hash - a*31²) * 31
           3) 'd' 추가: (hash - a*31²) * 31 + d

           결과: b*31² + c*31¹ + d*31⁰  ✓

   Step 3: window = "cde"
           1) 'b' 제거: hash - b*31²
           2) 왼쪽 시프트: (hash - b*31²) * 31
           3) 'e' 추가: (hash - b*31²) * 31 + e

           결과: c*31² + d*31¹ + e*31⁰  ✓
           패턴 해시와 일치! → 실제 문자열 비교 → 인덱스 2 반환
   ```

   **시간 복잡도 비교**:
   - 일반 방법: O(n * m) - n개 윈도우, 각각 m글자 해싱
   - 슬라이딩 윈도우: O(n + m) - 첫 해시 O(m), 이후 각 O(1)

   **주의사항**:
   1. `p_pow = p^k % m` 미리 계산 필요 (첫 글자 제거용)
   2. 음수 방지: `(hash + m) % m` 처리
   3. 해시 충돌 시 반드시 실제 문자열 비교

   **실전 활용**:
   - 긴 텍스트에서 고정 길이 패턴 찾기 (예: 6자리 우편번호)
   - 윈도우 크기 k인 모든 부분 문자열의 중복 찾기
   - 문자열 유사도 비교 (k-gram 해싱)

### 종합 평가

**롤링 해시 학습 목적으로는 훌륭한 구현**입니다. p=31, m=1_000_000_007을 사용한 표준 Polynomial Rolling Hash를 정확하게 구현했고, 코드 구조도 깔끔합니다.

하지만 **실전 활용을 위해서는 반드시 개선이 필요**합니다:

**1. 해시 충돌 처리의 중요성**
현재 구현의 가장 큰 학습 포인트는 "해시는 확률적 자료구조"라는 점입니다. 아무리 좋은 해시 함수라도 충돌 가능성이 존재하므로, 실제 응용에서는:
- 해시값이 같을 때 원본 문자열을 비교하는 검증 단계 필수
- 또는 이중 해시(서로 다른 p, m 사용)로 충돌 확률을 극도로 낮춤

**2. 자료구조 선택**
`hash_list`를 리스트로 사용하면 `in` 연산이 O(n)이 되어 해시의 장점이 사라집니다. `hash_set = set(hash_list)`로 변경하면 O(1) 조회가 가능합니다. 이것은 해시 테이블의 핵심 개념을 실습하는 중요한 부분입니다.

**3. 학습 가치**
이 구현을 통해 다음을 학습할 수 있습니다:
- 문자열을 정수로 변환하는 해시 함수의 원리
- Rabin-Karp 알고리즘의 기초
- 해시 충돌과 확률의 관계
- 모듈로 연산을 통한 오버플로우 방지

**다음 학습 단계 제안**:
1. set을 사용한 성능 개선 실습
2. 해시 충돌이 발생하는 테스트 케이스 만들어보기
3. 슬라이딩 윈도우 방식으로 해시 업데이트하는 Rabin-Karp 구현
4. 이중 해시 기법 적용해보기

롤링 해시의 본질을 이해하고 직접 구현해본 것은 매우 가치 있는 학습 경험입니다. 이제 한 단계 더 나아가 실전에서 안전하게 사용할 수 있는 방법들을 익혀보세요.

---
**복잡도**: O(n*m + q*(m+n)) → set 사용 시 O(n*m + q*m) (n: string_list 길이, m: 평균 문자열 길이, q: query_list 길이)
**풀이 날짜**:

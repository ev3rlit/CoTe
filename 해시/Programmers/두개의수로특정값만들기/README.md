# [두개의수로특정값만들기]
- 링크 : 

```
#해시
```

## 풀이 과정

### 핵심 아이디어
- 두 개의 수를 더하여 특정 값을 만드는 문제로, 해시 테이블을 사용하여 효율적으로 해결할 수 있다.
- 계수정렬 아이디어를 활용하여 주어진 수들의 존재 여부를 빠르게 확인할 수 있다.

### 접근 방법
1. target 크기의 배열을 생성하여 해시 테이블로 활용 (인덱스 = 숫자, 값 = 존재 여부)
2. 첫 번째 순회: arr의 모든 숫자를 해시 테이블에 표시
3. 두 번째 순회: 각 숫자에 대해 보수(target - num)가 해시 테이블에 존재하는지 O(1)에 확인
4. 같은 숫자를 두 번 사용하는 경우(target - num == num)는 제외

### 코드

```python
def solution(arr, target):
    hash = [0] * (target + 1)

    for num in arr:
        if num <= target:
            hash[num] = 1

    for num in arr:
        if num >= target:
            continue

        if target - num == num:
            continue

        if hash[target-num]:
            return True

    return False
```

## 회고

### 배운 점
- 해시의 핵심은 O(1) 조회 시간이며, 이를 배열 인덱스로 구현할 수 있음
- Two Sum 패턴의 기본: "보수(complement) 검색" 전략
- 전처리(preprocessing) 방식으로 해시 테이블을 먼저 구축하면 이후 탐색이 효율적

### 어려웠던 부분
- 같은 숫자를 두 번 사용하는 엣지 케이스 처리 (target=6, num=3일 때 3+3=6)
- 배열 인덱스 범위를 벗어나지 않도록 경계 조건 체크

### 개선할 점
- Python의 set/dict를 사용하면 메모리 효율적이고 일반화된 해시 구현 가능
- 한 번의 순회로 해결하는 최적화 버전 학습 필요

## 평가

### 개선할 점

1. **메모리 비효율성 (공간 복잡도 O(target))**
   - 현재: `hash = [0] * (target + 1)` → target 값에 비례한 메모리 사용
   - 문제 상황: `arr = [1, 1000000], target = 1000001`일 때 100만 크기 배열 생성하지만 실제로는 2개만 저장
   - 개선 방향: `set(arr)` 사용 시 공간 복잡도 O(n)으로 개선 (n = arr의 길이)

2. **음수 처리 불가**
   - 배열 인덱스는 음수를 지원하지 않아 `arr = [-5, 3, 8], target = 3` 같은 경우 처리 불가
   - dict/set 기반 해시는 음수도 key로 사용 가능

3. **두 번 순회의 비효율**
   - 첫 번째 순회로 해시 구축, 두 번째 순회로 검색
   - 한 번의 순회로 "이전에 본 숫자인지" 확인하며 동시에 처리 가능:
     ```python
     seen = set()
     for num in arr:
         if target - num in seen:
             return True
         seen.add(num)
     ```

4. **IndexError 위험성**
   - solution.py:16에서 `hash[target-num]` 접근 시, 경계 체크가 없으면 에러 발생 가능
   - 현재는 solution.py:10-11에서 방어하지만, dict/set은 자동으로 안전

### 잘한 점

1. **해시의 핵심 개념 이해 (O(1) 조회)**
   - solution.py:16의 `if hash[target-num]:`에서 보수를 즉시 찾는 방식이 해시의 본질
   - 이중 반복문 O(n²) 대신 O(n) 시간 복잡도 달성

2. **계수 정렬(Counting Sort) 아이디어 활용**
   - "배열 인덱스 = 값" 패턴으로 해시 테이블 구현
   - 해시 학습 초기에 직관적으로 이해하기 좋은 접근

3. **중요한 엣지 케이스 처리** (solution.py:13-14)
   - `target - num == num` 체크로 같은 원소를 두 번 사용하는 경우 방지
   - 해시 문제에서 자주 나오는 함정 회피

4. **경계 조건 체크** (solution.py:6, 10-11)
   - target보다 큰 숫자 필터링으로 불필요한 처리 제거
   - 배열 인덱스 범위 초과 방지

5. **Two Sum 패턴의 정확한 구현**
   - "현재 숫자 + 보수 = target" 로직을 명확히 표현
   - 코딩 테스트의 가장 기본적이면서 중요한 해시 패턴 학습

### 다른 응용 방안

1. **Python set을 사용한 일반화된 해시 구현**
   ```python
   def solution_set(arr, target):
       seen = set()
       for num in arr:
           if target - num in seen:
               return True
           seen.add(num)
       return False
   ```
   - 음수, 큰 숫자 모두 처리 가능
   - 공간 복잡도 O(n)으로 최적화
   - 한 번의 순회로 해결

2. **인덱스 반환 버전 (LeetCode Two Sum)**
   ```python
   def two_sum_indices(arr, target):
       hash_map = {}  # {값: 인덱스}
       for i, num in enumerate(arr):
           if target - num in hash_map:
               return [hash_map[target - num], i]
           hash_map[num] = i
       return None
   ```
   - 두 숫자의 인덱스를 반환
   - dict를 사용해 값과 위치를 동시에 저장

3. **K개 합 문제로 확장**

   **3Sum 문제** (세 숫자의 합 = target)
   ```python
   def three_sum(arr, target):
       """
       세 숫자의 합이 target인 조합이 있는지 확인
       접근: 정렬 + 투 포인터 + 해시
       """
       arr.sort()  # 정렬 필요
       n = len(arr)

       for i in range(n - 2):
           # 첫 번째 숫자 고정
           # 나머지 두 숫자는 Two Sum 문제로 해결
           needed = target - arr[i]
           seen = set()

           for j in range(i + 1, n):
               complement = needed - arr[j]
               if complement in seen:
                   return True
               seen.add(arr[j])

       return False

   # 예시: [1, 2, 3, 4, 5], target=9
   # i=0 (arr[0]=1) → 나머지에서 8 만들기 → 3+5=8 ✓
   ```

   **3Sum 모든 조합 찾기** (LeetCode 15번 스타일)
   ```python
   def three_sum_all(arr, target):
       """
       세 숫자의 합이 target인 모든 조합 반환
       중복 제거 포함
       """
       arr.sort()
       result = []
       n = len(arr)

       for i in range(n - 2):
           # 중복 방지: 같은 값은 한 번만 첫 번째 위치로
           if i > 0 and arr[i] == arr[i-1]:
               continue

           # Two Sum with Two Pointers
           left, right = i + 1, n - 1

           while left < right:
               current_sum = arr[i] + arr[left] + arr[right]

               if current_sum == target:
                   result.append([arr[i], arr[left], arr[right]])

                   # 중복 제거
                   while left < right and arr[left] == arr[left + 1]:
                       left += 1
                   while left < right and arr[right] == arr[right - 1]:
                       right -= 1

                   left += 1
                   right -= 1
               elif current_sum < target:
                   left += 1
               else:
                   right -= 1

       return result

   # 예시: [-1, 0, 1, 2, -1, -4], target=0
   # 결과: [[-1, -1, 2], [-1, 0, 1]]
   ```

   **4Sum 문제** (네 숫자의 합 = target)
   ```python
   def four_sum(arr, target):
       """
       네 숫자의 합이 target인 조합이 있는지 확인
       접근: 두 숫자 고정 + Two Sum 해시
       """
       arr.sort()
       n = len(arr)

       for i in range(n - 3):
           for j in range(i + 1, n - 2):
               # 두 숫자 고정 (arr[i], arr[j])
               # 나머지 두 숫자는 Two Sum으로 해결
               needed = target - arr[i] - arr[j]
               seen = set()

               for k in range(j + 1, n):
                   complement = needed - arr[k]
                   if complement in seen:
                       return True
                   seen.add(arr[k])

       return False

   # 시간 복잡도: O(n³)
   ```

   **N-Sum 일반화** (재귀 + 해시)
   ```python
   def n_sum(arr, target, n):
       """
       n개 숫자의 합이 target인 조합이 있는지 확인
       재귀를 통한 일반화
       """
       def n_sum_helper(start, n, target):
           # Base case: Two Sum
           if n == 2:
               seen = set()
               for i in range(start, len(arr)):
                   complement = target - arr[i]
                   if complement in seen:
                       return True
                   seen.add(arr[i])
               return False

           # Recursive case: 하나 고정 + (n-1) Sum
           for i in range(start, len(arr) - n + 1):
               if n_sum_helper(i + 1, n - 1, target - arr[i]):
                   return True

           return False

       arr.sort()
       return n_sum_helper(0, n, target)

   # 사용 예시
   # n_sum([1, 2, 3, 4, 5], 15, 5)  # 5개 합 = 15 → True (1+2+3+4+5)
   # n_sum([1, 2, 3, 4, 5], 10, 3)  # 3개 합 = 10 → True (2+3+5)
   ```

   **핵심 패턴 정리**:
   - 2Sum: 해시 O(n)
   - 3Sum: 1개 고정 + 2Sum → O(n²)
   - 4Sum: 2개 고정 + 2Sum → O(n³)
   - kSum: (k-2)개 고정 + 2Sum → O(n^(k-1))

4. **중복 허용 버전**
   - 같은 값이 배열에 여러 개 있을 때 처리
   - Counter를 사용한 빈도 추적:
     ```python
     from collections import Counter
     count = Counter(arr)
     for num in arr:
         complement = target - num
         if num == complement and count[num] >= 2:
             return True
         elif num != complement and complement in count:
             return True
     ```

### 해시 학습 관점 종합 평가

이 풀이는 **해시의 본질(O(1) 조회)**을 배열 인덱스로 구현한 훌륭한 학습 예제입니다. Two Sum 문제의 핵심 패턴인 "보수 검색"을 정확히 이해하고 있으며, 중복 사용 방지와 경계 조건 체크 등 중요한 엣지 케이스도 처리했습니다.

하지만 실전 코딩 테스트 관점에서는 몇 가지 제약이 있습니다. 현재 구현은 target 값에 비례한 메모리를 사용하므로(O(target)), target이 매우 크면 비효율적입니다. 또한 음수를 처리할 수 없고, 두 번의 순회가 필요합니다.

**학습 다음 단계**: Python의 `set`이나 `dict`를 사용한 일반화된 해시 구현을 익히는 것이 중요합니다. 이를 통해 음수, 큰 숫자, 부동소수점 등 모든 경우를 처리할 수 있으며, 한 번의 순회로 문제를 해결할 수 있습니다. 배열 인덱스 방식은 "해시가 왜 빠른지" 이해하는 데 좋지만, 실전에서는 Python의 내장 자료구조를 활용하는 것이 더 유연하고 안전합니다.

코딩 테스트에서 해시 문제는 매우 자주 출제되며, 이 문제에서 배운 "보수 검색" 패턴은 기본 중의 기본입니다. 계수 정렬 아이디어와 해시의 연결고리를 이해한 점이 특히 인상적이며, 이제 dict/set으로 확장하면 해시 마스터가 될 수 있을 것입니다.

---
**복잡도**: 시간 O(n), 공간 O(target) - n은 arr의 길이
**풀이 날짜**: 2025-01-06

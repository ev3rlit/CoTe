# 타겟 넘버

#DFS #BFS #완전탐색 #코딩테스트

## 문제 난이도: 중

## 문제 링크
[프로그래머스 - 타겟 넘버](https://school.programmers.co.kr/learn/courses/30/lessons/43165)

---

## 1. 📊 객관적 분석 및 근거

### 1.1 제약 조건 파악

| 항목 | 값 | 의미 |
|------|-----|------|
| 숫자 개수 (N) | 2 ~ 20개 | 2^20 ≈ 100만, 완전탐색 가능 |
| 각 숫자 범위 | 1 ~ 50 | 합의 범위: -1000 ~ 1000 |
| 타겟 넘버 | 1 ~ 1000 | |

### 1.2 시간 복잡도 역산

**기준**: 1초 ≈ 10^8 연산

| N | 2^N | 결과 |
|---|-----|------|
| 10 | 1,024 | ✅ |
| 15 | 32,768 | ✅ |
| 20 | 1,048,576 | ✅ |

**이 문제의 경우**:
- N ≤ 20이므로 최대 2^20 ≈ 100만
- **결론**: O(2^N) 완전탐색 가능

### 1.3 문제 패턴 인식

**핵심 질문**: 이 문제가 요구하는 것은 무엇인가?

| 관찰 포인트 | 이 문제에서 | 시사점 |
|-------------|-------------|--------|
| 최적해 vs 모든 경우 | 경우의 수 **개수** | 완전탐색 |
| 순서가 중요한가 | ✅ (순서 고정, +/- 선택) | 순열 아닌 조합 |
| 각 원소의 선택 | +숫자 또는 -숫자 | 2가지 분기 |
| 목표 | 합이 target인 경우 카운트 | |

### 1.4 알고리즘 선택 및 논증

#### 🎯 최종 선택: DFS (깊이 우선 탐색)

**선택 근거 (Why this algorithm?)**

1. **문제 구조와의 적합성**
   - 각 숫자마다 **2가지 선택** (+/-)
   - 이진 트리 형태의 탐색 → DFS 적합

2. **제약 조건 충족**
   - 시간 복잡도: O(2^N) → N=20일 때 100만 (✅ 통과)
   - 공간 복잡도: O(N) → 재귀 깊이 최대 20 (✅ 통과)

3. **핵심 인사이트**
   ```
   각 숫자에서 분기:
   - 현재 합 + numbers[i]
   - 현재 합 - numbers[i]
   
   모든 숫자를 사용했을 때 합이 target이면 카운트++
   ```

#### ❌ 기각된 대안들

| 대안 | 복잡도 | 기각 이유 |
|------|--------|-----------|
| BFS | O(2^N) | 가능하지만 메모리 사용량 더 큼 |
| DP | O(N × sum) | 가능하지만 DFS가 더 직관적 |

#### 💡 비슷한 문제에서 이 패턴을 인식하는 법

- **키워드**: "모든 경우", "방법의 수", "선택/비선택"
- **문제 유형**: 각 원소에서 2가지 선택이 있는 경우
- **패턴**: `dfs(index, current_sum)` → 분기 탐색

---

## 2. 🧠 자연어 실행 흐름

1. **DFS 함수 정의**
   - 매개변수: 현재 인덱스, 현재 합

2. **종료 조건**
   - 모든 숫자를 사용했을 때 (index == len(numbers))
   - 합이 target이면 카운트 증가

3. **분기 탐색**
   - 현재 숫자를 더하는 경우: `dfs(index + 1, sum + numbers[index])`
   - 현재 숫자를 빼는 경우: `dfs(index + 1, sum - numbers[index])`

4. **결과 반환**

---

## 3. 💻 Code Implementation

```python
def solution(numbers, target):
    count = [0]  # mutable 객체로 카운트 저장
    
    def dfs(index, current_sum):
        # 종료 조건: 모든 숫자를 사용했을 때
        if index == len(numbers):
            if current_sum == target:
                count[0] += 1
            return
        
        # 분기 1: 현재 숫자를 더하기
        dfs(index + 1, current_sum + numbers[index])
        
        # 분기 2: 현재 숫자를 빼기
        dfs(index + 1, current_sum - numbers[index])
    
    dfs(0, 0)
    return count[0]
```

**복잡도 분석**
- 시간: O(2^N) - 각 숫자마다 2가지 분기
- 공간: O(N) - 재귀 스택 깊이

---

## 4. 다른 풀이 방법

### itertools 활용

```python
from itertools import product

def solution(numbers, target):
    # 모든 +/- 조합 생성
    signs = product([1, -1], repeat=len(numbers))
    
    count = 0
    for sign in signs:
        total = sum(n * s for n, s in zip(numbers, sign))
        if total == target:
            count += 1
    
    return count
```

---

## 5. DFS 트리 시각화

```
numbers = [1, 1, 1], target = 1

                   0
              /         \
           +1             -1
          /   \          /   \
       +1      -1     +1      -1
       / \    / \     / \    / \
     +1  -1 +1 -1   +1  -1 +1  -1
      3   1  1  -1   1  -1 -1  -3
      
target=1인 경우: 3가지 (1, 1, 1)
```

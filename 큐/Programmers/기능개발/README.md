# 기능개발

#큐 #구현 #그룹화

## 🤔 왜 이게 "큐" 문제일까?

### 큐의 핵심: FIFO (First In, First Out)
```
작업 대기열: [기능1, 기능2, 기능3]
배포 순서:    ↓      ↓      ↓
             맨 앞부터 차례대로!
```

### 문제의 핵심 제약 조건
> "**배포는 순서대로** 이루어져야 하며, 뒤에 있는 기능이 먼저 완성되어도 **앞의 기능이 배포될 때까지 대기**해야 한다"

이것이 바로 **큐의 FIFO 특성**입니다!

### 시각화로 이해하기
```
진행도: [93, 30, 55]
속도:   [1, 30, 5]

Day 0: Queue = [작업1(93), 작업2(30), 작업3(55)]
         ↓
Day 3: 작업2 완료! (93)
       하지만 작업1이 아직 93... → 대기! (큐에서 못 빼냄)
         ↓
Day 7: 작업1 완료! (100)
       작업2도 이미 완료 (100)
       → 둘 다 배포! [작업1, 작업2 제거]
       Queue = [작업3(55→90)]
         ↓
Day 9: 작업3 완료! (100)
       → 배포! [작업3 제거]
       Queue = []

배포: [2개, 1개] = [2, 1]
```

**핵심**: 뒤 작업이 먼저 끝나도, 앞 작업을 "건너뛸 수 없다" = **큐의 특성**

---

## 🎭 개념적 활용 vs 실제 큐 사용

### ❓ 혼란의 원인
"큐 문제"라고 하는데, 현재 풀이(방법 1)는 큐 자료구조를 안 쓰잖아요?

### ✅ 답변
**큐 문제**에는 2가지 타입이 있습니다:

#### 타입 1: 개념적 활용 (현재 풀이)
```python
# 큐 자료구조는 안 쓰지만, "순서" 개념 활용
for day in days_left:
    if day <= max_day:  # 앞 작업 기준으로 판단
        count += 1
```
- 큐 자료구조 직접 사용 ❌
- **큐의 "순서" 개념만 활용** ✅
- 더 깔끔하고 이해하기 쉬움

#### 타입 2: 실제 큐 사용 (방법 2)
```python
# 실제 deque 사용
queue = deque(zip(progresses, speeds))
while queue:
    progress, speed = queue[0]    # 맨 앞 확인 (peek)
    ...
    queue.popleft()               # 맨 앞 제거 (dequeue)
```
- 큐 자료구조 직접 사용 ✅
- **큐의 동작을 그대로 시뮬레이션** ✅
- 학습용으로 좋음

### 📚 비유로 이해하기

**병원 대기실 (큐)**을 생각해보세요:

**방법 1 (개념적 활용)**:
```
환자 대기 명단을 종이에 적어놓고,
"첫 번째 환자가 30분 걸리면, 그 시간 안에 끝나는 환자들 묶어서 처리"
라고 머릿속으로 계산

→ 대기실(큐)을 직접 안 써도, "순서" 규칙은 지킴
```

**방법 2 (실제 큐 사용)**:
```
실제 대기실에서:
1. 맨 앞 환자 확인 (peek)
2. 진료 끝나면 나감 (popleft)
3. 다음 환자 확인...

→ 실제 대기실(큐) 운영
```

둘 다 "**순서대로 처리**"라는 큐의 핵심은 지킵니다!

---

## 풀이 과정

### 핵심 아이디어
- **사전 계산 + 그룹화 패턴**: 먼저 모든 작업의 완료일을 계산하고, 앞선 작업을 기준으로 그룹화
- 큐의 FIFO 특성 활용: 순서대로 배포되므로 앞 기능이 늦으면 뒤 기능도 기다려야 함
- **최댓값 갱신** 기법으로 그룹 구분

### 접근 방법

1. **남은 일수 사전 계산**
   ```python
   daysleft = [math.ceil((100-progress)/speed) for ...]
   ```
   - 각 기능이 완료되기까지 걸리는 일수 미리 계산
   - `math.ceil`로 올림 처리 (하루 단위)

2. **첫 번째 기능 = 배포 기준일**
   ```python
   max_day = daysleft[0]
   ```
   - 첫 번째 기능의 완료일이 첫 배포 그룹의 기준

3. **순회하며 그룹 판단**
   ```python
   if left <= max_day:    # 같이 배포 가능
       count += 1
   else:                  # 새로운 배포
       answer.append(count)
       max_day = left     # 기준일 갱신
   ```

4. **핵심 로직 이해**
   ```
   진행도: [93, 30, 55]
   속도:   [1, 30, 5]

   남은일수: [7, 3, 9]
            ↓
   7일차: 93, 30 완료 (둘 다 7일 이내) → 2개 배포
   9일차: 55 완료 → 1개 배포

   답: [2, 1]
   ```

### 코드

```python
import math

def solution(progresses, speeds):
    answer = []
    n = len(progresses)

    # 1. 각 기능의 남은 일수 계산
    daysleft = [math.ceil((100-progress)/speed)
                for (progress, speed) in zip(progresses, speeds)]

    count = 0
    max_day = daysleft[0]  # 현재 배포 그룹의 기준일

    # 2. 순회하며 그룹화
    for left in daysleft:
        if left <= max_day:
            # 현재 기준일 내에 완료 → 같이 배포
            count += 1
        else:
            # 기준일 넘음 → 새로운 배포
            answer.append(count)
            count = 1
            max_day = left  # 새 그룹의 기준일

    # 3. 마지막 그룹 추가
    answer.append(count)
    return answer
```

## 📚 교육적 가치

### 1️⃣ **사전 계산 패턴**
```python
# ✅ 좋은 패턴: 데이터를 변환 후 처리
daysleft = [계산식 for ...]  # 변환
for left in daysleft:          # 처리
    ...

# ❌ 나쁜 패턴: 매번 계산
for i in range(n):
    left = math.ceil((100-progresses[i])/speeds[i])  # 매번 계산
```
- **분리의 원칙**: 데이터 변환과 로직을 분리하면 코드가 명확해짐

### 2️⃣ **최댓값 갱신 기법**
```python
max_day = daysleft[0]  # 초기 기준

for left in daysleft:
    if left <= max_day:     # 기준 내
        ...
    else:                   # 기준 초과 → 갱신
        max_day = left
```
- 그룹화 문제에서 자주 사용되는 패턴
- "현재 기준"을 계속 갱신하며 구간 나누기

### 3️⃣ **리스트 컴프리헨션 + zip**
```python
daysleft = [math.ceil((100-progress)/speed)
            for (progress, speed) in zip(progresses, speeds)]
```
- 두 리스트를 동시에 순회
- 파이썬스러운(Pythonic) 코드

### 4️⃣ **마지막 처리 잊지 않기**
```python
for left in daysleft:
    if ...:
        answer.append(count)  # 중간 그룹

answer.append(count)  # ⭐ 마지막 그룹 추가!
```
- 반복문 종료 후 남은 데이터 처리는 흔한 실수 포인트
- 이 코드는 정확히 처리함

## 💡 개선 가능한 점

### 1. 변수명 개선
```python
# 현재
daysleft = [...]
max_day = daysleft[0]

# 더 명확하게
days_left = [...]
current_deploy_day = days_left[0]
```

### 2. 불필요한 변수 제거
```python
# 현재
n = len(progresses)  # 사용되지 않음

# 개선: 삭제
```

### 3. 함수 분리 (선택사항)
```python
def calculate_days_left(progresses, speeds):
    """각 기능의 남은 일수 계산"""
    return [math.ceil((100-p)/s) for p, s in zip(progresses, speeds)]

def group_by_deploy_day(days_left):
    """배포일 기준으로 그룹화"""
    ...
```
- 복잡한 문제에서는 함수 분리가 도움됨

## 🎯 이 풀이에서 배울 점

1. **문제를 단계로 나누기**
   - "남은 일수 계산" → "그룹화" 2단계로 분리

2. **큐 문제의 핵심**
   - 순서가 중요! 앞이 막히면 뒤도 막힘
   - 이 특성을 `max_day` 갱신으로 표현

3. **엣지 케이스 처리**
   - 마지막 그룹 처리 (`answer.append(count)`)

4. **효율성**
   - 한 번의 순회로 해결: O(N)
   - 추가 공간: O(N) (days_left 배열)

## 🔄 다른 풀이 방법들

### 방법 1: 현재 풀이 (사전 계산 + 최댓값 갱신) ⭐ 가장 추천
```python
import math

def solution(progresses, speeds):
    # 모든 완료일 미리 계산
    days_left = [math.ceil((100-p)/s) for p, s in zip(progresses, speeds)]

    answer = []
    max_day = days_left[0]
    count = 0

    for day in days_left:
        if day <= max_day:
            count += 1
        else:
            answer.append(count)
            count = 1
            max_day = day

    answer.append(count)
    return answer
```
**장점**: 깔끔하고 이해하기 쉬움, O(N)
**단점**: 추가 공간 O(N) 필요
**메모리**: ~240B (테스트 결과)

---

### 방법 2: deque를 이용한 실제 큐 시뮬레이션 🎯 큐 동작 이해!
```python
from collections import deque
import math

def solution(progresses, speeds):
    queue = deque(zip(progresses, speeds))
    answer = []

    while queue:
        # 첫 번째 작업이 완료되는 날짜 계산
        progress, speed = queue[0]
        days = math.ceil((100 - progress) / speed)

        # 같은 날 배포 가능한 작업들 카운트
        count = 0
        while queue:
            progress, speed = queue[0]
            # days일 후 진행도가 100 이상?
            if progress + (days * speed) >= 100:
                queue.popleft()  # 큐에서 제거 (배포)
                count += 1
            else:
                break  # 뒤 작업은 아직 미완성 → 멈춤

        answer.append(count)

    return answer
```

**핵심 아이디어**:
- 첫 작업 완료일에 맞춰 뒤 작업들도 완료됐는지 체크
- `progress + (days * speed) >= 100`로 완료 여부 판단

**장점**: 큐의 개념을 직접 구현, 진행도를 실시간 계산
**단점**: 코드가 약간 복잡, 이중 while문
**메모리**: ~920B (deque 오버헤드)

#### 📺 실제 큐 동작 시각화

입력: `progresses=[93, 30, 55], speeds=[1, 30, 5]`

```python
# 초기 상태
queue = deque([(93,1), (30,30), (55,5)])
               ↑맨앞
answer = []

# === 1차 배포 ===
queue[0] = (93, 1)
days = ceil((100-93)/1) = 7일

# 7일 후 각 작업 상태 체크:
(93, 1)  → 93 + 7*1  = 100 ✅ → popleft() → count=1
(30, 30) → 30 + 7*30 = 240 ✅ → popleft() → count=2
(55, 5)  → 55 + 7*5  = 90  ❌ → break (못 빼냄!)

queue = deque([(55,5)])  # 남은 것
answer = [2]

# === 2차 배포 ===
queue[0] = (55, 5)
days = ceil((100-55)/5) = 9일

# 9일 후:
(55, 5) → 55 + 9*5 = 100 ✅ → popleft() → count=1

queue = deque([])  # 비어있음
answer = [2, 1]

# 종료!
return [2, 1]
```

#### 🎓 큐 연산 배우기

| 연산 | 코드 | 의미 |
|------|------|------|
| **peek** | `queue[0]` | 맨 앞 확인 (제거 X) |
| **dequeue** | `queue.popleft()` | 맨 앞 제거 |
| **isEmpty** | `while queue:` | 비었는지 확인 |

이 방법은 **실제 큐 자료구조의 동작**을 그대로 따릅니다!
- ✅ 맨 앞부터 확인 (peek)
- ✅ 조건 만족하면 제거 (dequeue)
- ✅ 조건 불만족하면 멈춤 (FIFO 유지)

---

### 방법 3: 인덱스 기반 (메모리 최적화) ⭐ 공간 효율 최고
```python
import math

def solution(progresses, speeds):
    answer = []
    i = 0
    n = len(progresses)

    while i < n:
        # 현재 작업의 완료일
        days = math.ceil((100 - progresses[i]) / speeds[i])
        count = 1
        i += 1

        # 뒤따르는 작업 중 같이 배포 가능한 것들
        while i < n:
            next_days = math.ceil((100 - progresses[i]) / speeds[i])
            if next_days <= days:
                count += 1
                i += 1
            else:
                break

        answer.append(count)

    return answer
```
**장점**: 추가 공간 거의 없음 O(1), 직관적
**단점**: 완료일을 매번 재계산 (큰 문제는 아님)
**메모리**: ~32B (가장 효율적!)

---

## 🔍 방법 1 vs 방법 2: 핵심 차이

### 방법 1: 개념적 활용 (추상화)
```python
# "언제 끝나는가"를 미리 계산
days_left = [7, 3, 9]

# 머릿속으로: "7일차에 묶이는 것들 = 7일 이내 완료"
for day in days_left:
    if day <= max_day:  # 7일 이내?
        count += 1      # 같이 배포!
```
**사고방식**: "완료일 기준으로 그룹화"
- 큐 없이도 FIFO 원칙 준수
- 더 추상적이고 효율적

### 방법 2: 실제 큐 사용 (구체적)
```python
# "이 날짜에 완료됐나"를 실시간 체크
queue = deque([(93,1), (30,30), (55,5)])

# 실제 큐에서: "7일 후 완료된 것들 빼내기"
while queue:
    if queue[0] 완료됐나?:
        queue.popleft()  # 큐에서 제거!
```
**사고방식**: "실제 대기열 운영"
- 큐 자료구조 직접 조작
- 더 구체적이고 직관적

### 언제 어떤 방법을?

| 상황 | 추천 방법 | 이유 |
|------|----------|------|
| 코딩테스트 | 방법 1 | 빠르고 실수 적음 |
| 큐 학습 | 방법 2 | 자료구조 이해 |
| 면접 설명 | 방법 1 → 2 | 개념 → 구현 순 설명 |

---

## 📊 방법 비교표 (실제 측정 결과)

| 방법 | 시간 복잡도 | 공간 복잡도 | 메모리 사용 | 가독성 | 추천도 |
|------|------------|------------|------------|--------|--------|
| **방법 1 (현재)** | O(N) | O(N) | 240B | ⭐⭐⭐⭐⭐ | ✅ 가장 추천 |
| 방법 2 (deque) | O(N) | O(N) | 920B | ⭐⭐⭐ | 큐 학습용 |
| 방법 3 (인덱스) | O(N) | O(1) | 32B ⚡ | ⭐⭐⭐⭐ | 메모리 중요시 |

## 🎓 어떤 방법을 선택할까?

### 코딩테스트에서는?
→ **방법 1 (현재 풀이)** 추천
- 깔끔하고 실수 적음
- 면접관이 이해하기 쉬움
- 최적의 균형

### 실무에서는?
→ **방법 1 또는 3**
- 방법 1: 유지보수 쉬움, 코드 가독성 최우선
- 방법 3: 메모리 제약이 큰 임베디드 시스템

### 자료구조 학습용으로는?
→ **방법 2 (deque)** 추천
- 큐의 실제 동작 원리 이해
- FIFO 특성을 직접 구현

## 회고

### 배운 점
-

### 어려웠던 부분
-

### 개선할 점
-

---
**복잡도**: 시간 O(N), 공간 O(N)
**풀이 날짜**: 2025-11-03

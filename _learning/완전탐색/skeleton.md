// [Complete Search (Backtracking) Pattern]
// 모든 가능한 경우의 수를 체계적으로 탐색하여 정답을 찾습니다.

---
## Why & What (이 패턴은 왜/무엇)
- **목적**: 해가 될 수 있는 모든 후보를 검사하여 조건을 만족하는 해를 찾거나 그 수를 셉니다.
- **본질**: "가능한 모든 선택지를 시도하고, 막히면 되돌아간다 (Backtracking)"
- **장점**: 논리적으로 답을 놓칠 수 없음. 구현이 직관적임.
- **단점**: 시간 복잡도가 지수적(Exponential)이므로 N이 작을 때만 사용 가능.

## When to Use (이럴 때 사용)
- `N이 작음`: N <= 20 (부분집합 O(2^N)), N <= 10 (순열 O(N!))
- `모든 경우의 수`: "가능한 모든 방법의 수를 구하시오", "사전 순으로 출력하시오"
- `난해한 최적화`: 그리디나 DP로 해결이 불가능해 보일 때
- `재귀적 구조`: 선택 후 다음 상태로 넘어가는 구조가 반복될 때

### 추천 문제 (Base)
- [프로그래머스 Lv.2] 모음사전 (사전 순 생성)
- [프로그래머스 Lv.2] 카펫 (Brute Force)
- [프로그래머스 Lv.2] 전력망을 둘로 나누기 (Graph Search)
- [프로그래머스 Lv.3] N-Queen (Backtracking 대표 문제)
---

## 핵심 구조 (Backtracking)

```python
def solve(n, constraints):
    # 1. [Global State] ─────────────────────────────────
    #    역할: 탐색 과정에서 공유해야 할 데이터 (결과 저장소, 방문 체크 등)
    #    ADAPT: 전역 변수 대신 함수 인자로 넘겨도 됨 (상태가 가벼울 때)
    result = []
    visited = [False] * n 
    
    def backtrack(current_state):
        # 2. [Base Case] ─────────────────────────────────
        #    역할: 재귀 탈출 조건 (목표 도달)
        #    WHY: 종료 조건이 없으면 무한 재귀 → 스택 오버플로우
        #    PITFALL: 답을 찾았을 때 return을 잊지 말 것
        if is_complete(current_state):
            # ADAPT: shallow copy 주의 (current_state[:] 또는 list(current_state))
            result.append(current_state[:]) 
            return

        # 3. [Iterate Candidates] ─────────────────────────────────
        #    역할: 현재 상태에서 선택 가능한 다음 후보들을 순회
        #    COMPLEXITY: 여기서의 분기 수(Branching Factor)가 전체 복잡도 결정
        for candidate in get_candidates(n):
            
            # 4. [Pruning] (가지치기) ─────────────────────────────────
            #    역할: 유망하지 않은 경로는 더 이상 탐색하지 않음 (Backtracking의 핵심)
            #    WHY: 이 조건이 없으면 단순 DFS가 되어 시간 초과 가능성 급증
            if not is_valid(candidate, visited):
                continue

            # 5. [Transition] (Do) ─────────────────────────────────
            #    역할: 상태 변경 (선택)
            #    WHY: 재귀 호출 전 상태를 업데이트
            visited[candidate] = True
            current_state.append(candidate)
            
            # 6. [Recursion] ─────────────────────────────────
            #    역할: 다음 단계로 진입
            backtrack(current_state)
            
            # 7. [Revert] (Undo) ─────────────────────────────────
            #    역할: 상태 복구 (취소)
            #    WHY: 이전 단계로 돌아가서 다른 후보를 선택하기 위함
            #    PITFALL: Do와 Undo는 정확히 대칭이어야 함
            current_state.pop()
            visited[candidate] = False

    # 초기 호출
    backtrack([])
    return result
```

---
## Customization Points
- `is_complete(state)`: 원하는 깊이나 조건에 도달했는지 확인 (예: `len(state) == M`)
- `is_valid(candidate, visited)`: 중복 사용 불가, 인접 제약 등 문제별 제약 조건
- `visited`: 순열/조합 여부에 따라 필요/불필요 결정

---
## Variations (응용 유형)

### 변형 A: 순열 (Permutations)
**상황**: 서로 다른 N개에서 R개를 뽑아 **일렬로 나열**하는 경우 (순서 O)
**핵심 변화**: `visited` 배열로 중복 선택 방지
**추천 문제**
- [프로그래머스 Lv.2] 피로도 (순열)
- [프로그래머스 Lv.2] 단체사진 찍기 (조건이 있는 순열)
- [프로그래머스 Lv.2] 양궁대회 (중복조합/순열)

```python
# Itertools 사용 권장 (간단한 경우)
import itertools
def permutation_lib(arr, r):
    return list(itertools.permutations(arr, r))

# 직접 구현 (제약 조건이 복잡한 경우)
def permutations_manual(arr, r):
    result = []
    visited = [False] * len(arr)
    
    def dfs(curr):
        if len(curr) == r:
            result.append(curr[:])
            return
        
        for i in range(len(arr)):
            if not visited[i]:
                visited[i] = True
                curr.append(arr[i])
                dfs(curr)
                curr.pop()
                visited[i] = False
    
    dfs([])
    return result
```

### 변형 B: 조합 (Combinations)
**상황**: 서로 다른 N개에서 R개를 뽑는 경우 (순서 X)
**핵심 변화**: `start_index` 인자를 두어, 현재 선택한 원소의 **다음 원소부터** 탐색 (중복 방지, 순서 무시)
**추천 문제**
- [프로그래머스 Lv.1] 소수 만들기 (3개 뽑기)
- [프로그래머스 Lv.2] 메뉴 리뉴얼 (조합 + 카운팅)
- [프로그래머스 Lv.2] 소수 찾기 (순열 + 조합)

```python
# Itertools 사용 권장
import itertools
def combination_lib(arr, r):
    return list(itertools.combinations(arr, r))

# 직접 구현
def combinations_manual(arr, r):
    result = []
    
    # start: 탐색 시작 인덱스 (이전 선택보다 뒤쪽만 봄)
    def dfs(start, curr):
        if len(curr) == r:
            result.append(curr[:])
            return
        
        for i in range(start, len(arr)):
            # 조합은 visited 필요 없음 (앞으로만 가므로)
            curr.append(arr[i])
            dfs(i + 1, curr) # i + 1부터 탐색
            curr.pop()
            
    dfs(0, [])
    return result
```

### 변형 C: 부분집합 (Subsets)
**상황**: 원소들의 모든 가능한 그룹을 만들 때 (공집합 포함)
**핵심 변화**: 각 원소를 `선택한다 / 안 한다`의 이진 트리 구조로 접근
**추천 문제**
- [프로그래머스 Lv.2] 타겟 넘버 (선택의 기로)
- [프로그래머스 Lv.2] 후보키 (부분집합 + 유일성/최소성 검증)

```python
def subsets(arr):
    result = []
    n = len(arr)
    
    # 방식 1: 비트마스킹 (가장 빠르고 간결)
    for i in range(1 << n):
        subset = []
        for j in range(n):
            if i & (1 << j):
                subset.append(arr[j])
        result.append(subset)
    
    # 방식 2: 재귀 (백트래킹)
    def dfs(idx, curr):
        if idx == n:
            result.append(curr[:])
            return
        
        # idx번째 원소를 선택하는 경우
        curr.append(arr[idx])
        dfs(idx + 1, curr)
        
        # idx번째 원소를 선택하지 않는 경우
        curr.pop()
        dfs(idx + 1, curr)
        
    dfs(0, [])
    return result
```

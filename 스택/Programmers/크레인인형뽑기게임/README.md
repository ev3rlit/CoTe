# [문제명]
- 링크 : 

#태그1 #태그2 #태그3

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

## 개선할 점

### 1. 불필요한 더미 리스트 사용 (solution.py:12)
```python
dolls = [[],]  # 인덱스 0에 더미 리스트
```
- `moves`가 1-based 인덱싱이라고 가정하고 `dolls[0]`을 더미로 사용했습니다.
- 이는 메모리 낭비이며, 코드 읽는 사람에게 혼란을 줄 수 있습니다.
- **개선안**: 0-based로 변경하거나 명확한 주석 추가
  ```python
  # 방법 1: 명확한 주석
  dolls = [[],]  # moves가 1-based이므로 인덱스 0은 더미

  # 방법 2: 0-based로 변경 (더 권장)
  dolls = []
  # ...
  # 사용 시: dolls[m - 1]
  ```

### 2. 주석 처리된 코드 제거 필요 (solution.py:28-32)
```python
# # 바스켓이 비어있ㅇ면 넣기
# if not basket:
#     basket.append(dolls[m][-1])
#     dolls[m].pop()
#     continue
```
- 이 로직은 이미 `else` 블록(42줄)에서 처리되므로 불필요합니다.
- 주석 처리된 코드는 혼란을 야기하므로 삭제가 필요합니다.

### 3. 오타 수정 (solution.py:28)
```python
# 바스켓이 비어있ㅇ면 넣기  # -> "비어있으면"
```

### 4. 변수명 개선
```python
boomed = 0  # -> answer 또는 removed_count
```
- 프로그래머스 문제는 일반적으로 `answer`를 반환 변수명으로 사용합니다.
- `boomed`는 의미는 명확하지만 관례적이지 않습니다.

### 5. 추가 테스트 케이스 부족
- 현재 테스트 케이스가 1개뿐입니다.
- 엣지 케이스 테스트가 부족합니다:
  - 모든 moves가 빈 열을 선택하는 경우
  - 연속으로 여러 쌍이 터지는 경우
  - 인형이 전혀 터지지 않는 경우

## 잘한 점

### 1. 스택을 활용한 정확한 문제 이해
- 보드의 각 열을 스택으로 변환하는 아이디어가 매우 적절합니다.
- 인형을 아래에서 위 순서로 스택에 저장하여 `pop()`으로 쉽게 접근할 수 있도록 했습니다.

### 2. 엣지 케이스 처리
```python
# solution.py:25 - 빈 열 체크
if not dolls[m]:
    continue

# solution.py:36 - 빈 바구니 체크
if basket and dolls[m][-1] == basket[-1]:
```
- 빈 열과 빈 바구니에 대한 예외 처리를 정확히 했습니다.
- `basket and` 조건으로 IndexError를 방지했습니다.

### 3. 효율적인 시간복잡도
- **시간복잡도**: O(N × M + K)
  - N × M: 보드를 열별로 변환
  - K: moves 순회
  - 각 move당 O(1) 연산
- 스택의 `pop()`과 `append()`를 사용하여 최적의 성능을 달성했습니다.

### 4. 명확한 로직 흐름
```python
if basket and dolls[m][-1] == basket[-1]:
    # 터트림
    boomed += 2
    basket.pop()
    dolls[m].pop()
else:
    # 바구니에 추가
    basket.append(dolls[m].pop())
```
- if-else 구조로 두 가지 경우를 명확히 구분했습니다.

## 다른 응용 방안

### 1. 리팩토링된 버전
```python
def solution(board, moves):
    answer = 0
    rows, cols = len(board), len(board[0])

    # 각 열을 스택으로 변환 (인덱스 0은 더미, moves가 1-based)
    stacks = [[]]
    for col in range(cols):
        stack = []
        for row in range(rows - 1, -1, -1):
            if board[row][col] != 0:
                stack.append(board[row][col])
        stacks.append(stack)

    basket = []
    for move in moves:
        if not stacks[move]:
            continue

        doll = stacks[move].pop()

        if basket and basket[-1] == doll:
            basket.pop()
            answer += 2
        else:
            basket.append(doll)

    return answer
```

### 2. 2D 보드를 1D 스택 배열로 변환하는 패턴
- 이 문제의 핵심 패턴은 **2차원 격자를 1차원 스택 배열로 변환**하는 것입니다.
- 비슷한 유형:
  - 테트리스 게임 구현
  - 블록 쌓기 시뮬레이션
  - 열 단위 데이터 처리 문제

### 3. 연속 중복 제거 패턴 응용
```python
# 바구니 로직은 "연속된 같은 값 제거" 패턴
if basket and basket[-1] == doll:
    basket.pop()
```
- 이 패턴은 다른 문제에도 응용 가능:
  - 괄호 짝짓기 문제
  - 문자열 중복 제거
  - 연속된 같은 원소 제거

## 종합 평가

이 풀이는 **스택 자료구조를 정확히 이해하고 활용**한 좋은 예시입니다. 2차원 보드를 1차원 스택 배열로 변환하는 아이디어와 바구니에서 연속 중복을 제거하는 로직이 명확하게 구현되었습니다.

하지만 **코드 품질 측면에서 개선이 필요**합니다. 주석 처리된 불필요한 코드가 남아있고, 1-based 인덱싱을 위한 더미 리스트 사용이 명확한 주석 없이 사용되어 가독성을 떨어뜨립니다. 변수명도 `boomed`보다는 관례적인 `answer`를 사용하는 것이 좋습니다.

**알고리즘적으로는 최적의 시간복잡도 O(N×M + K)**를 달성했으나, 실무 코드 리뷰 관점에서는 **코드 정리와 명확한 의도 전달**이 부족합니다. 특히 테스트 케이스가 1개만 있어 엣지 케이스에 대한 검증이 충분하지 않습니다. 빈 열만 선택하는 경우, 연속으로 여러 쌍이 터지는 경우 등 다양한 시나리오를 테스트해야 코드의 견고성을 보장할 수 있습니다.

코딩 테스트에서는 정답을 맞추는 것도 중요하지만, **유지보수 가능한 깔끔한 코드**를 작성하는 습관이 더 중요합니다. 다음 문제부터는 불필요한 코드를 제거하고, 명확한 변수명을 사용하며, 충분한 테스트 케이스를 작성하는 연습을 해보세요.

---
**복잡도**: O(N × M + K) (N=행, M=열, K=moves 길이)
**풀이 날짜**: 2025-11-02

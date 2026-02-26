# 길 찾기 게임
- 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/42892

```
#트리 #이진트리 #재귀 #정렬 #전위순회 #후위순회
```

---

## 문제 설명

2차원 좌표 평면에 노드들이 흩어져 있습니다. 각 노드의 (x, y) 좌표가 주어질 때, 다음 규칙에 따라 이진 트리를 구성하고 전위 순회와 후위 순회 결과를 반환하는 문제입니다.

**트리 구성 규칙:**
- y 좌표가 높을수록 상위 레벨 (루트에 가까움)
- 같은 레벨에서 x 좌표가 작으면 왼쪽, 크면 오른쪽
- 부모 노드의 x 좌표를 기준으로 왼쪽/오른쪽 서브트리 결정

## 문제 입출력

**입력:**
- `nodeinfo`: 각 노드의 [x, y] 좌표 배열 (1-based 인덱스)

**출력:**
- `[전위 순회 결과, 후위 순회 결과]` 2차원 배열

**예시:**
```
입력: [[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]
출력: [[7,4,6,9,1,8,5,2,3],[9,6,5,8,1,4,3,2,7]]
```

---

## 풀이 과정

### 핵심 아이디어
- **정렬 기반 트리 구성**: y 좌표 내림차순 → x 좌표 오름차순으로 정렬하면 루트부터 순서대로 삽입 가능
- **BST 스타일 삽입**: x 좌표를 기준으로 부모의 왼쪽/오른쪽 결정
- **재귀 순회**: 전위/후위 순회를 재귀로 구현

### 접근 방법
1. **좌표에 노드 번호 부여**: `(x, y, 노드번호)` 형태로 변환
2. **정렬**: y 내림차순 (상위 레벨부터), x 오름차순 (같은 레벨 내)
3. **이진 트리 구성**:
   - 첫 노드를 루트로 설정
   - 이후 노드들은 x 좌표를 기준으로 왼쪽/오른쪽 자식으로 삽입
4. **순회**: 전위 순회(Root → Left → Right), 후위 순회(Left → Right → Root)

### 코드

```python
from dataclasses import dataclass
import sys

sys.setrecursionlimit(10**6)

@dataclass
class Node():
    number : int = 0
    x : int = 0
    y : int = 0
    left = None
    right = None

class BinaryTree():
    def __init__(self) -> None:
        self.root = None

    def insert(self, number, x, y):
        node = Node(number, x, y)

        if self.root is None:
            self.root = node
            return

        # x 좌표를 기준으로 왼쪽/오른쪽 결정
        parent = self.root
        while True:
            if node.x < parent.x:
                if parent.left is not None:
                    parent = parent.left
                    continue
                parent.left = node
                break
            else:
                if parent.right is not None:
                    parent = parent.right
                    continue
                parent.right = node
                break

    def pre_order(self):
        result = []

        def travel(node):
            if node is None:
                return
            result.append(node.number)
            travel(node.left)
            travel(node.right)

        travel(self.root)
        return result

    def post_order(self):
        result = []

        def travel(node):
            if node is None:
                return
            travel(node.left)
            travel(node.right)
            result.append(node.number)

        travel(self.root)
        return result

def solution(nodeinfo):
    # (x, y, 노드번호) 형태로 변환
    nodes = [(x, y, i+1) for i, (x, y) in enumerate(nodeinfo)]

    # y 내림차순, x 오름차순 정렬
    nodes.sort(key=lambda node: (-node[1], node[0]))

    # 이진 트리 구성
    tree = BinaryTree()
    for (x, y, number) in nodes:
        tree.insert(number, x, y)

    return [tree.pre_order(), tree.post_order()]
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

#### 1. **프로그래머스 호환성 문제**

##### dataclass 사용
```python
from dataclasses import dataclass

@dataclass
class Node():
    number : int = 0
    x : int = 0
    y : int = 0
    left = None
    right = None
```

**문제**: 프로그래머스 채점 환경에서 `dataclasses`를 지원하지 않을 수 있습니다.

**개선안**:
```python
class Node():
    def __init__(self, number=0, x=0, y=0):
        self.number = number
        self.x = x
        self.y = y
        self.left = None
        self.right = None
```

일반 클래스로 변경하면 모든 환경에서 동작 보장됩니다.

##### sys.setrecursionlimit
```python
import sys
sys.setrecursionlimit(10**6)
```

**현재 상태**: 주석 없이 사용
**개선**: 왜 필요한지 주석 추가

```python
import sys
# 재귀 깊이 제한 확장 (최대 10,000개 노드 대비)
sys.setrecursionlimit(10**6)
```

#### 2. **타입 힌트 관련 Pylance 경고**

현재 `left = None`, `right = None`으로 선언하면 Pylance가 "항상 None"이라고 추론하여 경고를 표시합니다.

**해결 방법 (선택사항)**:
```python
# 방법 1: 타입 주석 (프로그래머스 미지원 가능성)
from typing import Optional
left: Optional['Node'] = None

# 방법 2: 일반 클래스 사용 (권장)
class Node():
    def __init__(self, number=0, x=0, y=0):
        self.number = number
        self.x = x
        self.y = y
        self.left = None   # __init__에서는 Pylance 경고 없음
        self.right = None
```

**참고**: Pylance 경고는 정적 타입 체크일 뿐, **실제 실행에는 전혀 문제 없습니다**. 무시해도 됩니다.

#### 3. **변수명 일관성**

```python
def travel(node):  # 순회 함수
```

`travel`보다 `traverse`가 더 일반적인 용어입니다. 또는 한글 주석으로 명확히 표시하는 것도 좋습니다.

```python
def traverse(node):  # 재귀 순회
    # 또는
def _traverse(node):  # private 메서드 표시 (언더스코어)
```

#### 4. **insert 메서드 개선 가능성**

현재 반복문으로 삽입 위치를 찾는데, 재귀로 구현하면 더 간결합니다.

**현재 (반복문)**:
```python
parent = self.root
while True:
    if node.x < parent.x:
        if parent.left is not None:
            parent = parent.left
            continue
        parent.left = node
        break
    # ...
```

**대안 (재귀)**:
```python
def insert(self, number, x, y):
    node = Node(number, x, y)
    if self.root is None:
        self.root = node
    else:
        self._insert_recursive(self.root, node)

def _insert_recursive(self, parent, node):
    if node.x < parent.x:
        if parent.left is None:
            parent.left = node
        else:
            self._insert_recursive(parent.left, node)
    else:
        if parent.right is None:
            parent.right = node
        else:
            self._insert_recursive(parent.right, node)
```

**장점**: 트리 순회 로직과 일관성, 코드 간결함
**단점**: 스택 깊이 증가 (이미 setrecursionlimit 설정했으므로 문제없음)

---

### 잘한 점

#### 1. **정렬 전략이 완벽함**
```python
nodes.sort(key=lambda node: (-node[1], node[0]))
```

y 내림차순, x 오름차순 정렬로 **루트부터 순서대로 삽입**할 수 있게 만든 것이 핵심입니다. 이 한 줄이 문제의 70%를 해결합니다.

#### 2. **이진 트리 구조 설계**
- Node 클래스: 필요한 정보만 간결하게 보유
- BinaryTree 클래스: 삽입과 순회 책임 분리
- 객체 지향적 설계가 깔끔합니다.

#### 3. **재귀 순회 구현이 명확함**
```python
def travel(node):
    if node is None:
        return
    result.append(node.number)  # 전위: Root 먼저
    travel(node.left)
    travel(node.right)
```

전위/후위 순회의 차이를 `result.append()` 위치로만 표현한 것이 매우 직관적입니다.

#### 4. **테스트 케이스 작성**
- 기본 케이스, 단일 노드, 편향 트리까지 테스트
- 엣지 케이스를 고려한 점이 훌륭합니다.

#### 5. **enumerate를 활용한 노드 번호 부여**
```python
nodes = [(x, y, i+1) for i, (x, y) in enumerate(nodeinfo)]
```

인덱스를 1-based로 변환하는 부분이 깔끔합니다.

---

### 다른 응용 방안

#### 1. **세그먼트 트리 (Segment Tree)**
- 2D 좌표를 구간으로 나눠 관리
- 범위 쿼리 최적화 (O(log N))

#### 2. **kd-Tree (k-dimensional Tree)**
- 다차원 공간에서 최근접 이웃 탐색
- 2D/3D 게임에서 충돌 감지

#### 3. **Quad Tree**
- 2D 공간을 4개 사분면으로 분할
- 이미지 압축, 지리 정보 시스템

#### 4. **표현식 트리 (Expression Tree)**
- 수식을 트리로 표현
- 전위: 전위 표기법, 중위: 중위 표기법, 후위: 후위 표기법

#### 5. **파일 시스템 탐색**
- 디렉토리 구조 순회
- 전위: 디렉토리 먼저, 후위: 파일 먼저 처리

---

### 다른 추천 문제

#### 이진 트리 순회
- **[프로그래머스] 양과 늑대** (Level 3) - 트리 + 상태 공간 탐색
- **[백준] 1991 트리 순회** - 전위/중위/후위 순회 기본
- **[백준] 5639 이진 검색 트리** - 전위 → 후위 변환

#### 트리 구성 문제
- **[백준] 2250 트리의 높이와 너비** - 좌표 기반 트리 배치
- **[백준] 9934 완전 이진 트리** - 중위 순회로 트리 복원
- **[LeetCode] 105. Construct Binary Tree from Preorder and Inorder** - 순회 결과로 트리 구성

#### 좌표/정렬 기반 문제
- **[백준] 2170 선 긋기** - 좌표 정렬 + 구간 병합
- **[백준] 1202 보석 도둑** - 정렬 + 우선순위 큐
- **[프로그래머스] 줄 서는 방법** (Level 2) - 순열 + 정렬

---

### 종합 평가

이 풀이는 **정렬을 활용한 트리 구성**이라는 핵심 아이디어를 정확히 구현했습니다. 특히 `(-y, x)` 정렬 전략으로 복잡한 트리 구성 문제를 단순화한 점이 뛰어납니다. 이진 트리 클래스 설계와 재귀 순회 구현 모두 깔끔합니다.

다만 **프로그래머스 제출 시 주의사항**이 있습니다:
1. `dataclass`는 지원하지 않을 수 있음 → 일반 클래스로 변경 권장
2. `sys.setrecursionlimit`는 필수이지만 설명 주석 추가 권장

**코드 스타일 측면**에서 몇 가지 개선 제안:
- 변수명: `travel` → `traverse` (더 일반적인 용어)
- insert 메서드: 반복문보다 재귀가 트리 문제에 더 자연스러움
- Pylance 경고: 실행 무관하므로 무시 가능, 신경 쓰인다면 일반 클래스 사용

**알고리즘 이해도**는 매우 높습니다. 정렬 전략을 통해 문제를 단순화한 것은 "복잡한 문제를 간단하게 만드는 능력"을 보여줍니다. 이는 코딩 테스트에서 가장 중요한 능력 중 하나입니다.

마지막으로, **테스트 케이스를 직접 작성**한 점이 인상적입니다. 특히 편향 트리(왼쪽으로 치우친 트리)까지 테스트한 것은 엣지 케이스를 고려하는 좋은 습관입니다. 실무에서도 이런 습관은 버그를 미리 방지하는 데 큰 도움이 됩니다.

---

### 추가 학습: 트리 순회 방식

#### 순회 방식 비교

| 순회 방식 | 순서 | 용도 |
|----------|------|------|
| **전위 (Pre-order)** | Root → Left → Right | 트리 복사, 표현식 전위 표기 |
| **중위 (In-order)** | Left → Root → Right | BST 정렬 순서 출력 |
| **후위 (Post-order)** | Left → Right → Root | 트리 삭제, 표현식 계산 |
| **레벨 (Level-order)** | 레벨별 왼쪽→오른쪽 | BFS, 최단 경로 |

#### 이 문제에서의 활용

```
       7(8,6)
      /      \
   4(3,5)    6(11,5)
   /         /     \
9(1,3)   1(6,1)   8(13,3)
        /   \
     5(2,2) 2(7,2)
       \
      3(5,3)
```

**전위 순회** (Root → Left → Right):
```
7 → 4 → 9 → 6 → 1 → 5 → 3 → 2 → 8
```
- 루트부터 시작하여 깊이 우선 탐색
- 트리 구조를 그대로 복원 가능

**후위 순회** (Left → Right → Root):
```
9 → 4 → 3 → 5 → 2 → 1 → 8 → 6 → 7
```
- 자식부터 처리 후 부모 처리
- 트리 삭제, 폴더 정리 등에 사용

#### 재귀 vs 반복

**재귀 (현재 코드)**:
```python
def traverse(node):
    if node is None:
        return
    result.append(node.number)  # 전위
    traverse(node.left)
    traverse(node.right)
```

**반복 (스택 사용)**:
```python
def pre_order_iterative(self):
    if not self.root:
        return []

    result = []
    stack = [self.root]

    while stack:
        node = stack.pop()
        result.append(node.number)

        # 오른쪽 먼저 push (나중에 처리)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

    return result
```

**비교**:
- 재귀: 코드 간결, 직관적, 스택 오버플로 가능
- 반복: 메모리 효율적, 제어 가능, 코드 복잡

이 문제는 노드 수가 최대 10,000개이므로 재귀가 적합합니다.

---

**복잡도**:
- 시간: O(N log N) - 정렬 O(N log N) + 트리 구성 O(N log N) + 순회 O(N)
- 공간: O(N) - 트리 노드 저장

**풀이 날짜**: 2025-01

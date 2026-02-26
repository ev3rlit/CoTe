# 신고 결과 받기
- 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/92334
- 출제: 2022 KAKAO BLIND RECRUITMENT

```
#해시 #구현 #문자열 #집합
```

## 풀이 과정

### 핵심 아이디어
- `defaultdict(set)`을 사용하여 중복 신고를 자동으로 제거하고, 신고자-피신고자 관계를 양방향으로 관리

### 접근 방법
1. 신고 내역을 파싱하여 "누가 누구를 신고했는지"와 "누가 누구에게 신고받았는지"를 양방향으로 기록
2. k번 이상 신고받은 유저를 정지 대상으로 추출
3. 각 유저가 신고한 대상 중 정지된 유저 수를 카운팅하여 결과 반환

## 회고

### 배운 점
- 튜플 unpacking을 활용하여 배열 데이터에 각 변수로 할당가능함.

### 어려웠던 부분
-

### 개선할 점
- 코드가 길어서 가독성으로는 아쉬웠지만 효율성 측면에서는 좋은 성능을 보였다.
- 변수가 3개 할당되어있는데, 저장하지 않고 메모리 효율적으로 관리할 방법을 고민해보자.
- 각 유저 닉네임에 대한 int 고유 아이디를 할당하면 메모리를 더 효율적으로 관리할 수 있다.

---

# 평가

## 개선할 점

### 1. 변수명 개선 필요
```python
for id in id_list:  # ❌ 'id'는 Python 내장 함수명
```
Python의 내장 함수 `id()`와 충돌하는 변수명을 사용했습니다. `user_id` 또는 `user` 등으로 변경하는 것이 권장됩니다.

### 2. 집합 연산으로 더 간결한 구현 가능
현재 코드:
```python
for id in id_list:
    count = 0
    for reportee in reporters[id]:
        if reportee in blocks:
            count += 1
    result.append(count)
```

개선안:
```python
for user_id in id_list:
    count = len(reporters[user_id] & blocks)  # 집합 교집합 연산
    result.append(count)
```
집합의 `&` 연산자를 사용하면 중첩 반복문 없이 한 줄로 처리 가능하며, 코드의 의도가 더 명확해집니다.

### 3. 불필요한 주석 정리
```python
# 특정 유저는 다른 유저를 신고할 수 있고, 신고를 여러번 해도 1번으로 기록됨
# 특정 유저가 K번 이상 다른 유저들로 부터 신고가 누적될경우 정지 및  신고한 유저들에게 사실을 알림
...
#
# 총 신고자 report 길이에  조회를 하는 M
```
문제 설명을 그대로 옮긴 주석들이 많아 코드가 길어졌습니다. 핵심 로직에 대한 간결한 주석만 남기는 것이 좋습니다.

## 잘한 점

### 1. 자료구조 선택이 탁월함 ⭐
`defaultdict(set)` 조합은 이 문제의 핵심인 "중복 신고 제거"를 자동으로 처리하는 최적의 선택입니다. 별도의 중복 체크 로직 없이 `set`의 특성만으로 문제를 해결한 점이 매우 효율적입니다.

### 2. 명확한 두 단계 접근
```python
# 1단계: 정지 대상자 추출
blocks = set()
for reportee, users in reportees.items():
    if len(users) >= k:
        blocks.add(reportee)

# 2단계: 각 유저별 카운팅
```
로직을 명확히 분리하여 가독성과 디버깅 용이성을 높였습니다.

### 3. 양방향 관계 관리
`reporters`(신고자→피신고자)와 `reportees`(피신고자→신고자) 두 방향을 모두 관리하여, 각 단계에서 필요한 정보를 효율적으로 조회할 수 있습니다.

### 4. tuple unpacking 활용
```python
reporter, reportee = tuple(event.split(" "))
```
문자열 파싱 결과를 깔끔하게 변수에 할당했습니다. (참고: `tuple()` 호출은 불필요 - `split()`은 이미 리스트를 반환하므로 언패킹 가능)

## 다른 응용 방안

### 1. 온라인 커뮤니티 모더레이션 시스템
- 유튜브, 인스타그램 등의 댓글/게시글 신고 시스템
- 특정 임계값 이상 신고 시 자동 숨김 처리
- 신고자에게 처리 결과 알림 전송

### 2. 스팸 메일 필터링
- 여러 사용자가 특정 발신자를 스팸으로 신고
- k명 이상 신고 시 자동 차단 리스트 등록
- 신고한 사용자들에게 차단 완료 알림

### 3. 게임 내 악성 유저 관리
- 게임에서 욕설, 핵 사용 등 부정행위 신고
- 누적 신고 수에 따른 계정 정지
- 신고자에게 처리 결과 보상 지급

### 4. 네트워크 보안 - IP 차단 시스템
- 여러 서버에서 특정 IP의 비정상 접근 감지 (신고)
- 임계값 초과 시 방화벽 차단 규칙 자동 등록
- 관리자에게 차단 내역 알림

## 종합 평가

이 풀이는 **자료구조 선택의 정석**을 보여주는 좋은 사례입니다. `defaultdict(set)`으로 중복 신고를 자연스럽게 처리하고, 양방향 관계를 관리하여 각 단계에서 필요한 정보를 O(1) 시간에 조회할 수 있도록 설계한 점이 훌륭합니다.

그러나 **코딩 테스트 관점에서는 간결함이 중요**합니다. 현재 코드는 주석이 과도하게 많고(50줄 중 14줄이 주석), 마지막 카운팅 로직에서 집합 연산을 활용하지 않아 불필요한 중첩 반복문이 존재합니다. 카카오 코딩 테스트는 제한 시간이 짧기 때문에, 핵심 로직을 빠르게 구현하고 검증하는 것이 중요합니다.

또한 `id`와 같은 Python 내장 함수명을 변수명으로 사용한 것은 실무에서도 피해야 할 안티패턴입니다. IDE의 경고를 무시하지 말고, 명확하고 충돌 없는 변수명(`user_id`, `user_name` 등)을 사용하는 습관을 들이는 것이 좋습니다.

**성능 분석**: 시간 복잡도는 O(M + N×R_avg)로, M은 신고 수, N은 유저 수, R_avg는 평균 신고 대상 수입니다. 최악의 경우 O(M + N²)이지만, 문제의 제약 조건(id_list ≤ 1,000, report ≤ 200,000)을 고려하면 충분히 효율적입니다. 집합 교집합 연산으로 개선하면 내부 반복을 최적화할 수 있습니다.

**개선 포인트**: 집합 연산 활용, 불필요한 주석 제거, 변수명 개선만으로도 코드 품질이 크게 향상될 것입니다. 특히 `len(reporters[user_id] & blocks)` 패턴은 다른 문제에서도 자주 활용되니 꼭 기억하시기 바랍니다.

---
**복잡도**:
- 시간: O(M + N×R_avg) (M: 신고 수, N: 유저 수, R_avg: 평균 신고 대상 수)
- 공간: O(M) (최악의 경우 모든 신고가 유니크)

**풀이 날짜**: 2025-11-12

---

# 추가 학습

## 1. Python 집합(set) 연산의 활용

### 기본 집합 연산
```python
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

# 교집합 (intersection)
A & B           # {3, 4}
A.intersection(B)

# 합집합 (union)
A | B           # {1, 2, 3, 4, 5, 6}
A.union(B)

# 차집합 (difference)
A - B           # {1, 2}
A.difference(B)

# 대칭 차집합 (symmetric difference)
A ^ B           # {1, 2, 5, 6}
A.symmetric_difference(B)
```

### 코딩 테스트에서 자주 쓰이는 패턴
```python
# 패턴 1: 두 그룹의 공통 요소 개수 세기
common_count = len(set_a & set_b)

# 패턴 2: 리스트에서 중복 제거
unique_items = list(set(items))

# 패턴 3: 여러 조건을 만족하는 요소 찾기
valid_items = set(candidates) & set(allowed) - set(blocked)

# 패턴 4: 빠른 멤버십 테스트 (O(1))
if item in my_set:  # 리스트보다 훨씬 빠름
    pass
```

## 2. defaultdict vs dict vs Counter 선택 가이드

### defaultdict(set) - 그룹핑에 최적
```python
from collections import defaultdict

# 사용 시기: 키별로 여러 값을 모을 때
graph = defaultdict(set)
graph['A'].add('B')  # KeyError 걱정 없음
```

### defaultdict(list) - 순서가 중요할 때
```python
groups = defaultdict(list)
groups['team1'].append('member1')
groups['team1'].append('member2')
```

### Counter - 빈도 계산
```python
from collections import Counter

votes = ['A', 'B', 'A', 'C', 'A', 'B']
count = Counter(votes)  # Counter({'A': 3, 'B': 2, 'C': 1})
count.most_common(1)    # [('A', 3)]
```

### 일반 dict - 명시적 제어가 필요할 때
```python
# KeyError를 명시적으로 처리하고 싶을 때
user_scores = {}
if user_id not in user_scores:
    user_scores[user_id] = 0
```

## 3. 양방향 관계 관리 패턴

이 문제에서 사용한 "양방향 그래프" 패턴은 다양한 문제에 응용됩니다:

### 친구 관계 (무방향 그래프)
```python
friendships = defaultdict(set)
# A와 B가 친구라면 양방향 저장
friendships['A'].add('B')
friendships['B'].add('A')
```

### 팔로우 관계 (방향 그래프)
```python
followers = defaultdict(set)  # 누가 나를 팔로우
following = defaultdict(set)  # 내가 누구를 팔로우

followers['Alice'].add('Bob')   # Bob이 Alice를 팔로우
following['Bob'].add('Alice')
```

### 구매 이력 (사용자↔상품)
```python
user_products = defaultdict(set)  # 사용자가 구매한 상품들
product_users = defaultdict(set)  # 상품을 구매한 사용자들

# 추천 시스템에 활용
def recommend(user_id):
    # 내가 산 상품을 산 다른 사람들
    similar_users = set()
    for product in user_products[user_id]:
        similar_users |= product_users[product]

    # 그들이 산 상품 중 내가 안 산 것
    recommendations = set()
    for user in similar_users:
        recommendations |= user_products[user]
    return recommendations - user_products[user_id]
```

## 4. 이 문제와 유사한 알고리즘 문제 유형

- **프로그래머스 - 오픈채팅방** (문자열 파싱 + 해시)
- **프로그래머스 - 위장** (해시 + 조합)
- **프로그래머스 - 베스트앨범** (해시 + 정렬)
- **백준 - 친구 네트워크** (Union-Find + 해시)
- **LeetCode - Group Anagrams** (해시 + 문자열)

## 5. 시간복잡도 함정 주의

```python
# ❌ 나쁜 예: O(N²) - 리스트에서 in 연산
blocked_users = ['user1', 'user2', 'user3', ...]  # 리스트
for user in all_users:
    if user in blocked_users:  # O(N) 탐색이 매번 발생
        pass

# ✅ 좋은 예: O(N) - 집합에서 in 연산
blocked_users = {'user1', 'user2', 'user3', ...}  # 집합
for user in all_users:
    if user in blocked_users:  # O(1) 탐색
        pass
```

**핵심**: 반복문 안에서 멤버십 테스트(`in`)를 할 때는 반드시 `set`을 사용하세요!

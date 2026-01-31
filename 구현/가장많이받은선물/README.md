# 가장 많이 받은 선물

#구현 #시뮬레이션 #해시 #완전탐색 #코딩테스트

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/258712) - 2024 KAKAO WINTER INTERNSHIP

# 문제 난이도 하

## 1. 📊 객관적 분석 및 근거

### 1.1 제약 조건 파악

| 항목 | 값 | 의미 |
|------|-----|------|
| `friends` 길이 (N) | 2 ~ 50 | 친구 수가 최대 50명으로 매우 작음 |
| `gifts` 길이 (M) | 1 ~ 10,000 | 선물 기록 최대 10,000개 |
| 친구 이름 길이 | 최대 10 | 문자열 처리 부담 없음 |
| 시간 제한 | 일반적 | O(N²) 충분히 통과 가능 |

### 1.2 시간 복잡도 역산

**기준**: 1초 ≈ 10^8 연산

| 복잡도 | N=50 | 비고 |
|--------|------|------|
| O(N²) | 2,500 ✅ | 모든 친구 쌍 비교 |
| O(M) | 10,000 ✅ | 선물 기록 순회 |
| O(N² + M) | ~12,500 ✅ | 실제 알고리즘 |

**이 문제의 경우**:
- N = 50 (친구 수), M = 10,000 (선물 기록)
- 모든 친구 쌍을 비교해도 50 × 50 = 2,500회
- 선물 기록을 순회하며 집계해도 10,000회
- **결론**: **O(N² + M)** 알고리즘으로 충분 (완전탐색 가능)

### 1.3 문제 패턴 인식

**핵심 질문**: 이 문제가 요구하는 것은 무엇인가?

| 관찰 포인트 | 이 문제에서 | 시사점 |
|-------------|-------------|--------|
| 최적해 vs 모든 경우 | 모든 친구 쌍 비교 | 완전탐색 (Brute Force) |
| 데이터 집계 필요 | A→B 선물 횟수 | 2D 테이블 or 해시맵 필요 |
| 조건 분기 | 선물 수 → 선물 지수 → 무승부 | 조건문 정확한 구현 |
| 문자열 → 인덱스 매핑 | 이름으로 접근 | 딕셔너리 활용 |

### 1.4 알고리즘 선택 및 논증

#### 🎯 최종 선택: 구현 (시뮬레이션) + 해시맵

**선택 근거 (Why this algorithm?)**

1. **문제 구조와의 적합성**
   - N이 매우 작아(≤50) 모든 친구 쌍을 비교해도 시간 충분
   - 복잡한 알고리즘 없이 문제 조건을 그대로 구현하면 됨

2. **필요한 자료구조**
   - `gift_count[A][B]`: A가 B에게 준 선물 횟수 (2D 테이블)
   - `gift_score[A]`: A의 선물 지수 (준 선물 - 받은 선물)
   - `name_to_idx`: 이름 → 인덱스 매핑 (딕셔너리)

3. **핵심 인사이트**
   - **"규칙을 정확히 구현하는 것이 핵심"**
   - 조건 우선순위: 선물 주고받은 수 비교 → 선물 지수 비교 → 무승부

#### ❌ 기각된 대안들

| 대안 | 기각 이유 |
|------|-----------|
| 그래프 알고리즘 | N이 작아서 불필요한 복잡도 |
| 정렬 기반 접근 | 쌍(pair)별 비교가 핵심이라 정렬 의미 없음 |

#### 💡 비슷한 문제에서 이 패턴을 인식하는 법

- **키워드**: "주고받은", "쌍(pair)별 비교", "조건에 따라"
- **문제 유형**: 관계 데이터 집계 후 조건부 처리
- **주의사항**:
  - 조건 우선순위 정확히 파악 (이 문제: 선물 수 → 선물 지수 → 무승부)
  - 자기 자신과의 비교 제외
  - 양방향 관계 (A→B, B→A) 구분

---

## 2. 🧠 자연어 실행 흐름

(코드 없이 순수 한글로 작성. 단계별 번호 매김)

1. **초기화**:
   - 친구 이름 → 인덱스 매핑 딕셔너리 생성
   - `gift_count[N][N]` 2D 배열 생성 (A가 B에게 준 선물 수)
   - `gift_score[N]` 배열 생성 (각 친구의 선물 지수)

2. **선물 기록 집계**:
   - `gifts` 배열 순회
   - 각 기록 "A B"를 파싱하여 `gift_count[A][B] += 1`
   - A의 선물 지수 +1, B의 선물 지수 -1

3. **모든 친구 쌍 비교** (i < j인 경우만):
   - A가 B에게 준 수와 B가 A에게 준 수 비교
   - **Case 1**: A가 더 많이 줬으면 → A가 선물 1개 받음
   - **Case 2**: B가 더 많이 줬으면 → B가 선물 1개 받음
   - **Case 3**: 같거나 기록 없음 → 선물 지수 비교
     - 선물 지수가 더 큰 사람이 선물 1개 받음
     - 선물 지수도 같으면 → 아무도 안 받음

4. **결과 계산**:
   - 각 친구가 받을 선물 수 중 최댓값 반환

---

## 3. 💻 Code Implementation

(언어: Python)
```python
def solution(friends, gifts):
    n = len(friends)
    
    # 1. 이름 → 인덱스 매핑
    name_to_idx = {name: i for i, name in enumerate(friends)}
    
    # 2. 선물 주고받은 횟수 테이블: gift_count[i][j] = i가 j에게 준 횟수
    gift_count = [[0] * n for _ in range(n)]
    
    # 3. 선물 지수: 준 선물 - 받은 선물
    gift_score = [0] * n
    
    # 4. 선물 기록 집계
    for gift in gifts:
        giver, receiver = gift.split()
        giver_idx = name_to_idx[giver]
        receiver_idx = name_to_idx[receiver]
        
        gift_count[giver_idx][receiver_idx] += 1
        gift_score[giver_idx] += 1   # 준 사람 +1
        gift_score[receiver_idx] -= 1  # 받은 사람 -1
    
    # 5. 다음 달 받을 선물 수 계산
    next_gift = [0] * n
    
    for i in range(n):
        for j in range(i + 1, n):  # 모든 쌍 비교 (i < j)
            i_to_j = gift_count[i][j]  # i가 j에게 준 횟수
            j_to_i = gift_count[j][i]  # j가 i에게 준 횟수
            
            if i_to_j > j_to_i:
                # i가 더 많이 줬으므로 i가 선물 받음
                next_gift[i] += 1
            elif j_to_i > i_to_j:
                # j가 더 많이 줬으므로 j가 선물 받음
                next_gift[j] += 1
            else:
                # 같거나 기록 없음 → 선물 지수 비교
                if gift_score[i] > gift_score[j]:
                    next_gift[i] += 1
                elif gift_score[j] > gift_score[i]:
                    next_gift[j] += 1
                # 선물 지수도 같으면 아무도 안 받음
    
    return max(next_gift)

# 시간 복잡도: O(M + N²) - 선물 기록 순회 + 모든 친구 쌍 비교
# 공간 복잡도: O(N²) - gift_count 테이블
```

**복잡도 분석**
- 시간: O(M + N²) ≈ O(10,000 + 2,500) = O(12,500)
- 공간: O(N²) ≈ O(2,500) (gift_count 테이블)

---

## 4. 🏗️ Alternative: dataclass 활용 풀이

```python
from collections import defaultdict

# 가장 간단한 방법: 일반 클래스
class Friend:
    def __init__(self, name):
        self.name = name
        self.given = 0
        self.received = 0
        self.next_gift = 0
        self.gift_to = defaultdict(int)


def solution(friends, gifts):
    # 1. 친구 객체 생성
    friend_map: dict[str, Friend] = {
        name: Friend(name=name) for name in friends
    }
    
    # 2. 선물 기록 집계
    for gift in gifts:
        giver_name, receiver_name = gift.split()
        giver = friend_map[giver_name]
        receiver = friend_map[receiver_name]
        
        giver.given += 1
        giver.gift_to[receiver_name] += 1
        receiver.received += 1
    
    # 3. 모든 친구 쌍 비교
    friend_list = list(friend_map.values())
    n = len(friend_list)
    
    for i in range(n):
        for j in range(i + 1, n):
            a, b = friend_list[i], friend_list[j]
            
            a_to_b = a.gift_to[b.name]  # a가 b에게 준 횟수
            b_to_a = b.gift_to[a.name]  # b가 a에게 준 횟수
            
            if a_to_b > b_to_a:
                a.next_gift += 1
            elif b_to_a > a_to_b:
                b.next_gift += 1
            else:
                # 선물 지수 비교 (준 - 받은)
                a_score = a.given - a.received
                b_score = b.given - b.received
                
                if a_score > b_score:
                    a.next_gift += 1
                elif b_score > a_score:
                    b.next_gift += 1
                # 같으면 아무도 안 받음
    
    # 4. 최댓값 반환
    return max(f.next_gift for f in friend_list)
```

### 💡 dataclass 버전의 장점

| 장점 | 설명 |
|------|------|
| **캡슐화** | 친구의 모든 정보(이름, 선물 내역, 지수)가 하나의 객체에 응집됨 |
| **가독성** | `a.gift_score`, `a.give_gift(b.name)` 등 의도가 명확함 |
| **확장성** | 새로운 속성/메서드 추가가 용이 |
| **디버깅** | `print(friend)` 시 자동으로 상태 출력 |

### ⚠️ 코딩 테스트에서의 트레이드오프

| 항목 | 배열 버전 | dataclass 버전 |
|------|----------|---------------|
| 코드 길이 | 짧음 ✅ | 김 |
| 작성 속도 | 빠름 ✅ | 느림 |
| 가독성 | 보통 | 좋음 ✅ |
| 실수 방지 | 인덱스 헷갈림 가능 | 타입 힌트로 안전 ✅ |
| 메모리 | 효율적 ✅ | 객체 오버헤드 |

**결론**: 
- **시간이 촉박한 코테** → 배열 버전 권장
- **가독성/유지보수가 중요한 상황** → dataclass 버전 권장

---

# 평가

## 개선할 점

1. **변수명 일관성 부족**
   - `expected`보다 README에서 사용한 `next_gift`가 문제 맥락에 더 적합
   - `gift_to`는 동사형보다 `gifts_given_to` 또는 `given_to` 같은 명사형이 더 명확

2. **선물 지수 계산 중복**
   - 매 비교 시 `a.given - a.received`를 계산하는 대신, 클래스에 `@property`로 `gift_score`를 정의하거나 초기화 시 미리 계산해두면 효율적

```python
@property
def gift_score(self):
    return self.given - self.received
```

3. **인덱스 접근 방식 혼재**
   - 48-52라인에서 `friends[i]`로 이름을 가져와 다시 `friend_map`을 조회하는 것은 비효율적
   - `list(friend_map.values())`로 직접 Friend 객체 리스트를 만들어 순회하면 더 깔끔

```python
friend_list = list(friend_map.values())
for i in range(len(friend_list)):
    for j in range(i+1, len(friend_list)):
        a, b = friend_list[i], friend_list[j]
```

4. **주석 중복**
   - 파일 상단(1-19줄)과 코드 내 주석(33, 36, 47줄)에 동일한 내용이 중복됨
   - 설계 주석은 상단에, 구현 주석은 코드 내에 분리하면 가독성 향상

## 잘한 점

1. **객체지향적 접근**
   - `Friend` 클래스로 관련 데이터를 응집시킨 것은 좋은 설계
   - 실제 코테에서 이런 접근은 실수를 줄이고 디버깅을 쉽게 함

2. **defaultdict 활용**
   - `gift_to`에 `defaultdict(int)`를 사용해 KeyError 방지
   - 없는 키 접근 시 자동으로 0 반환

3. **설계 주석 선행**
   - 코드 작성 전에 전체 흐름을 주석으로 정리한 습관은 좋음
   - 복잡한 조건 분기를 명확히 정리함

4. **정확한 알고리즘 이해**
   - 선물 횟수 → 선물 지수 → 무승부의 조건 우선순위를 정확히 구현
   - 중복 비교 방지를 위해 `i+1`부터 시작하는 패턴 적용

## 다른 응용 방안

1. **관계 데이터 집계**
   - 팔로우/팔로잉 관계 분석 (인스타그램, 트위터)
   - 송금 내역 분석 (누가 누구에게 얼마나)
   - 채팅 메시지 통계 (가장 많이 대화한 상대)

2. **조건부 우선순위 결정**
   - 순위 결정 시스템 (1차 조건 → 2차 조건 → 3차 조건)
   - 스포츠 리그 순위 결정 (승점 → 골득실 → 다득점)
   - 입사 지원자 순위 (점수 → 경력 → 자격증)

3. **쌍(pair)별 비교 패턴**
   - 토너먼트 대진표 생성
   - 1:1 매칭 시스템
   - 비교 기반 정렬 알고리즘 구현

## 추천 문제

| 문제 | 플랫폼 | 핵심 패턴 |
|------|--------|----------|
| [실패율](https://programmers.co.kr/learn/courses/30/lessons/42889) | 프로그래머스 | 조건부 정렬, 관계 데이터 집계 |
| [메뉴 리뉴얼](https://programmers.co.kr/learn/courses/30/lessons/72411) | 프로그래머스 | 조합 생성, 빈도 집계 |
| [개인정보 수집 유효기간](https://programmers.co.kr/learn/courses/30/lessons/150370) | 프로그래머스 | 조건 분기, 날짜 처리 |
| [신고 결과 받기](https://programmers.co.kr/learn/courses/30/lessons/92334) | 프로그래머스 | 해시맵, 관계 데이터 |
| [A vs B](https://www.acmicpc.net/problem/12101) | 백준 | 쌍별 비교, 조건부 처리 |

## 종합 평가

**핵심을 정확히 파악한 풀이입니다.** 문제의 조건 우선순위(선물 횟수 → 선물 지수 → 무승부)를 올바르게 이해하고, 모든 친구 쌍을 비교하는 완전탐색 접근을 적용했습니다.

`Friend` 클래스를 도입한 객체지향적 접근은 README의 Alternative 풀이와 일치하며, 이는 **가독성과 유지보수성 측면에서 좋은 선택**입니다. 다만 코테 상황에서는 배열 기반 풀이가 더 빠르게 작성될 수 있으므로, 상황에 따른 트레이드오프를 인식하고 있어야 합니다.

개선점으로는 **선물 지수를 미리 계산하거나 property로 분리**하면 반복 계산을 줄일 수 있고, **인덱스와 객체 접근 방식을 통일**하면 코드가 더 깔끔해집니다.

전반적으로 문제 이해도와 구현 정확도가 높으며, 설계 주석을 먼저 작성하는 습관이 좋습니다. 이 패턴(관계 데이터 집계 + 조건부 우선순위)을 익혀두면 유사 문제에서 빠르게 적용할 수 있습니다.

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

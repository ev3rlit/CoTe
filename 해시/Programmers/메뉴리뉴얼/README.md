# 메뉴 리뉴얼
- 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/72411

```
#해시 #조합 #빈도수카운팅
```

## 풀이 과정

### 핵심 아이디어
각 주문에서 가능한 모든 메뉴 조합을 생성하고, 각 코스 요리 갯수별로 가장 많이 주문된 조합을 찾는다.

### 접근 방법
1. 각 코스 요리 갯수(course)를 순회하면서
2. 모든 주문(orders)에서 해당 갯수만큼의 메뉴 조합을 생성 (itertools.combinations)
3. 각 조합의 빈도수를 defaultdict로 카운팅
4. 최대 빈도수가 2 이상인 경우, 최대 빈도수를 가진 모든 조합을 결과에 추가
5. 최종 결과를 알파벳순으로 정렬하여 반환

### 코드
```python
from collections import defaultdict
from itertools import combinations

def solution(orders, course):
    answer = []

    for c in course:
        menus = defaultdict(int)

        for order in orders:
            for case in combinations(sorted(order), c):
                menus[case] += 1

        if len(menus) <= 0:
            continue

        max_value = max(menus.values())
        if max_value < 2:
            continue

        for menu, count in menus.items():
            if count == max_value:
                answer.append("".join(menu))

    return sorted(answer)
```

## 회고

### 배운 점
- 리스트의 extend 메서드는 iterable 객체를 파라미터로 받아, 원소들을 리스트에 추가한다.
- combinations 함수는 iterable 객체를 파라미터로 받아, iterable을 반환함.

### 어려웠던 부분
- 문제의 입출력을 제대로 이해하지 못해, 잘못된 방향으로 풀이를 시도했다.

### 개선할 점
- 문제의 입출력을 제대로 이해하고, 문제의 요구사항을 정확히 파악하여 풀이를 시도해야 한다.
- 잘못된 방향으로 문제를 풀이할시, 주어진 시간 내에 문제를 해결하지 못할 수 있다.

---

## 평가

### 개선할 점

1. **과도한 주석**
   - 코드 내 주석이 너무 많고 중복적입니다 (solution.py:6-23)
   - 특히 22번째 줄의 긴 설명은 README에 작성하는 것이 더 적절합니다
   - 주석은 코드로 표현하기 어려운 "왜(why)"에 집중하고, "무엇을(what)" 하는지는 코드 자체로 설명되어야 합니다

2. **타입 힌트 부재**
   ```python
   def solution(orders: list[str], course: list[int]) -> list[str]:
   ```
   - 타입 힌트를 추가하면 함수 시그니처가 명확해지고 IDE 지원도 향상됩니다

3. **불필요한 검사**
   ```python
   if len(menus) <= 0:
       continue
   ```
   - 빈 딕셔너리에서 `max()`를 호출하면 ValueError가 발생하므로 이 검사는 의미가 있지만,
   - 주문이 없는 경우는 문제 조건상 발생하지 않으므로 삭제해도 무방합니다

4. **변수명 개선**
   - `c` → `course_size` 또는 `course_count`
   - `case` → `combination` 또는 `menu_combo`
   - 더 명확한 변수명으로 가독성을 높일 수 있습니다

### 잘한 점

1. **적절한 자료구조 선택**
   - `defaultdict(int)`를 사용하여 카운팅 로직을 간결하게 구현했습니다
   - 딕셔너리 키로 tuple을 사용하여 조합을 효율적으로 관리했습니다

2. **조합 생성 최적화**
   ```python
   for case in combinations(sorted(order), c):
   ```
   - 주문 문자열을 먼저 정렬하여 조합의 순서를 통일시켰습니다
   - 예: "ABC"와 "CBA"가 동일한 조합 ('A', 'B', 'C')로 인식됩니다

3. **최빈도 처리**
   - 각 코스 갯수별로 최대 빈도수를 찾아 해당하는 모든 조합을 추가하는 로직이 정확합니다
   - 최빈도가 여러 개인 경우를 올바르게 처리했습니다

4. **itertools.combinations 활용**
   - 내장 라이브러리를 적절히 활용하여 조합 생성 로직을 간결하게 구현했습니다

### 다른 응용 방안

1. **장바구니 분석 (Market Basket Analysis)**
   - 이커머스에서 함께 구매되는 상품 조합 찾기
   - 예: "맥주와 기저귀"처럼 의외의 연관성 발견

2. **추천 시스템**
   - 사용자들이 자주 선택하는 기능 조합을 바탕으로 패키지 추천
   - 예: 소프트웨어 구독 플랜 설계

3. **Apriori 알고리즘 (빈발 항목 집합)**
   - 이 문제는 빈발 항목 집합 마이닝의 단순화된 버전입니다
   - 최소 지지도(minimum support = 2)를 만족하는 항목 집합 찾기
   - 연관 규칙 학습(Association Rule Learning)의 기초

4. **메뉴 최적화**
   - 레스토랑이 실제로 고객 주문 데이터를 분석하여 세트 메뉴 구성
   - 재고 관리 및 주방 효율성 개선

### 다른 추천 문제

**조합 + 해시 유형**
1. [위장](https://school.programmers.co.kr/learn/courses/30/lessons/42578) - Level 2
   - 해시와 조합론을 결합한 문제
   - 의상 종류별로 조합 경우의 수 계산
   - 수학적 접근: (A+1) × (B+1) × (C+1) - 1

2. [후보키](https://school.programmers.co.kr/learn/courses/30/lessons/42890) - Level 2
   - 조합 + 집합 연산
   - 컬럼 조합으로 유일성과 최소성 판별
   - 비트마스킹 또는 combinations 활용

**빈도수 카운팅 유형**
3. [베스트앨범](https://school.programmers.co.kr/learn/courses/30/lessons/42579) - Level 3
   - 해시 + 정렬 + 빈도수 집계
   - 장르별 재생 횟수 합계 및 곡 정렬
   - 다중 조건 정렬 연습

4. [신고 결과 받기](https://school.programmers.co.kr/learn/courses/30/lessons/92334) - Level 1
   - 해시 + 집합 + 빈도수
   - 중복 제거 후 카운팅
   - defaultdict와 set 활용

**문자열 조합 유형**
5. [튜플](https://school.programmers.co.kr/learn/courses/30/lessons/64065) - Level 2
   - 집합 연산 + 빈도수
   - 문자열 파싱 후 원소 빈도 분석
   - Counter 또는 defaultdict 활용

6. [압축](https://school.programmers.co.kr/learn/courses/30/lessons/17684) - Level 2
   - 해시 + 문자열 처리
   - 동적으로 사전 구성하며 압축
   - LZW 압축 알고리즘 이해

**난이도 상승**
7. [순위 검색](https://school.programmers.co.kr/learn/courses/30/lessons/72412) - Level 2
   - 조합 + 해시 + 이분탐색
   - 모든 조건 조합을 미리 생성하여 해시에 저장
   - 효율성 테스트: 전처리 + 이분탐색 필수

### 종합 평가

이 문제는 조합론과 빈도수 카운팅을 결합한 전형적인 해시 문제입니다. 해결 방법은 정확하고 효율적이지만, 문제를 처음에 잘못 이해했다는 점에서 **문제 해석 능력**이 개선 포인트로 보입니다.

코드 자체는 Python의 강력한 내장 라이브러리(`collections.defaultdict`, `itertools.combinations`)를 잘 활용했으며, 알고리즘 로직도 명확합니다. 다만 solution.py 파일에 남겨진 시행착오 주석들은 학습 과정을 보여주긴 하지만, 실무에서는 깔끔하게 정리하는 것이 좋습니다.

**핵심 개선 사항:**
- 문제를 읽고 요구사항을 정확히 파악하는 연습이 필요합니다
- 입출력 예시를 손으로 직접 따라가며 패턴을 파악하는 습관을 들이세요
- 코드 주석은 최소화하고, 복잡한 설명은 README에 작성하세요

**강점:**
- 조합 생성 시 정렬을 통해 중복 방지
- 최빈도 값 추출 및 처리 로직이 정확함
- 테스트 케이스를 통한 검증 완료

이 문제는 빈발 패턴 마이닝의 기초이며, 데이터 마이닝과 추천 시스템에서 자주 사용되는 기법입니다. 이번 경험을 통해 문제 해석의 중요성과 조합 문제 해결 패턴을 체득했기를 바랍니다.

---

## 추가 학습

### 조합(Combinations) vs 순열(Permutations)
- **조합**: 순서 무관, 선택만 중요 → 메뉴 선택 (AC = CA)
- **순열**: 순서 중요 → 비밀번호, 순위 (AC ≠ CA)
- 이 문제에서는 "AC"와 "CA"가 같은 코스이므로 조합을 사용합니다

### 빈발 항목 집합 마이닝 (Frequent Itemset Mining)
- **지지도(Support)**: 항목 집합이 나타나는 빈도
- **신뢰도(Confidence)**: A를 선택했을 때 B도 선택할 확률
- **Apriori 원리**: 빈발 항목 집합의 부분집합도 빈발합니다
- 이 문제는 최소 지지도(min_support=2)를 만족하는 항목 집합 찾기입니다

### 복잡도 분석
- **시간 복잡도**: O(N × M × C(M, K))
  - N: 주문 개수
  - M: 평균 주문 메뉴 개수
  - K: 코스 요리 갯수
  - C(M, K): M개에서 K개를 선택하는 조합의 수
- **공간 복잡도**: O(총 생성된 조합 수)

### 실전 팁
1. 문제에서 "조합"이라는 키워드를 발견하면 `itertools.combinations`를 떠올리세요
2. 빈도수 카운팅은 `collections.Counter` 또는 `defaultdict(int)` 활용
3. 문자열 조합은 정렬 후 생성하여 중복 방지

---
**복잡도**: O(N × M × C(M, K)) - N:주문수, M:평균메뉴수, K:코스크기
**풀이 날짜**: 2025-11-13

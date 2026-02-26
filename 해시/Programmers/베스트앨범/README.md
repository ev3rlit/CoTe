# 베스트앨범
- 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/42579

```
#해시 #정렬 #딕셔너리
```

## 문제 설명

스트리밍 사이트에서 장르 별로 가장 많이 재생된 노래를 두 개씩 모아 베스트 앨범을 출시하려 합니다.

### 수록 기준
1. 속한 노래가 많이 재생된 장르를 먼저 수록합니다.
2. 장르 내에서 많이 재생된 노래를 먼저 수록합니다.
3. 장르 내에서 재생 횟수가 같은 노래 중에서는 고유 번호가 낮은 노래를 먼저 수록합니다.

노래의 장르를 나타내는 문자열 배열 `genres`와 노래별 재생 횟수를 나타내는 정수 배열 `plays`가 주어질 때, 베스트 앨범에 들어갈 노래의 고유 번호를 순서대로 return 하도록 solution 함수를 완성하세요.

## 풀이 과정

### 핵심 아이디어
- 장르별 총 재생 횟수를 먼저 계산하여 장르 간 우선순위를 정한다
- 각 장르 내에서 노래를 재생 횟수 내림차순, 고유번호 오름차순으로 정렬한다
- 각 장르에서 최대 2곡만 선택한다

### 접근 방법
1. `genre_plays` 딕셔너리로 각 장르별 총 재생 횟수 집계
2. `genre_music` 딕셔너리로 각 장르별 노래 리스트 저장 (노래 ID, 재생 횟수)
3. 각 장르 내 노래들을 재생 횟수 내림차순(-play), 노래 ID 오름차순(id)로 정렬
4. 장르들을 총 재생 횟수 내림차순으로 정렬
5. 각 장르에서 최대 2곡씩 선택하여 결과 배열에 추가

### 코드
```python
def solution(genres, plays):
    answers = []

    # 각 장르별 총 플레이 횟수를 집계
    genre_plays = {}
    for (genre, play) in zip(genres, plays):
        genre_plays[genre] = genre_plays.get(genre, 0) + play

    # 각 장르별 노래 플레이 횟수 집계
    genre_music = {}
    for i, (genre, play) in enumerate(zip(genres, plays)):
        if genre not in genre_music:
            genre_music[genre] = []
        genre_music[genre].append((i, play))

    # 각 장르 내 노래를 정렬 (재생 횟수 내림차순, 노래 번호 오름차순)
    for genre in genre_music:
        genre_music[genre].sort(key=lambda x: (-x[1], x[0]))

    # 장르를 총 재생 횟수 기준 내림차순 정렬
    top_genres = list(map(lambda x: x[0], sorted(genre_plays.items(), key=lambda x: x[1], reverse=True)))

    # 각 장르에서 최대 2곡 선택
    for genre in top_genres:
        count = min(2, len(genre_music[genre]))
        for i in range(count):
            music_id = genre_music[genre][i][0]
            answers.append(music_id)

    return answers
```

## 회고

### 배운 점
-

### 어려웠던 부분
-

### 개선할 점
-

---

## 평가

### 개선할 점

1. **반복문 최적화**
   - 현재 `zip(genres, plays)`를 두 번 순회하고 있습니다 (14-16라인, 19-24라인). 이를 한 번의 루프로 통합하면 더 효율적입니다.
   ```python
   # 개선 예시
   for i, (genre, play) in enumerate(zip(genres, plays)):
       genre_plays[genre] = genre_plays.get(genre, 0) + play
       if genre not in genre_music:
           genre_music[genre] = []
       genre_music[genre].append((i, play))
   ```

2. **자료구조 활용**
   - `defaultdict`를 사용하면 `if genre not in genre_music` 조건문을 제거할 수 있어 코드가 더 간결해집니다.
   - `Counter`를 사용하면 장르별 총 재생 횟수 집계가 더 pythonic해집니다.
   ```python
   from collections import defaultdict, Counter
   genre_music = defaultdict(list)
   genre_plays = Counter()
   ```

3. **복잡한 람다 표현식**
   - 30번 라인의 `map(lambda x : x[0], sorted(...))` 표현식은 가독성이 떨어집니다. 리스트 컴프리헨션이나 sorted의 key만 사용하는 것이 더 명확합니다.
   ```python
   # 개선 예시
   top_genres = sorted(genre_plays.keys(), key=lambda x: genre_plays[x], reverse=True)
   ```

4. **변수명 개선**
   - `answers`보다는 `album` 또는 `result`가 문제 맥락에 더 부합합니다.
   - `top_genres`는 이미 정렬된 상태이므로 `sorted_genres`가 더 명확합니다.

### 잘한 점

1. **명확한 단계 분리**
   - 문제를 논리적인 단계로 잘 나누었습니다: 집계 → 정렬 → 선택
   - 각 단계가 독립적이어서 디버깅과 이해가 쉽습니다.

2. **효과적인 정렬 키 사용**
   - `key=lambda x: (-x[1], x[0])`를 사용하여 다중 정렬 조건을 한 번에 처리한 점이 좋습니다.
   - 음수를 사용한 내림차순 처리가 효율적입니다.

3. **경계 조건 처리**
   - `min(2, len(genre_music[genre]))`를 사용하여 노래가 1개만 있는 장르도 안전하게 처리했습니다.

4. **zip 함수 활용**
   - `zip(genres, plays)`를 사용하여 두 배열을 효율적으로 순회했습니다.

### 테스트 케이스 검증 필요

"올라운더" 테스트 케이스의 기대값이 잘못된 것으로 보입니다:
- 입력: `(['jazz', 'pop', 'classic', 'piano'], [400, 300, 200, 100])`
- 현재 기대값: `[3, 2, 1, 0]`
- 코드 결과: `[0, 1, 2, 3]`

장르별 총 재생 횟수: jazz(400) > pop(300) > classic(200) > piano(100)이므로, 올바른 결과는 `[0, 1, 2, 3]`입니다. 테스트 케이스의 기대값을 수정해야 합니다.

### 다른 응용 방안

1. **음악 추천 시스템**
   - 사용자별 장르 선호도를 집계하고, 인기 곡을 추천하는 시스템에 적용 가능
   - 최근 N일간 트렌딩 음악 선정

2. **전자상거래 베스트셀러**
   - 카테고리별 판매량을 집계하고, 각 카테고리에서 상위 N개 상품 선정
   - 시즌별 인기 상품 큐레이션

3. **콘텐츠 큐레이션**
   - 뉴스 카테고리별 조회수 집계 후 주요 기사 선별
   - YouTube/Netflix의 카테고리별 인기 콘텐츠 선정

4. **게임 랭킹 시스템**
   - 게임 모드별 점수 집계 후 상위 플레이어 선정
   - 서버별 최고 기록 보유자 추출

### 종합 평가

이 풀이는 문제의 핵심 요구사항을 정확히 파악하고 구현했습니다. 특히 다중 정렬 조건을 효과적으로 처리한 점과 단계별로 로직을 명확히 분리한 점이 우수합니다.

다만, 같은 데이터를 두 번 순회하는 비효율성과 복잡한 람다 표현식으로 인한 가독성 저하가 아쉽습니다. 실무에서는 코드의 명확성과 유지보수성이 중요하므로, `defaultdict`와 `Counter` 같은 표준 라이브러리를 적극 활용하는 습관을 들이면 좋겠습니다.

코딩 테스트 관점에서는 시간 복잡도 O(n log n)로 최적화되어 있어 대부분의 제약 조건을 통과할 수 있습니다. 하지만 코드 가독성 향상과 Pythonic한 코드 작성을 위한 개선이 필요합니다.

## 추가 학습

### 1. collections 모듈 활용

**defaultdict**: 키가 없을 때 기본값을 자동으로 생성
```python
from collections import defaultdict
genre_music = defaultdict(list)  # if 문 없이 append 가능
```

**Counter**: 빈도 집계에 특화된 딕셔너리
```python
from collections import Counter
genre_plays = Counter()
for genre, play in zip(genres, plays):
    genre_plays[genre] += play
```

### 2. 다중 정렬 기준 패턴

튜플을 사용한 정렬은 매우 유용한 패턴입니다:
```python
# 여러 조건으로 정렬 (첫 번째 요소 우선, 같으면 두 번째 요소)
data.sort(key=lambda x: (x[0], -x[1], x[2]))
# x[0]: 오름차순, x[1]: 내림차순(음수), x[2]: 오름차순
```

### 3. 해시맵 활용 패턴

이 문제는 "그룹별 집계 + 상위 N개 선택" 패턴의 전형적인 예시입니다:
1. **집계**: 해시맵으로 그룹별 데이터 수집
2. **정렬**: 그룹 간 우선순위 결정
3. **선택**: 각 그룹에서 조건에 맞는 항목 선정

이 패턴은 다양한 문제에서 반복적으로 나타나므로 숙지하면 유용합니다.

---
**복잡도**: O(n log n) - n은 전체 노래 수
**풀이 날짜**: 2025-11-12

# 개인정보 수집 유효기간

| 항목 | 내용 |
|------|------|
| 플랫폼 | 프로그래머스 |
| 문제 | [개인정보 수집 유효기간](https://school.programmers.co.kr/learn/courses/30/lessons/150370) |
| 난이도 | Level 1 |
| 분류 | 구현, 문자열 |
| 태그 | 2023 KAKAO BLIND RECRUITMENT |

## 문제 요약

오늘 날짜를 기준으로 유효기간이 지난 개인정보 번호를 오름차순으로 반환

### 핵심 조건
- 모든 달은 28일로 통일
- 약관 종류마다 유효기간(월 수)이 다름
- 수집일 + 유효기간 = 보관 가능 마지막 날

### 입력 크기
- `terms` ≤ 20
- `privacies` ≤ 100

---

# 평가

## 개선할 점

- **`get_days` 함수 간소화**: 기준일 `(2000, 1, 1)`을 매번 함수 내부에서 정의하지 않고, 계산식을 더 직관적으로 작성할 수 있음
  ```python
  def to_days(date):
      year, month, day = date
      return year * 336 + month * 28 + day
  ```
- **변수명 일관성**: `elapsed`보다 `collected_days`가 의미를 더 명확히 전달
- **마지막 `sorted()` 불필요**: 순차적으로 `enumerate`로 순회하므로 이미 오름차순임. `sorted(answer)` 대신 `answer` 직접 반환 가능

## 잘한 점

- **모든 달 28일 조건을 이용한 일수 변환**: 날짜 계산을 단순화하여 복잡한 datetime 라이브러리 없이 해결
- **딕셔너리 컴프리헨션 활용**: `terms_map` 생성 시 `map(str.split, terms)`와 딕셔너리 컴프리헨션으로 간결하게 처리
- **주석으로 설계 흐름 기록**: 문제 분석 → 실행 흐름을 주석으로 명확히 정리

## 다른 응용 방안

- **만료일 계산 시스템**: 쿠폰, 구독, 라이선스 유효기간 관리
- **일수 변환 패턴**: 시간/날짜를 단일 단위(초, 분, 일)로 변환하여 비교하는 문제
- **조건 기반 필터링**: 특정 조건을 만족하는 항목의 인덱스 반환

## 추천 문제

- [붕대 감기](https://school.programmers.co.kr/learn/courses/30/lessons/250137) - 시간 기반 상태 관리 (구현)
- [공원 산책](https://school.programmers.co.kr/learn/courses/30/lessons/172928) - 명령 기반 시뮬레이션 (구현)
- [실패율](https://school.programmers.co.kr/learn/courses/30/lessons/42889) - 조건 필터링 + 정렬 (구현)

## 종합 평가

날짜 계산 문제의 핵심인 **단위 통일**을 잘 파악하여 모든 날짜를 일수로 변환하는 접근을 취했습니다. 이 패턴은 시간 관련 문제에서 매우 유용하며, `datetime` 라이브러리 없이도 간단히 해결할 수 있음을 보여줍니다.

다만, 경과일과 유효기간을 비교하는 조건식 `total_days - elapsed >= duration`이 직관적이지 않습니다. 수집일 + 유효기간 = 만료일로 계산한 후 `today_days > expired_days`로 비교하면 문제 설명과 더 일치하고 디버깅이 쉬워집니다.

```python
# 현재 방식
if total_days - elapsed >= duration:  # 경과일이 유효기간 이상

# 대안: 만료일 기준 비교 (더 직관적)
expired_days = elapsed + duration
if total_days >= expired_days:  # 오늘이 만료일 이후
```

전체적으로 깔끔한 풀이이며, 주석을 통한 설계 흐름 정리가 코딩 테스트에서 좋은 습관입니다.

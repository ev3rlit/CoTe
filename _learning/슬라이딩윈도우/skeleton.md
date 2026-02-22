# 슬라이딩 윈도우 Pattern Skeleton

> 생성일: 2026-02-20

---

## 암기 카드 (필수 4요소)

- **트리거 문장**
  - "연속 부분 배열/부분 문자열"
  - "길이 K 구간"
  - "최대/최소 합, 조건 만족 최소 길이"
- **핵심 불변식**
  - 현재 윈도우의 상태(합/빈도)는 포인터 1칸 이동으로 O(1) 갱신 가능
  - 각 원소는 최대 2번(들어오고 나감)만 처리되어 O(N)
- **실수 포인트**
  - 왼쪽 포인터 이동 시 상태 갱신 누락 / while 조건 실수 / 초기값 설정 오류
- **템플릿 위치**
  - 아래 `핵심 구조` 코드 블록

## 핵심 구조

```python
def min_len_subarray_at_least_target(nums, target):
    left = 0
    curr_sum = 0
    answer = float('inf')

    for right in range(len(nums)):
        curr_sum += nums[right]

        while curr_sum >= target:
            answer = min(answer, right - left + 1)
            curr_sum -= nums[left]
            left += 1

    return 0 if answer == float('inf') else answer
```

## 예제 문제 (입문 → 확장)

- 백준 2559 수열
- 백준 1806 부분합
- 프로그래머스 할인 행사

---

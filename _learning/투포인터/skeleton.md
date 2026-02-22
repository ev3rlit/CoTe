# 투포인터 Pattern Skeleton

> 생성일: 2026-02-20

---

## 암기 카드 (필수 4요소)

- **트리거 문장**
  - "정렬된 배열에서 두 수의 합/차"
  - "조건을 만족하는 쌍 찾기"
  - "양쪽에서 좁혀오기"
- **핵심 불변식**
  - 포인터 이동은 항상 탐색 공간을 줄이며, 같은 상태를 재탐색하지 않는다
  - 정렬 + 단조성(합이 크면 오른쪽 줄이기, 작으면 왼쪽 늘리기)을 이용한다
- **실수 포인트**
  - 정렬 누락 / 포인터 갱신 조건 반대로 작성 / 중복 처리 누락
- **템플릿 위치**
  - 아래 `핵심 구조` 코드 블록

## 핵심 구조

```python
def two_pointers(arr, target):
    arr.sort()
    left, right = 0, len(arr) - 1

    while left < right:
        s = arr[left] + arr[right]
        if s == target:
            return True
        elif s < target:
            left += 1
        else:
            right -= 1

    return False
```

## 예제 문제 (입문 → 확장)

- 백준 1940 주몽
- 백준 3273 두 수의 합
- 프로그래머스 숫자 게임

---

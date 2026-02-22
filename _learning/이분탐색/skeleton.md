# 이분탐색 Pattern Skeleton

> 생성일: 2026-02-20

---

## 암기 카드 (필수 4요소)

- **트리거 문장**
  - "정렬된 배열에서 빠른 탐색"
  - "정답의 범위를 줄여가며 찾기"
  - "최소/최대 가능값 (파라메트릭 서치)"
- **핵심 불변식**
  - 탐색 구간 [lo, hi] 안에 정답이 항상 존재하도록 유지
  - mid 판별 결과가 단조적(True/False 경계)을 가져야 한다
- **실수 포인트**
  - mid 계산/경계 갱신 실수 / 종료 조건 무한 루프 / lower·upper 구분 실패
- **템플릿 위치**
  - 아래 `핵심 구조` 코드 블록

## 핵심 구조

```python
def lower_bound(arr, target):
    lo, hi = 0, len(arr)
    while lo < hi:
        mid = (lo + hi) // 2
        if arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid
    return lo
```

## 예제 문제 (입문 → 확장)

- 백준 1920 수 찾기
- 백준 1654 랜선 자르기
- 프로그래머스 입국심사

---

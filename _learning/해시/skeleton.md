# 해시 Pattern Skeleton

> 생성일: 2026-02-20

---

## 암기 카드 (필수 4요소)

- **트리거 문장**
  - "존재 여부를 빠르게 확인"
  - "중복/빈도 세기"
  - "한 번 순회로 해결"
- **핵심 불변식**
  - 딕셔너리/셋 조회는 평균 O(1)
  - 현재 원소 이전 정보만으로 판단 가능한 문제는 one-pass 가능
- **실수 포인트**
  - 키 초기화 누락 / `dict.get()` 기본값 누락 / 중복 원소 처리 실수
- **템플릿 위치**
  - 아래 `핵심 구조` 코드 블록

## 핵심 구조

```python
def has_pair_sum(nums, target):
    seen = set()
    for x in nums:
        if (target - x) in seen:
            return True
        seen.add(x)
    return False
```

## 예제 문제 (입문 → 확장)

- 백준 10815 숫자 카드
- 프로그래머스 완주하지 못한 선수
- 프로그래머스 베스트앨범

---

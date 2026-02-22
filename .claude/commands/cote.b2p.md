---
description: 백준 문제의 입출력 처리 코드를 자동 생성하여 solution 함수만 구현하면 되도록 세팅합니다
---

백준 문제 $ARGUMENTS (URL 또는 문제번호)를 파싱하여 solution.py와 test.py를 생성합니다.

## 입력 인자 처리

$ARGUMENTS는 다음 형식 중 하나:
- 문제번호: `1000`
- 전체 URL: `https://www.acmicpc.net/problem/1000`

→ 문제번호 추출 후 `https://www.acmicpc.net/problem/{문제번호}`로 접근

## 작업 순서

### 1. 백준 문제 페이지 파싱

웹 페이지를 fetch하여 파싱:
- 문제 제목
- 입력 형식 설명
- 출력 형식 설명  
- 예제 입력/출력 (모든 예제)

### 2. 입출력 분석 및 함수 시그니처 결정

**입력 패턴 → 매개변수 매핑:**

| 백준 입력 패턴 | solution 매개변수 | 입력 처리 코드 |
|--------------|------------------|---------------|
| 첫 줄에 정수 1개 | `n: int` | `n = int(input())` |
| 첫 줄에 정수 2개 | `a: int, b: int` | `a, b = map(int, input().split())` |
| 첫 줄에 정수 N개 | `nums: list[int]` | `nums = list(map(int, input().split()))` |
| 문자열 1개 | `s: str` | `s = input().strip()` |
| N 주어지고, 다음 줄에 N개 정수 | `n: int, arr: list[int]` | 두 줄로 처리 |
| N, M 주어지고 N×M 격자 | `n: int, m: int, grid: list[list[int]]` | 격자 읽기 |
| T (테스트케이스 수) 주어지는 경우 | 반복문으로 처리 | `for _ in range(T):` |

**출력 패턴 → 반환값:**

| 출력 패턴 | 반환 타입 | 출력 처리 |
|----------|----------|----------|
| 정수 1개 | `int` | `print(result)` |
| 실수 1개 | `float` | `print(result)` |
| 문자열 1개 | `str` | `print(result)` |
| 여러 줄 | `list` | `print('\n'.join(...))` |
| 공백 구분 | `list` | `print(' '.join(...))` |

### 3. 파일 저장 경로 결정

문제 분석 후 저장 경로를 결정:
- **문제유형**: 알고리즘 카테고리 (DP, 그래프, 완전탐색, 그리디 등)
- **문제이름**: 백준 문제 제목

→ 저장 경로: `./{문제유형}/{백준_문제이름}/`

예시:
- 문제 1000번 "A+B" → `./구현/A+B/`
- 문제 1463번 "1로 만들기" → `./DP/1로 만들기/`

### 4. 파일 생성

`{문제유형}/{백준_문제이름}/` 폴더에 생성:

#### solution.py

```python
import sys
input = sys.stdin.readline

def solution(매개변수들) -> 반환타입:
    """
    문제 제목
    
    Parameters:
    - param1: 설명
    
    Returns:
    - 반환값 설명
    """
    # TODO: 구현
    pass

# ============================================================
# 입출력 처리 (자동 생성, 수정 금지)
# ============================================================
if __name__ == "__main__":
    # 입력 파싱
    (입력 처리 코드)
    
    # solution 실행 및 출력
    result = solution(매개변수들)
    (출력 처리 코드)
```

#### test.py

`_template_boj/test.py` 템플릿을 복사하고, `test_cases` 배열만 예제 입출력으로 채움:

```python
test_cases = [
    {
        "name": "예제 1",
        "input": """(예제 입력 문자열)
""",
        "expected": """(예제 출력 문자열)
""",
    },
    # ... 모든 예제
]
```

> **중요**: `_template_boj/test.py`의 테스트 프레임워크 코드는 그대로 유지하고 `test_cases`만 수정

## 예시

### `/cote.b2p 1000` (A+B)

**solution.py:**
```python
import sys
input = sys.stdin.readline

def solution(a: int, b: int) -> int:
    """
    A+B
    두 정수 A와 B를 입력받아 A+B를 출력
    """
    # TODO: 구현
    pass

if __name__ == "__main__":
    a, b = map(int, input().split())
    result = solution(a, b)
    print(result)
```

**test.py:**
```python
test_cases = [
    {
        "name": "예제 1",
        "input": """1 2
""",
        "expected": """3
""",
    },
]
```

### `/cote.b2p 10950` (테스트케이스 여러 개)

```python
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        a, b = map(int, input().split())
        result = solution(a, b)
        print(result)
```

## 주의사항

1. **복잡한 입력**: 문제 설명과 예제를 함께 분석하여 적합한 매개변수 구조 결정
2. **특수 출력**: 소수점 자릿수, 특정 포맷 등 출력 처리 코드에 반영
3. **다중 테스트케이스**: 반복문을 입출력 처리부에 포함, solution은 단일 케이스만 처리
4. **파일 위치**: `{문제유형}/{백준_문제이름}/` 폴더에 생성, 필요시 폴더 자동 생성
"""
테스트 케이스 정의 (프로그래머스 입출력 예시)

각 문제마다 test_cases 배열만 수정하면 됩니다.
테스트 실행 로직은 프로젝트 루트의 _runners 폴더에서 관리합니다.
"""

import sys
from pathlib import Path

# 프로젝트 루트의 _runners 모듈을 import
sys.path.insert(0, str(Path(__file__).parent.parent))
from _runners import run_tests

# ============================================================
# 테스트 케이스 정의 (문제별로 수정하는 부분)
# ============================================================
test_cases = [
    # 여러 매개변수: 튜플 사용 (언팩됨)
    # {
    #     "name": "테스트케이스",
    #     "input": (1, 2, 3),  # 튜플 = solution(1, 2, 3)으로 호출
    #     "expected": 6,
    # },

    # 단일 매개변수: 리스트, 문자열, 숫자 등 (그대로 전달)
    {
        "name": "테스트케이스 1",
        "input": ([93,30,55],[1,30,5]),
        "expected": [2,1],
    },
    {
        "name": "테스트케이스 2",
        "input": ([95,90,99,99,80,99], [1,1,1,1,1,1]),
        "expected": [1,3,2],
    },
    # 아래에 추가
]

from solution import solution

# ============================================================
# 다른 풀이 방법들
# ============================================================

# 방법 2: deque 활용
from collections import deque
import math

def solution_deque(progresses, speeds):
    queue = deque(zip(progresses, speeds))
    answer = []

    while queue:
        progress, speed = queue[0]
        days = math.ceil((100 - progress) / speed)

        count = 0
        while queue:
            progress, speed = queue[0]
            if progress + (days * speed) >= 100:
                queue.popleft()
                count += 1
            else:
                break

        answer.append(count)

    return answer


# 방법 3: 인덱스 기반
def solution_index(progresses, speeds):
    answer = []
    i = 0
    n = len(progresses)

    while i < n:
        days = math.ceil((100 - progresses[i]) / speeds[i])
        count = 1
        i += 1

        while i < n:
            next_days = math.ceil((100 - progresses[i]) / speeds[i])
            if next_days <= days:
                count += 1
                i += 1
            else:
                break

        answer.append(count)

    return answer


# ============================================================
# 테스트 실행 (수정 금지)
# ============================================================
if __name__ == "__main__":
    print("=" * 70)
    print("방법 1: 현재 풀이 (사전 계산 + 최댓값 갱신)")
    print("=" * 70)
    run_tests(solution, test_cases)

    print("\n" + "=" * 70)
    print("방법 2: deque 활용")
    print("=" * 70)
    run_tests(solution_deque, test_cases)

    print("\n" + "=" * 70)
    print("방법 3: 인덱스 기반 (메모리 최적화)")
    print("=" * 70)
    run_tests(solution_index, test_cases)

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
    {
        "name": "프로그래머스 예제",
        "input": [1, 2, 3, 2, 3],
        "expected": [4, 3, 1, 1, 0],
    },
    {
        "name": "계속 하락하는 경우",
        "input": [5, 4, 3, 2, 1],
        "expected": [1, 1, 1, 1, 0],
    },
    {
        "name": "계속 상승하는 경우",
        "input": [1, 2, 3, 4, 5],
        "expected": [4, 3, 2, 1, 0],
    },
    {
        "name": "단일 원소",
        "input": [100],
        "expected": [0],
    },
    {
        "name": "같은 가격 유지",
        "input": [5, 5, 5, 5],
        "expected": [3, 2, 1, 0],
    },
]

from solution import (
    solution,
    solution_n2,
    solution_deque,
    solution_backward,
    solution_optimized_brute
)

# ============================================================
# 테스트 실행 (수정 금지)
# ============================================================
if __name__ == "__main__":
    print("=" * 70)
    print("방법 1: O(n²) Brute Force")
    print("=" * 70)
    run_tests(solution_n2, test_cases)

    print("\n" + "=" * 70)
    print("방법 2: O(n) 스택 (기본)")
    print("=" * 70)
    run_tests(solution, test_cases)

    print("\n" + "=" * 70)
    print("방법 3: O(n) Deque")
    print("=" * 70)
    run_tests(solution_deque, test_cases)

    print("\n" + "=" * 70)
    print("방법 4: O(n)~O(n²) 역방향 순회 + 점프 포인터")
    print("=" * 70)
    run_tests(solution_backward, test_cases)

    print("\n" + "=" * 70)
    print("방법 5: O(n²) 최적화 Brute Force")
    print("=" * 70)
    run_tests(solution_optimized_brute, test_cases)

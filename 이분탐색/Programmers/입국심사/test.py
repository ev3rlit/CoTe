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
    # 입국심사 문제: n명, times 배열
    {
        "name": "예제 1",
        "input": (6, [7, 10]),  # n=6, times=[7, 10]
        "expected": 28,
    },
    {
        "name": "예제 2",
        "input": (1, [10]),  # n=1, times=[10]
        "expected": 10,
    },
    {
        "name": "예제 3",
        "input": (3, [1, 1, 1]),  # n=3, times=[1, 1, 1]
        "expected": 1,
    },
    {
        "name": "예제 4",
        "input": (10, [5, 7]),  # n=10, times=[5, 7]
        "expected": 30,
    },
]

from solution import solution

# ============================================================
# 테스트 실행 (수정 금지)
# ============================================================
if __name__ == "__main__":
    run_tests(solution, test_cases)

    # 다른 구현으로 테스트하려면:
    # def my_solution(nums):
    #     return sorted(nums)
    # run_tests(my_solution, test_cases)

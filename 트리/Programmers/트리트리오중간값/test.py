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
    # 트리 트리오 중간값: n, edges
    {
        "name": "예제 1 - 일자 트리",
        "input": (4, [[1,2],[2,3],[3,4]]),  # 1-2-3-4
        "expected": 2,
    },
    {
        "name": "예제 2 - 별 모양",
        "input": (5, [[1,5],[2,5],[3,5],[4,5]]),  # 중심 5, 끝점 1,2,3,4
        "expected": 2,
    },
    {
        "name": "예제 3 - Y자 트리",
        "input": (6, [[1,2],[2,3],[3,4],[3,5],[5,6]]),
        "expected": 3,
    },
    {
        "name": "예제 4 - 최소 트리",
        "input": (3, [[1,2],[2,3]]),  # 1-2-3
        "expected": 2,
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

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
        "input": (["apple", "banana", "cherry"], ["banana", "dragonfruit", "apple"]),
        "expected": [True, False, True],
    },
    {
        "name": "테스트케이스 2",
        "input": (["dog", "cat", "mouse"], ["cat", "elephant"]),
        "expected": [True, False],
    },
    {
        "name": "테스트케이스 3",
        "input": (["hello", "world"], ["world", "hello"]),
        "expected": [True, True],
    },
    # 아래에 추가
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

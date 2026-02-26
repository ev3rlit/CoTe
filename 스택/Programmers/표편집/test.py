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
    # 표 편집 문제: solution(n, k, cmd) - 여러 매개변수이므로 튜플 사용
    {
        "name": "예제 1",
        "input": (8, 2, ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z"]),
        "expected": "OOOOXOOO",
    },
    {
        "name": "예제 2",
        "input": (8, 2, ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z", "U 1", "C"]),
        "expected": "OOXOXOOO",
    },
    {
        "name": "단순 삭제",
        "input": (5, 0, ["D 1", "C", "D 1", "C"]),
        "expected": "OXOXO",  # 1번, 3번 행 삭제
    },
    {
        "name": "복구 테스트",
        "input": (3, 1, ["C", "Z"]),
        "expected": "OOO",
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

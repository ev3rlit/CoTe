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
        "name": "테스트케이스 1 - KAKAO",
        "input": "KAKAO",
        "expected": [11, 1, 27, 15],
    },
    {
        "name": "테스트케이스 2 - TOBEORNOTTOBEORTOBEORNOT",
        "input": "TOBEORNOTTOBEORTOBEORNOT",
        "expected": [20, 15, 2, 5, 15, 18, 14, 15, 20, 27, 29, 31, 36, 30, 32, 34],
    },
    {
        "name": "테스트케이스 3 - ABABABABABABABAB",
        "input": "ABABABABABABABAB",
        "expected": [1, 2, 27, 29, 28, 31, 30],
    },
]

from solution import solution, solutionv2

# ============================================================
# 테스트 실행 (수정 금지)
# ============================================================
if __name__ == "__main__":
    print("=" * 70)
    print("원본 solution (O(N²) - 뒤에서부터 탐색)")
    print("=" * 70)
    run_tests(solution, test_cases)

    print("\n" + "=" * 70)
    print("개선된 solutionv2 (O(N) - 앞에서부터 확장)")
    print("=" * 70)
    run_tests(solutionv2, test_cases)

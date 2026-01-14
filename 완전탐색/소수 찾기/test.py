"""
테스트 케이스 정의 (프로그래머스 입출력 예시)

각 문제마다 test_cases 배열만 수정하면 됩니다.
테스트 실행 로직은 프로젝트 루트의 _runners 폴더에서 관리합니다.
"""

import sys
from pathlib import Path

# 프로젝트 루트의 _runners 모듈을 import
# 폴더 구조에 상관없이 _runners 폴더가 있는 루트를 찾음
def find_project_root(start_path: Path, marker: str = "_runners") -> Path:
    """상위 디렉토리를 탐색하여 marker 폴더가 있는 루트를 찾음"""
    current = start_path
    while current != current.parent:  # 파일시스템 루트에 도달할 때까지
        if (current / marker).is_dir():
            return current
        current = current.parent
    raise FileNotFoundError(f"프로젝트 루트를 찾을 수 없습니다. '{marker}' 폴더가 필요합니다.")

project_root = find_project_root(Path(__file__).parent)
sys.path.insert(0, str(project_root))
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
        "input": "17",  
        "expected": 3,
    },
    {
        "name": "테스트케이스 2",
        "input": "011",  
        "expected": 2,
    },
    {
        # 1, 2, 3, 12, 13, 21, 23, 31, 32, 123, 213, 312, 321
        "name": "테스트케이스 3",
        "input": "123",  
        "expected": 5,
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

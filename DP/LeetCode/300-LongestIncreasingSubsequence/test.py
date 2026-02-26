"""
테스트 케이스 정의 (LeetCode 입출력 예시)

각 문제마다 test_cases 배열과 METHOD_NAME만 수정하면 됩니다.
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
from _runners import run_leetcode_tests

# ============================================================
# 설정 (문제별로 수정하는 부분)
# ============================================================
METHOD_NAME = "lengthOfLIS"  # LeetCode 채점 메서드명

# ============================================================
# 테스트 케이스 정의 (문제별로 수정하는 부분)
# ============================================================
test_cases = [
    {
        "name": "예제 1",
        "input": ([10, 9, 2, 5, 3, 7, 101, 18],),
        "expected": 4,
    },
    {
        "name": "예제 2",
        "input": ([0, 1, 0, 3, 2, 3],),
        "expected": 4,
    },
    {
        "name": "예제 3",
        "input": ([7, 7, 7, 7, 7, 7, 7],),
        "expected": 1,
    },
]

from solution import Solution

# ============================================================
# 테스트 실행 (수정 금지)
# ============================================================
if __name__ == "__main__":
    run_leetcode_tests(Solution, METHOD_NAME, test_cases)

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
        "input": [[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]],  
        "expected": [[7,4,6,9,1,8,5,2,3],[9,6,5,8,1,4,3,2,7]],
    },
    {
        "name": "단일 노드",
        "input": [[1,1]],  
        "expected": [[1],[1]],
    },
    {
        "name": "왼쪽으로 치우친 트리",
        "input": [[5,5],[4,4],[3,3],[2,2],[1,1]],  
        "expected": [[1,2,3,4,5],[5,4,3,2,1]],
    },
    {
        "name" : "굉장히 큰 편향된 트리",
        "input": [[i, 10000 - i] for i in range(1, 1001)],
        "expected": [[i for i in range(1, 1001)], [i for i in range(1000, 0, -1)]],
    }
    # 아래에 추가
]

from solution import solution
from solution_alternative import solution_alter as alternative_solution
from solution_index_correct import solution_index

# ============================================================
# 테스트 실행 (수정 금지)
# ============================================================
if __name__ == "__main__":
    run_tests(solution, test_cases)
    run_tests(alternative_solution, test_cases)
    run_tests(solution_index, test_cases)

    # 다른 구현으로 테스트하려면:
    # def my_solution(nums):
    #     return sorted(nums)
    # run_tests(my_solution, test_cases)

"""
테스트 케이스 정의 (백준 입출력 예시)

각 문제마다 test_cases 배열만 수정하면 됩니다.
테스트 실행 로직은 프로젝트 루트의 _runners 폴더에서 관리합니다.

추가로 testcases/ 폴더에 .in/.out 파일을 넣으면 자동으로 로드됩니다.
"""

import sys
from pathlib import Path

# 프로젝트 루트의 _runners 모듈을 import
sys.path.insert(0, str(Path(__file__).parent.parent))
from _runners import run_boj_tests

# ============================================================
# 테스트 케이스 정의 (문제별로 수정하는 부분)
# ============================================================
test_cases = [
    {
        "name": "예제 1",
        "input": """14
push 1
push 2
top
size
empty
pop
pop
pop
size
empty
pop
push 3
empty
top
""",
        "expected": """2
2
0
2
1
-1
0
1
-1
0
3
""",
    },
    {
        "name": "예제 2",
        "input": """7
pop
top
push 123
top
pop
top
pop
""",
        "expected": """-1
-1
123
123
-1
-1
""",
    },
    # 아래에 추가
]

# ============================================================
# 테스트 실행 (수정 금지)
# ============================================================
if __name__ == "__main__":
    run_boj_tests(test_cases)

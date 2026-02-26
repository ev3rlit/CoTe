"""
테스트 실행 모듈 (다중 언어/플랫폼 지원)

각 언어별, 플랫폼별 테스트 러너를 관리합니다.
- run_tests: 프로그래머스용 (함수 기반)
- run_boj_tests: 백준용 (stdin/stdout 기반)
- run_leetcode_tests: LeetCode용 (Solution 클래스 기반)
"""

from .python import run_tests
from .boj import run_tests as run_boj_tests
from .leetcode import run_tests as run_leetcode_tests

__all__ = ["run_tests", "run_boj_tests", "run_leetcode_tests"]

"""
LeetCode 테스트 실행 모듈

LeetCode 문제풀이용 Python 테스트 러너
- Solution 클래스 기반 (매 테스트마다 새 인스턴스 생성)
- lru_cache 등 상태 격리 지원
"""

import time
import tracemalloc


def format_memory(bytes_value):
    """바이트를 읽기 좋은 형식으로 변환"""
    for unit in ["B", "KB", "MB", "GB"]:
        if bytes_value < 1024:
            return f"{bytes_value:.2f}{unit}"
        bytes_value /= 1024
    return f"{bytes_value:.2f}TB"


def run_tests(solution_class, method_name, test_cases):
    """
    LeetCode 테스트 케이스 실행

    Args:
        solution_class: Solution 클래스 (인스턴스가 아닌 클래스 자체)
        method_name: 테스트할 메서드 이름 (문자열)
        test_cases: 테스트 케이스 리스트
                   [{"name": "...", "input": ..., "expected": ...}, ...]

    Examples:
        from solution import Solution

        test_cases = [
            {"name": "예제 1", "input": ([10, 9, 2, 5, 3, 7, 101, 18],), "expected": 4},
        ]

        run_tests(Solution, "lengthOfLIS", test_cases)
    """
    print("=" * 70)
    print(f"LeetCode 테스트 시작 (클래스: {solution_class.__name__}, 메서드: {method_name})")
    print("=" * 70 + "\n")

    passed_count = 0
    failed_count = 0
    total_time = 0
    max_memory = 0

    for test_case in test_cases:
        name = test_case["name"]
        input_data = test_case["input"]
        expected = test_case["expected"]

        try:
            # 매 테스트마다 새 인스턴스 생성 (lru_cache 등 상태 격리)
            instance = solution_class()
            method = getattr(instance, method_name)

            # 메모리 추적 시작
            tracemalloc.start()
            start_time = time.perf_counter()

            # 입력이 튜플이면 언팩(여러 인자), 아니면 그대로(단일 인자)
            if isinstance(input_data, tuple):
                result = method(*input_data)
            else:
                result = method(input_data)

            # 시간과 메모리 측정
            end_time = time.perf_counter()
            peak = tracemalloc.get_traced_memory()[1]
            tracemalloc.stop()

            elapsed_time = end_time - start_time
            total_time += elapsed_time
            max_memory = max(max_memory, peak)

            passed = result == expected
            status = "✓ 통과" if passed else "✗ 실패"

            if passed:
                passed_count += 1
            else:
                failed_count += 1

            print(f"[{status}] {name}")
            print(f"  입력   : {input_data}")
            print(f"  기대값 : {expected}")
            print(f"  결과값 : {result}")
            print(f"  시간   : {elapsed_time*1000:.2f}ms")
            print(f"  메모리 : {format_memory(peak)}")
            print()

        except Exception as e:
            failed_count += 1
            tracemalloc.stop()
            print(f"[✗ 에러] {name}")
            print(f"  입력 : {input_data}")
            print(f"  에러 : {e}")
            print()

    # 결과 요약
    print("=" * 70)
    print(f"테스트 완료: {passed_count} 통과, {failed_count} 실패")
    print(f"총 실행 시간 : {total_time*1000:.2f}ms")
    print(f"최대 메모리  : {format_memory(max_memory)}")
    print("=" * 70)

"""
개선된 solution - 하드코딩 제거 버전
"""
import string


def solution(msg):
    """
    LZW 압축 알고리즘 구현 (개선 버전)

    개선사항:
    1. string.ascii_uppercase 사용으로 하드코딩 제거
    2. enumerate의 start 파라미터로 의도 명확화
    3. 변수명 개선 (idx → dict_size, i → pos)
    """
    # A-Z 초기화 (하드코딩 없음!)
    dictionary = {char: idx for idx, char in enumerate(string.ascii_uppercase, start=1)}
    dict_size = len(dictionary)  # 현재 사전 크기 = 26

    pos = 0
    answer = []

    while pos < len(msg):
        # 현재 위치에서 가장 긴 문자열 찾기
        for end_pos in range(len(msg), pos, -1):
            substring = msg[pos:end_pos]
            if substring not in dictionary:
                continue

            # 출력에 색인 번호 추가
            answer.append(dictionary[substring])

            # 다음 글자를 포함한 문자열을 사전에 추가
            if end_pos < len(msg):
                dict_size += 1
                dictionary[substring + msg[end_pos]] = dict_size

            # 다음 위치로 이동
            pos = end_pos
            break

    return answer


def solution_optimized(msg):
    """
    최적화된 버전 - O(N) 복잡도

    추가 개선사항:
    4. 앞에서부터 확장하는 방식으로 O(N²) → O(N) 개선
    """
    # A-Z 초기화
    dictionary = {char: idx for idx, char in enumerate(string.ascii_uppercase, start=1)}
    dict_size = len(dictionary)

    pos = 0
    answer = []

    while pos < len(msg):
        # 현재 위치에서 한 글자부터 시작
        w = msg[pos]

        # 사전에 있는 동안 계속 확장
        while pos + len(w) < len(msg) and w + msg[pos + len(w)] in dictionary:
            w += msg[pos + len(w)]

        # 출력에 색인 번호 추가
        answer.append(dictionary[w])

        # 다음 글자를 포함한 문자열을 사전에 추가
        if pos + len(w) < len(msg):
            dict_size += 1
            dictionary[w + msg[pos + len(w)]] = dict_size

        # 다음 위치로 이동
        pos += len(w)

    return answer


if __name__ == "__main__":
    # 테스트
    test_cases = [
        ("KAKAO", [11, 1, 27, 15]),
        ("TOBEORNOTTOBEORTOBEORNOT", [20, 15, 2, 5, 15, 18, 14, 15, 20, 27, 29, 31, 36, 30, 32, 34]),
        ("ABABABABABABABAB", [1, 2, 27, 29, 28, 31, 30]),
    ]

    print("=" * 70)
    print("개선된 코드 테스트")
    print("=" * 70)

    for msg, expected in test_cases:
        result1 = solution(msg)
        result2 = solution_optimized(msg)

        status1 = "✅" if result1 == expected else "❌"
        status2 = "✅" if result2 == expected else "❌"

        print(f"\n입력: {msg}")
        print(f"  개선 버전 (O(N²)): {status1} {result1}")
        print(f"  최적화 버전 (O(N)): {status2} {result2}")

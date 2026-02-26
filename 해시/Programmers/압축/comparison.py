"""
앞에서부터 확장 vs 뒤에서부터 탐색 비교
"""

def solution_backward(msg):
    """현재 구현: 뒤에서부터 탐색 (O(N²))"""
    dictionary = {chr(i+65): i+1 for i in range(0, 26)}
    idx = 26

    i = 0
    answer = []
    steps = []  # 디버깅용

    while i < len(msg):
        # 현재 위치에서 가장 긴 길이 문자를 찾아야함
        # 뒤에서 부터 가장 긴 길이 문자를 탐색
        for j in range(len(msg), i, -1):
            if msg[i:j] not in dictionary:
                continue

            steps.append(f"위치 {i}: '{msg[i:j]}' 찾음 (범위 탐색: {len(msg)-i}번)")
            answer.append(dictionary[msg[i:j]])

            if j < len(msg):
                idx += 1
                dictionary[msg[i:j+1]] = idx
                steps.append(f"  → 사전에 '{msg[i:j+1]}' 추가 (번호: {idx})")

            i = j
            break

    return answer, steps


def solution_forward(msg):
    """개선된 구현: 앞에서부터 확장 (O(N))"""
    dictionary = {chr(i+65): i+1 for i in range(0, 26)}
    idx = 26

    i = 0
    answer = []
    steps = []  # 디버깅용

    while i < len(msg):
        # 현재 위치에서 한 글자부터 시작
        w = msg[i]

        # 사전에 있는 동안 계속 확장
        while i + len(w) < len(msg) and w + msg[i + len(w)] in dictionary:
            w += msg[i + len(w)]

        steps.append(f"위치 {i}: '{w}' 찾음 (확장 횟수: {len(w)}번)")
        answer.append(dictionary[w])

        # 다음 글자를 포함한 문자열을 사전에 추가
        if i + len(w) < len(msg):
            idx += 1
            dictionary[w + msg[i + len(w)]] = idx
            steps.append(f"  → 사전에 '{w + msg[i + len(w)]}' 추가 (번호: {idx})")

        i += len(w)

    return answer, steps


# 테스트
test_msg = "KAKAO"

print("=" * 60)
print(f"입력: {test_msg}")
print("=" * 60)

print("\n[방법 1] 뒤에서부터 탐색 (현재 구현)")
print("-" * 60)
result1, steps1 = solution_backward(test_msg)
for step in steps1:
    print(step)
print(f"\n결과: {result1}")

print("\n" + "=" * 60)
print("[방법 2] 앞에서부터 확장 (개선된 구현)")
print("-" * 60)
result2, steps2 = solution_forward(test_msg)
for step in steps2:
    print(step)
print(f"\n결과: {result2}")

print("\n" + "=" * 60)
print(f"결과 일치: {result1 == result2}")
print("=" * 60)

# 복잡도 비교
print("\n[시간 복잡도 분석]")
print("-" * 60)
print("방법 1 (뒤에서부터):")
print("  - 매 위치마다 최대 N번 탐색")
print("  - 총 복잡도: O(N²)")
print()
print("방법 2 (앞에서부터):")
print("  - 매 위치마다 사전에 없을 때까지만 확장")
print("  - 각 문자는 최대 1번만 확인")
print("  - 총 복잡도: O(N)")

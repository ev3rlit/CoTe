"""
Dictionary 초기화 방법 비교
"""
import string

print("=" * 70)
print("Dictionary 초기화 방법 비교")
print("=" * 70)

# 방법 1: 현재 방법 (하드코딩)
print("\n[방법 1] 현재 방법 - 하드코딩")
print("-" * 70)
dictionary1 = {chr(i+65): i+1 for i in range(0, 26)}
print(f"코드: dictionary = {{chr(i+65): i+1 for i in range(0, 26)}}")
print(f"결과: {dict(list(dictionary1.items())[:5])}... (총 {len(dictionary1)}개)")
print("\n장점: 간결함")
print("단점: 26 하드코딩, A의 ASCII 65도 하드코딩, 의도 불명확")

# 방법 2: string.ascii_uppercase 사용 (가장 추천!)
print("\n[방법 2] string.ascii_uppercase 사용 ✨ 추천!")
print("-" * 70)
dictionary2 = {char: idx for idx, char in enumerate(string.ascii_uppercase, start=1)}
print(f"코드: {{char: idx for idx, char in enumerate(string.ascii_uppercase, start=1)}}")
print(f"결과: {dict(list(dictionary2.items())[:5])}... (총 {len(dictionary2)}개)")
print("\n장점:")
print("  - 하드코딩 없음")
print("  - 의도 명확: 'A부터 Z까지 대문자 알파벳'")
print("  - 파이썬 표준 라이브러리 활용")
print("  - enumerate의 start 파라미터로 1부터 시작 명시")
print("단점: import 필요 (미미한 단점)")

# 방법 3: 상수 분리
print("\n[방법 3] 상수로 분리")
print("-" * 70)
ALPHABET_START = ord('A')
ALPHABET_COUNT = 26
dictionary3 = {chr(ALPHABET_START + i): i+1 for i in range(ALPHABET_COUNT)}
print(f"코드:")
print(f"  ALPHABET_START = ord('A')")
print(f"  ALPHABET_COUNT = 26")
print(f"  dictionary = {{chr(ALPHABET_START + i): i+1 for i in range(ALPHABET_COUNT)}}")
print(f"결과: {dict(list(dictionary3.items())[:5])}... (총 {len(dictionary3)}개)")
print("\n장점: 매직 넘버 제거, 상수명으로 의도 표현")
print("단점: 여전히 26 하드코딩, 코드가 길어짐")

# 방법 4: 범위 기반 (더 명확한 의도)
print("\n[방법 4] 범위 기반")
print("-" * 70)
dictionary4 = {chr(code): code - ord('A') + 1 for code in range(ord('A'), ord('Z') + 1)}
print(f"코드: {{chr(code): code - ord('A') + 1 for code in range(ord('A'), ord('Z') + 1)}}")
print(f"결과: {dict(list(dictionary4.items())[:5])}... (총 {len(dictionary4)}개)")
print("\n장점: A부터 Z까지 명확, 26 불필요")
print("단점: ord 호출이 많고, 계산식 복잡")

# 방법 5: zip 사용
print("\n[방법 5] zip 사용")
print("-" * 70)
dictionary5 = dict(zip(string.ascii_uppercase, range(1, 27)))
print(f"코드: dict(zip(string.ascii_uppercase, range(1, 27)))")
print(f"결과: {dict(list(dictionary5.items())[:5])}... (총 {len(dictionary5)}개)")
print("\n장점: 간결함")
print("단점: 27 하드코딩 필요 (26+1)")

# 방법 6: zip + enumerate (가장 범용적!)
print("\n[방법 6] string + len() 사용")
print("-" * 70)
ALPHABET = string.ascii_uppercase
dictionary6 = {char: idx for idx, char in enumerate(ALPHABET, start=1)}
print(f"코드:")
print(f"  ALPHABET = string.ascii_uppercase")
print(f"  dictionary = {{char: idx for idx, char in enumerate(ALPHABET, start=1)}}")
print(f"결과: {dict(list(dictionary6.items())[:5])}... (총 {len(dictionary6)}개)")
print("\n장점:")
print("  - 완전히 범용적 (알파벳 변경 시 ALPHABET만 수정)")
print("  - 하드코딩 전무")
print("  - 가독성 우수")
print("단점: 변수 하나 더 선언 (미미한 단점)")

# 검증
print("\n" + "=" * 70)
print("모든 방법이 같은 결과를 생성하는지 검증")
print("=" * 70)
all_same = (
    dictionary1 == dictionary2 == dictionary3 ==
    dictionary4 == dictionary5 == dictionary6
)
print(f"결과 일치: {all_same} ✅" if all_same else f"결과 불일치: {all_same} ❌")

# 실전 추천
print("\n" + "=" * 70)
print("🎯 실전 추천")
print("=" * 70)
print("""
1순위 (가장 추천): 방법 2
   import string
   dictionary = {char: idx for idx, char in enumerate(string.ascii_uppercase, start=1)}

   이유: Pythonic하고, 하드코딩 없고, 의도 명확

2순위: 방법 6
   ALPHABET = string.ascii_uppercase
   dictionary = {char: idx for idx, char in enumerate(ALPHABET, start=1)}

   이유: 알파벳 변경이 필요한 경우 (예: 소문자 포함) 유연함

피해야 할 것:
   - 매직 넘버 (26, 65)
   - 의도가 불명확한 코드
""")

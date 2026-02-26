import sys
input = sys.stdin.readline

# ============================================================
# 풀이 코드 (백준 제출용)
# ============================================================

def solve():
    # 입력 받기
    n = int(input())
    arr = list(map(int, input().split()))

    # 최대값 찾기
    max_value = max(arr)

    # 최대값으로 재 정규화 하여 평균 계산
    total = sum(map(lambda x : x / max_value * 100, arr))

    print(total/n)


if __name__ == "__main__":
    solve()

import sys
input = sys.stdin.readline


def solution(n: int, k: int, items: list[tuple[int, int]]) -> int:
    """
    평범한 배낭 (BOJ 12865)

    Parameters:
    - n: 물품의 수
    - k: 버틸 수 있는 무게
    - items: (무게, 가치) 튜플 리스트

    Returns:
    - 배낭에 넣을 수 있는 물건들의 가치합의 최댓값
    """

    dp = [0] * (k + 1)

    for w_i, v_i in items:
        for w in range(k, w_i - 1, -1):
            dp[w] = max(dp[w], dp[w-w_i] + v_i)
    
    return dp[k]


# ============================================================
# 입출력 처리 (자동 생성, 수정 금지)
# ============================================================
if __name__ == "__main__":
    n, k = map(int, input().split())
    items = []
    for _ in range(n):
        w, v = map(int, input().split())
        items.append((w, v))

    result = solution(n, k, items)
    print(result)

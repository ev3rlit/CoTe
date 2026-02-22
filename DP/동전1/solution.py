import sys
input = sys.stdin.readline


def solution(n: int, k: int, coins: list[int]) -> int:
    """
    동전 1 (BOJ 2293)

    Parameters:
    - n: 동전의 종류 수
    - k: 만들려는 금액
    - coins: 각 동전의 가치 리스트

    Returns:
    - k원을 만드는 경우의 수
    """

    dp = [0] * (k+1)
    # 금액 0원을 만드는 방법은 아무것도 안쓰는 1가지
    dp[0] = 1

    for coin in coins:
        for j in range(coin, k+1):
            dp[j] = dp[j] + dp[j-coin]

    return dp[k]


# ============================================================
# 입출력 처리 (자동 생성, 수정 금지)
# ============================================================
if __name__ == "__main__":
    n, k = map(int, input().split())
    coins = []
    for _ in range(n):
        coins.append(int(input()))

    result = solution(n, k, coins)
    print(result)

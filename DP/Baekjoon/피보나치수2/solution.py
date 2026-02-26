import sys
input = sys.stdin.readline


def solution(n: int) -> int:
    """
    피보나치 수 2 (BOJ 2748)

    Parameters:
    - n: 피보나치 수의 인덱스

    Returns:
    - n번째 피보나치 수
    """

    dp = [0] * (n+1)
    dp[0] = 0
    dp[1] = 1

    for i in range(2, n+1, 1):
        dp[i] = dp[i-1]+ dp[i-2]
    
    return dp[n]


# ============================================================
# 입출력 처리 (자동 생성, 수정 금지)
# ============================================================
if __name__ == "__main__":
    n = int(input())
    result = solution(n)
    print(result)
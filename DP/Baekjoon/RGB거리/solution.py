import sys
input = sys.stdin.readline

# 각 집의 인접한 경우 색을 달라야함
# 색은 R,G,B중 하나
# 칠하는 최소한의 비용
# dp[i][j] = i번째 집을 j색으로 칠할 때의 최소비용

# 입력 크기는 N 1000
# bottom up 
# 집이 3개이고 다음 순서대로 하면 최솟값임  R, B, R -> 96
# 음 이전 집에서 현재와 다른 색상을 칠하는 경우의 최소값을 구하는 것임
# j가 0이면 R, 1이면 G, 2이면 B
# dp[i][j] = min(dp[i-1][j-1], ..., dp[i-1][j+1]) + costs[i][j]

def solution(n: int, costs: list[list[int]]) -> int:
    """
    RGB거리
    
    N개의 집을 빨강, 초록, 파랑 중 하나로 칠할 때,
    인접한 집은 같은 색으로 칠할 수 없다.
    모든 집을 칠하는 비용의 최솟값을 구한다.
    
    Parameters:
    - n: 집의 수 (2 ≤ N ≤ 1,000)
    - costs: 각 집을 [R, G, B]로 칠하는 비용 (N×3 배열)
    
    Returns:
    - 모든 집을 칠하는 비용의 최솟값
    """

    # DP 테이블 초기화, 이전행만 저장
    prev = costs[0][:]
    colors = len(costs[0])

    for i in range(1,n):
        curr = [0]*colors

        # R인 경우, G, B 중 최소값과 현재 R의 값을 더함
        # curr[0] = min(prev[1],prev[2]) + costs[i][0]
        # curr[1] = min(prev[0],prev[2]) + costs[i][1]
        # curr[2] = min(prev[0],prev[1]) + costs[i][2]

        for j in range(colors):
            curr[j] = min(prev[(j+1)%colors], prev[(j+2)%colors]) + costs[i][j]

        prev = curr

    return min(prev)

# ============================================================
# 입출력 처리 (자동 생성, 수정 금지)
# ============================================================
if __name__ == "__main__":
    n = int(input())
    costs = [list(map(int, input().split())) for _ in range(n)]
    
    result = solution(n, costs)
    print(result)

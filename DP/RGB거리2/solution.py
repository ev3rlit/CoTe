import sys
input = sys.stdin.readline


# RGB 거리 문제에서 선형이 아닌 원형을 도입
# 이문제는 기존 도둑질과 유사함
# 다른말로하면 기존 로직과 동일한데
# 첫번째 집과 맨 마지막집의 색상이 다르면됨

def solution(n: int, costs: list[list[int]]) -> int:
    """
    RGB거리2
    
    Parameters:
    - n: 집의 수 (2 ≤ N ≤ 1,000)
    - costs: 각 집을 [R, G, B]로 칠하는 비용 (N×3 배열)
    
    Returns:
    - 모든 집을 칠하는 비용의 최솟값
    """


    colors = len(costs[0])
    INF = float('inf')

    answer = INF

    # 첫번째 집은 R,G,B 각 색상 중 하나로 고정하여 DP
    for first_color in range(colors):

        # DP에따라서 현재 집은 이전집 최솟값 + 현재집비용
        prev = [INF] * colors
        prev[first_color] = costs[0][first_color]

        for i in range(1, n-1):
            curr = [0]*colors
            for j in range(colors):
                curr[j] = min(prev[(j+1)%colors], prev[(j+2)%colors]) + costs[i][j]
            prev = curr

        # 맨마지막 색상은 첫번째 색상과 다르게 칠해야함
        for last_color in range(colors):
            if last_color == first_color:
                continue

            cost = min(prev[(last_color+1)%colors], prev[(last_color+2)%colors]) + costs[n-1][last_color]

            answer = min(answer, cost)

    return answer

# ============================================================
# 입출력 처리 (자동 생성, 수정 금지)
# ============================================================
if __name__ == "__main__":
    n = int(input())
    costs = [list(map(int, input().split())) for _ in range(n)]
    
    result = solution(n, costs)
    print(result)

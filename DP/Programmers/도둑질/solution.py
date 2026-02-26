# 2칸마다 한집을 선택할 수 있음. 
# 원형이므로 첫번재 집을 선택하는 경우 마지막집은 못함
# 첫번째 집을 건너띄는 경우 마지막집 선택 가능
# dp[i] = i번째 집에서 최대값
# dp[i] = max(dp[i-1], dp[i-2]+money[i])
# 1칸전 집의 최대값을 하거나, 2칸전 집에서 도둑질을 하는 경우

def solution(money):
    n = len(money)
    
    if n == 3:
        return max(money)
    
    # prev1, prev2로 순회하는 이유는 무엇인가?
    # prev1, prev2
    # 1. 0, 0
    # 2. 1, 0
    # 3. 2, 1
    # 4. 4, 2
    # 변수 2개로 1칸전과 2칸전을 저장하면서 최적화가 가능함.
    def rob_linear(start,end):
        prev2, prev1 = 0,0
        for m in range(start,end+1):
            prev2, prev1 = prev1, max(prev1, prev2+money[m])
        return prev1
    
    # 첫번째집 포함, 마지막집 제외
    case1 = rob_linear(0,n-2)
    
    # 첫번째집 제외, 마지막집 포함
    case2 = rob_linear(1,n-1)
    
    return max(case1,case2)
# 총 길이는 201이며,  홀수이므로 피연산자와 연산자가 2:1
# 연산자와 숫자는 항상 절반, 즉 숫자와 연산자가 규칙적으로 배치됨
# dp[i][j] = i~j구간 사이의 최대 결과
# 두 연산 결과 A, B가 있을때 최대 결과를 위한 경우
# max(A) + max(B)
# max(A) - min(B)

# dp하나로는 최대값 밖에 못구하기 때문에,  dp_max, dp_min을 이용해서 두 구간 i~j 사이의 최대, 최소값 보관

# 1. 입력파싱
# - 배열에서 숫자만 추출
# - 배열에서 연산자만 추출
# 2. DP 테이블 초기화 dp_max[i][i] = nums[i] 구간별 초기값은 자기자신
# 3. Buttom up 방식으로  2 ~ len(nums) 까지 진행
# - 각 구간 [i,j]에 대해서 모든 분할 시도 k (i <= k < j)
# - 모든 연산자 ops[k]에 따라 최대 최소 계산

# 4.최종 결과
# dp_max[0][n-1] = 0 ~ n-1까지의 전체 구간의 최대값

def solution(arr):
    
    # 1. 입력파싱
    nums = []
    ops = []
    for i, x in enumerate(arr):
        # 짝수 구간마다 연산자 배치
        if i % 2 == 0:
            nums.append(int(x))
        else:
            ops.append(x)
    
    n = len(nums)
    
    # 2. DP 초기화 적당히 큰수
    INF = 2**63
    dp_max = [[-INF] * n for _ in range(n)]
    dp_min = [[INF] * n for _ in range(n)]

    for i in range(n):
        dp_max[i][i] = nums[i]
        dp_min[i][i] = nums[i]
    
    # 3. 
    for length in range(2, n+1):
        for i in range(n-length+1):
            j = i + length-1
                
            for k in range(i,j):
                op = ops[k]
                
                if op == '+':
                    dp_max[i][j] = max(dp_max[i][j], dp_max[i][k]+dp_max[k+1][j])
                    dp_min[i][j] = min(dp_min[i][j], dp_min[i][k]+dp_min[k+1][j])
                else:
                    dp_max[i][j] = max(dp_max[i][j], dp_max[i][k]-dp_min[k+1][j])
                    dp_min[i][j] = min(dp_min[i][j], dp_min[i][k]-dp_max[k+1][j])
   
    
    return dp_max[0][n-1]

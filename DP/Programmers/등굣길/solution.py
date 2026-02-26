# m이 가로 x,  n이 세로 y
# m과n은 100이하 100x100 = 10000가지?
# 바로 도착 케이스는 없음
# dp[y][x] = 
# 이문제는 y만큼 갔을때  x만큼 이동했을때 최단 경로를 구하는건가?
# dp[y][x] = y,x 이동시 최단 경로의 갯수
# 이 문제에서 길을 가는 경우는  오른쪽으로가거나 내려가거나 밖에 없음.
# 현재 위치의 최단 경로의 갯수는  dp[y][x] = 오른쪽으로 오는 경우 dp[y][x-1] + 위에서 오는 경우 dp[y-1][x]
# 만약 해당 위치에 물웅덩이가 있으면 dp[y][x] = 0

# dp 공간 초기화
# dp[1][1] = 1, 현재 위치는 1번만 가능
# 물웅덩이 조회를 위해 집합으로 변경
# 행과 열을 기준으로 2차원 순회
# dp[y][x]물웅덩이인 경우 0으로 설정
# dp[y][x] = dp[y-1][x] + dp[y][x-1]

def solution(m, n, puddles):
    MOD = 1_000_000_007
    height, width = n, m
    
    # 기준 좌표가 1,1 부터 시작하므로 dp 공간 크기는 +1
    dp = [[0] * (width+1) for _ in range(height+1)]
    dp[1][1] = 1
    
    puddle_set = {(y,x) for (x,y) in puddles}
    
    
    for y in range(1,height+1):
        for x in range(1,width+1):
            # 시작점은 무시
            if y == 1 and x == 1:
                continue
            
            if (y,x) in puddle_set:
                dp[y][x] = 0
            else:                
                dp[y][x] = (dp[y-1][x] + dp[y][x-1]) % MOD
    
    return dp[height][width]
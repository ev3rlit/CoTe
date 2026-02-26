# dp[k] = N를 k번 사용할때 나올 수 있는 모든 결과의 집합
# dp[k] = dp[i] 번 사용한 집합 과  dp[k-i] 번 사용한 집합

# 최대 8까지 가능함.  

# 1~8 k번 사용하는 집합인 dp 초기화
# 1~8까지 k를 순회
# N을 k번 이어붙인 케이스도 추가
# dp[i]와 dp[k-i]를 이용한 모든 사칙연산 조합


def solution(N, number):
    
    if N == number:
        return 1
    
    dp = [set() for _ in range(9)]
        
    for k in range(1,9):
        repeated = int(str(N)*k)
        dp[k].add(repeated)
        
        for i in range(1,k):
            for a in dp[i]:
                for b in dp[k-i]:
                    
                    # 왜 a-b와 b-a는 서로 다른 결과인데 신경쓰지 않는가?
                    # 이는 a//b와 b//a도 결과가 다르지만 없음?
                    dp[k].add(a+b)
                    dp[k].add(a-b)
                    dp[k].add(a*b)
                    if b != 0:
                        dp[k].add(a//b)
                        
        if number in dp[k]:
            return k
        
    # 8번 이내 못찾은 경우 -1
    return -1
# 초기 접근 방법은 최소 비용이므로 BFS로 풀었으나
# 이동 경로마다 가중치가 다르므로 BFS 접근으로는 도착 지점이 최소일수가 없음
# 다익스트라 방법을 이용해야 문제를 풀 수 있었음.

# 위치별 이동 방향에 따라 비용이 다다름
# 최소 비용 가지치기를 해야함

# 다음 비용 계산은  직전 방향과 다음으로 이동할 방향이 다르면 코너 비용 추가함

from heapq import heappop, heappush

def solution(board):
    
    N = len(board)
    dirs = [(-1,0),(0,1),(1,0),(0,-1)]
    INF = float('inf')
    
    costs = {}
    for y in range(N):
        for x in range(N):
            for (dy,dx) in dirs:
                costs[(y,x,dy,dx)] = INF
    
    pq = []
    if board[0][0] == 0:
        for (dy,dx) in dirs:
            costs[(0,0,dy,dx)] = 0
        # 비용, y,x, prev_dir(-1은 시작)
        heappush(pq, (0,0,0,0,0))
    
    min_cost = INF
    
    while pq:
        cost, y,x, prev_dy,prev_dx = heappop(pq)
        
        if (y,x) == (N-1,N-1):
            min_cost = min(min_cost, cost)
            continue
        
        # 4방향 이동
        for (dy,dx) in dirs:
            ny,nx = y + dy, x + dx
            
            # 경계
            if not(0 <= ny < N and 0 <= nx < N):
                continue
            
            # 벽
            if board[ny][nx] == 1:
                continue
                
            # 비용 계산
            next_cost = cost + 100
            if (0,0) != (prev_dy,prev_dx) and (dy,dx) != (prev_dy,prev_dx):
                next_cost += 500
                
            # 최소 비용 갱신
            if next_cost < costs[(ny,nx,dy,dx)]:
                costs[(ny,nx,dy,dx)] = next_cost
                heappush(pq,(next_cost,ny,nx,dy,dx))
    
    return min_cost
from heapq import heappush, heappop

def solution(board):
    N = len(board)
    # 상, 하, 좌, 우
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    
    # 3차원 비용 배열: costs[y][x][direction]
    # direction: 0:상, 1:하, 2:좌, 3:우
    INF = float('inf')
    costs = [[[INF] * 4 for _ in range(N)] for _ in range(N)]
    
    pq = []
    
    # 시작점 초기화
    # 시작점에서는 방향이 없으므로, 이동 가능한 방향(하, 우)으로 초기 비용을 넣고 시작
    # (0,0)은 항상 0이므로, (0,0)에서 출발하는 것으로 처리
    if board[0][0] == 0:
        for i in range(4):
            costs[0][0][i] = 0
        heappush(pq, (0, 0, 0, -1)) # cost, y, x, prev_dir (-1은 시작점 표시)

    min_cost = INF

    while pq:
        curr_cost, y, x, prev_dir = heappop(pq)
        
        # 도착점 도달 시 최소 비용 갱신 (다익스트라라 처음 도착이 최소일 수 있지만, 방향 때문에 끝까지 확인)
        if y == N - 1 and x == N - 1:
            min_cost = min(min_cost, curr_cost)
            continue
            
        # 4방향 이동
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            
            # 범위 및 벽 체크
            if 0 <= ny < N and 0 <= nx < N and board[ny][nx] == 0:
                # 비용 계산: 기본 100원
                new_cost = curr_cost + 100
                
                # 코너 비용 추가 (시작점이 아니고, 방향이 다르면)
                if prev_dir != -1 and prev_dir != i:
                    new_cost += 500
                
                # 최소 비용 갱신 조건
                # 해당 방향으로 들어오는 비용이 더 작을 때만 갱신
                if new_cost < costs[ny][nx][i]:
                    costs[ny][nx][i] = new_cost
                    heappush(pq, (new_cost, ny, nx, i))
    
    # 도착점의 4방향 비용 중 최솟값 반환 (혹은 while문 내 min_cost)
    return min(costs[N-1][N-1])
# 입력 크기는 100 * 100 이므로 최대 1만
# 목표는?  위치 G로 이동하는데 최소 움직임
# 현재 위치에서 4방향 이동 하면서  BFS로 이동
# 각 경우 마다 방문 여부가 필요할거같음

# 미끄러진다라는 것은?
# 주어진 방향으로 이동 처리시, 벽을 만날때까지 움직이는것임
# 당장 떠오르는 방법은   현재 위치 및  축 방향을 기준으로 +1 순회하면서 벽이 나오기 전까지 이동하는것임
# BFS 상태에 저장할것은?   방문여부, 이동횟수, 

# 종결조건 - G 도착시
# 예외조건 - 모두 방문한 경우 =  len(set) == 넓이


# 실행 흐름
# 1. 초기화
# - 보드에서 시작점 R화 G의 좌표를 확인
# - BFS 큐에 ((시작위치), 이동횟수)
# - 방문 set[(y,x)]에 시작점을 방문처리
# 2. 큐가 비어있을때 까지 순회
# 3. 현재 상태 pop
# 4. 현재 위치가 목표 위치면 현재 이동 횟수 반환
# 5. 4방향 슬라이드탐색
# - 현재 위치에서 해당 방향으로 한칸씩 이동, 
# - 장애물이면 멈춤, 벽이면 멈춤, 방문처리
# - 큐에 ((y,x), 이동횟수 +1) 저장

# - 큐가 비었는데 아직 도착못했다면? -1을 반환

from collections import deque

def solution(board):
    height,width = len(board), len(board[0])
    R = (0,0)
    G = (0,0)
    
    for y in range(height):
        for x in range(width):
            if board[y][x] == 'R':
                R = (y,x)
            elif board[y][x] == 'G':
                G = (y,x)
    
    # 북 동 남 서
    directions = [(-1,0),(0,1),(1,0),(0,-1)]
    
    # 큐 ((y,x), 이동 횟수)
    queue = deque([(R,0)])
    visited = set([R])
    
    def is_wall(y,x):
        if y < 0 or y >= height:
            return True
        if x < 0 or x >= width:
            return True
        if board[y][x] == 'D':
            return True
        return False
    
    while queue:
        ((y,x),moves) = queue.popleft()
        
        if G == (y,x):
            return moves
        
        # 4방향 탐색
        
        for (dy,dx) in directions:
            # 현재 위치 기준 슬라이딩
            ny,nx = y,x
            
            # 벽이나 장애물에 부딪히기 전까지
            # 슬라이딩
            while not is_wall(ny+dy,nx+dx):
                ny += dy
                nx += dx
                
            # 방문한 경우 무시
            if (ny,nx) in visited:
                continue
                
            # 이동이 없는 경우 무시
            if (ny,nx) == (y,x):
                continue
                
            # 새위치 방문 처리 및 큐에 추가
            visited.add((ny,nx))
            queue.append(((ny,nx), moves +1))
            
    return -1
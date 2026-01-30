def solution(grid):
    answer = []
    
    height = len(grid)
    width = len(grid[0])
    
    # 방향 정의 (y,x)
    directions = [(-1,0),(0,1),(1,0),(0,-1)]
    
    
    # 방문 체크 (y,x,d)
    visited = set()
    
    for y in range(height):
        for x in range(width):
            for d in range(len(directions)):
                # 새로운 싸이클 발견
                dy,dx = directions[d]
                if (y,x,dy,dx) not in visited:
                    count = 0
                    cy, cx = y,x
                    
                    while (cy,cx,dy,dx) not in visited:
                        visited.add((cy,cx,dy,dx))
                        count += 1
                        
                        # 현재 위치 기준 처리
                        # 'S' 직진  dy,dx 그대로
                        # 'L' 좌회전   
                        # 'R' 우회전 
                        char = grid[cy][cx]
                        if char == 'L':
                            dy,dx = directions[(d-1)%len(directions)]
                            d = d-1
                        elif char == 'R':
                            dy,dx = directions[(d+1)%len(directions)]
                            d = d+1
                        
                        # 다음 좌표 이동
                        cy = (cy + dy) % height
                        cx = (cx + dx) % width
                    
                    # 사이클 종료 및 길이 저장
                    answer.append(count)
    
    return sorted(answer)
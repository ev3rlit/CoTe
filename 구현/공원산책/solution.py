# 명령 대로 처리하지만,  2가지를 만족하지 않는 경우 해당 명령은 무시됨
# 좌표는 0 base
# 공원 그리드와 명령이 배열로 제공


# 주어진 방향으로 이동할때 공원을 벗어나는지 확인
# 주어진 방향으로 이동중 장애물을 만나는지 확인

# 1. 값 초기화 
# - 시작 위치 확인
# - 현재 위치 초기화
# 2. routes 순회
# - 이동한 위치가 범위 안에 있는지 확인
# - 이동한 위치 사이에 장애물 확인
# - 두 조건을 만족하면 이동
# 3. 최종 좌표 반환
    
def solution(park, routes):
    # 북동남서 좌표계(y,x)
    directions = {'N' : (-1,0), 'E' : (0,1), 'S' : (1,0), 'W':(0,-1)}
    
    print(directions['N'])
    
    # 1. 값 초기화 
    # 시작 위치 확인
    # 현재 위치 초기화
    width, height = len(park[0]), len(park)
    current_x, current_y = 0, 0
    for y in range(height):
        for x in range(width):
            if 'S' == park[y][x]:
                current_y, current_x = y,x
                break
                
    # 2. routes 순회
    # map을 사용하여 파싱 로직 분리 (direction, steps_str)
    for direction, steps_str in map(str.split, routes):
        steps = int(steps_str)
        
        dir_y, dir_x = directions[direction]
        ny, nx = current_y + dir_y * steps, current_x + dir_x * steps
        
    # - 이동한 위치가 범위 안에 있는지 확인
        if not (0 <= ny < height and 0 <= nx < width):
            continue
    
    # - 이동한 위치 사이에 장애물 확인
        found_obstacle = False
        for s in range(1,steps+1):
            # 현재 위치에서 주어진 방향으로 한칸씩 이동하면서 장애물 확인
            temp_y = current_y + dir_y * s
            temp_x = current_x + dir_x * s
            if not (0 <= temp_y < height and 0 <= temp_x < width):
                found_obstacle = True
                break
            
            if 'X' == park[temp_y][temp_x]:
                found_obstacle = True
                break
        
        if found_obstacle:
            continue
            
    # - 두 조건을 만족하면 이동
        current_y, current_x = ny, nx
    
    # 3. 최종 좌표 반환
    return [current_y, current_x]
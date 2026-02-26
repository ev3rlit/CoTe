# dirs를  순회
# 해당 방향으로 이동 가능한지 확인
# 이동 가능하면 이동 처리
# 이동하지 않은 방향이면 이동 거리 증가
# 이동한 방향 기록 (양방향)

# 필요한 변수
# 이동한 거리 
# 방향 방문 여부

def validPosition(x, y):
    return (-5 <= x <= 5) and (-5 <= y <= 5)

def nextPosition(x,y,dir) :
    if dir == 'U':
        return x,y+1
    if dir == 'D':
        return x,y-1
    if dir == 'R':
        return x+1, y
    if dir == 'L':
        return x-1, y
    return x,y

def solution(dirs):
    visited = set()
    cx, cy = 0, 0

    for dir in dirs:
        nx,ny = nextPosition(cx,cy,dir)
        if not validPosition(nx,ny):
            continue

        visited.add((cx,cy,nx,ny))
        visited.add((nx,ny,cx,cy))

        cx,cy = nx,ny

    return int(len(visited)/2)

def ValidatePosition(x, y, xrange, yrange) -> bool:
    return -xrange <= x <= xrange and -yrange <= y <= yrange

 
DIRECTIONS   = {
        'U' : (0, 1),
        'D' : (0, -1),
        'R' : (1, 0),
        'L' : (-1, 0)
    }

def NextPosition(directions, dir, x, y) -> tuple[int,int]:
    dx, dy = directions.get(dir, (0,0))
    return x + dx, y + dy

def solutionv2(dirs):
    visited = set()
    cx, cy = 0, 0
    xrange, yrange = 5, 5

    for dir in dirs:
        nx, ny = NextPosition(DIRECTIONS, dir, cx, cy)
        if not ValidatePosition(nx, ny, xrange, yrange):
            continue

        edge = tuple(sorted([(cx, cy), (nx, ny)]))
        visited.add(edge)

        cx, cy = nx, ny

    return len(visited)
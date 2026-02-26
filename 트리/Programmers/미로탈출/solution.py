# 맵이 주어져 있고,  한칸씩 이동 가능하며, S에서 E로 가는 최단 경로의 칸 수를 구하는 문제
# 만약 갈수 없다면 -1 을 반환

# 너비 우선 탐색으로 1칸씩 이동하면, 최단 경로로 갈 수 있음
# 'E'를 처음으로 탐방한 곳이 있으면 그곳이 최단 경로임
# 모든 곳을 다 탐색했는데 'E'가 없다면  도착 못한것임

# 맵을 순회하면서 'S', 'E' 위치를 찾기
# 레버를 당겼는지 안당겼는지 상태가 필요함

from collections import deque
from dataclasses import dataclass


directions = [(1,0), (-1, 0), (0,1), (0,-1)]

@dataclass(frozen=True)
class Trace:
    # 좌표
    x : int
    y : int
    # 레버 여부
    lever : int 

def solution(maps):

    # Trace
    visited = set()

    # (x 좌표, y 좌표, 경과시간, 레버 여부)
    queue = deque()

    # 맵을 순회하면서 시작점, 도착점 찾기
    start_x, start_y = (-1, -1)
    end_x, end_y = (-1, -1)

    height, width= len(maps), len(maps[0])
    for y in range(height):
        for x in range(width):
            if maps[y][x] == 'S':
                start_y = y
                start_x = x
            elif maps[y][x] == 'E':
                end_y = y
                end_x = x
    

    # 경로 탐색
    queue.append((start_x,start_y,0,0))
    while queue:

        x, y, count, lever = queue.popleft()

        if x == end_x and y == end_y and lever == 1:
            return count
        
        # 4방향 이동 여부 확인
        for (dx, dy) in directions:
            nx, ny = x+dx, y+dy

            # 경계 안에 있는지 확인
            if (0 <= nx < width and 0 <= ny < height) != True:
                continue

            # 이동 가능한지 확인
            if maps[ny][nx] == 'X':
                continue

            # 방문 여부 확인
            if Trace(nx,ny,lever) in visited:
                continue
        
            # 다음 이동이 레버라면 그 때부 레버는 활성화됨
            if maps[ny][nx] == 'L':
                queue.append((nx,ny, count+1, 1))
                visited.add(Trace(nx,ny,1))
            else:
                queue.append((nx,ny,count+1, lever))
                visited.add(Trace(nx,ny,lever))

    return -1
    
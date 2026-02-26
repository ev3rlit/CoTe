# 너비 우선 탐색으로 갈 수 있는 길을 탐색하며, 도착한 경우 그곳이 최단 거리
# 탐색을 하였으나, 도착지 까지 도달하지 못한 경우 -1을 저장
# 큐의 노드 정보에는   x 좌표, y 좌표, 이동 거리  세가지만 있으면 될듯함
# 그리고 재방문하지 않아야 최단 거리가 되므로  방문 여부 추가

# 방문 여부와 노드는  튜플로 관리

from collections import deque

directions = [(-1,0),(1,0),(0,-1),(0,1)]

def solution(maps):

    # (x, y)
    visited = set()

    # (x, y, moves)
    queue = deque()

    # 0,0 부터 이동합니다.

    # 큐에서 이동 정보를 가져옵니다
    # 현재 위치가 도착지라면 이동 거리와 함께 종료
    # 이동 정보를 토대로 4방향을 탐색
    # 각 방향으로 이동 가능하면  방문 여부 및 큐에 저장

    # 못찾은 경우 -1 반환

    height,width = len(maps), len(maps[0])

    queue.append((0,0,1))
    visited.add((0,0))
    while queue:

        # 다음 이동 정보
        x, y, moves = queue.popleft()

        # 도착 여부 확인
        if x == width-1 and y == height -1:
            return moves
        
        for (dx, dy) in directions:
            nx, ny = x + dx, y + dy

            # 이동 경계 확인
            if not (0 <= nx < width and 0 <= ny < height):
                continue

            # 이동 가능 여부 확인
            if maps[ny][nx] == 0:
                continue

            # 방문 여부 확인
            if (nx,ny) in visited:
                continue

            # 방문 처리
            visited.add((nx,ny))

            # 다음 이동 정보 추가
            queue.append((nx,ny,moves+1))

    # 도착 하지 못한 경우 -1
    return -1
    
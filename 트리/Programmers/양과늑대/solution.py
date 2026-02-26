from collections import defaultdict
from collections import deque

def solution(info, edges):

    # 노드에 저장할 정보는  양의 수, 늑대 수, 현재 활성화된 노드 인덱스
    # 활성화된 노드 인덱스를 기준으로 탐색을 하면서 양의수+1 >= 늑대수 인 노드만
    # 탐색이 가능하다.  탐색한 노드는 방문 처리 한다.

    # 이진 트리 구조
    tree = defaultdict(list)
    for [parent, child] in edges:
        tree[parent].append(child)

    
    # (현재 위치, 양의 수, 늑대의 수, 방문 예정 노드 집합)
    queue = deque()
    queue.append((0, 1, 0, set()))

    # 최대 양 탐색 횟수
    max_sheeps = 0

    while queue:

        # 현재 노드 가져오기
        current, sheeps, wolfs, reachable = queue.popleft()

        # 최대 양 갱신
        max_sheeps = max(max_sheeps, sheeps)

        # 현재 노드에서 인접 노드를 확인 하여 방문 예정 노드로 추가
        reachable.update(tree[current])

        for next_node in reachable:
            # 늑대인 경우 양이 늑대보다 많아야 됨
            if info[next_node]:
                if not (sheeps > wolfs+1):
                    continue

                # 방문 예정 노드들 중 다음 노드만 제외
                queue.append((next_node, sheeps, wolfs+1, reachable-{next_node}))
            # 양인 경우
            else:
                queue.append((next_node, sheeps+1, wolfs, reachable-{next_node}))

    return max_sheeps
    
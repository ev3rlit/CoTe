def union_set(x, y, parents, rank_data):
    """
    두 집합을 합치는 함수 (Union 연산)
    rank 기반 최적화를 사용하여 트리의 높이를 최소화합니다.
    """
    root1 = find(x, parents)
    root2 = find(y, parents)

    if root1 != root2:
        # rank가 더 높은 쪽 밑으로 낮은 쪽을 붙임 (트리 깊이 최소화)
        if rank_data[root1] < rank_data[root2]:
            parents[root1] = root2
        elif rank_data[root1] > rank_data[root2]:
            parents[root2] = root1
        else:
            # rank가 같으면 한쪽을 다른 쪽에 붙이고 rank를 1 증가시킴
            parents[root2] = root1
            rank_data[root1] += 1

def find(x, parents):
    """
    특정 원소가 속한 집합의 대표(루트 노드)를 찾는 함수 (Find 연산)
    경로 압축(Path Compression)을 사용하여 탐색 효율을 높입니다.
    """
    if parents[x] != x:
        # 재귀적으로 루트를 찾으면서, 경로상의 모든 노드가 루트를 직접 가리키도록 갱신
        parents[x] = find(parents[x], parents)
    return parents[x]

def solution(k, operations):
    """
    k: 노드의 개수 (0 ~ k-1)
    operations: 수행할 연산 리스트 [['u', 0, 1], ['f', 0, 1], ...]
    """
    # 초기화: 각 노드는 자기 자신을 부모로 가짐 (서로 다른 k개의 집합)
    parents = list(range(k))
    # rank_data: 각 트리의 깊이(랭크)를 저장하는 배열, 초기값은 모두 0
    rank_data = [0] * k

    results = []

    for (cmd, x, y) in operations:
        if cmd == 'u': # Union 연산: x와 y가 속한 집합을 합침
            x = int(x)
            y = int(y)
            union_set(x, y, parents, rank_data)

        elif cmd == 'f': # Find 연산: x와 y가 같은 집합에 속하는지 확인
            x = int(x)
            y = int(y)
            # 두 노드의 루트가 같으면 같은 집합임
            results.append(find(x, parents) == find(y, parents))

    return results
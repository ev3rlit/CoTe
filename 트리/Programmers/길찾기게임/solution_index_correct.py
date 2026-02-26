# 올바른 인덱스 기반 분할 정복
# 핵심: 각 재귀 호출마다 해당 범위 내에서 y 최댓값을 루트로

def solution_index(nodeinfo):
    # (x, y, 노드번호) 형태로 변환
    nodes = [(x, y, i+1) for i, (x, y) in enumerate(nodeinfo)]

    preorder = []
    postorder = []

    def divide_and_traverse(node_indices):
        """
        노드 인덱스 리스트를 받아서 처리
        여전히 리스트를 전달하지만, 원본 nodes 배열의 인덱스만 전달
        """
        if not node_indices:
            return

        # 현재 범위에서 y가 가장 큰 노드를 루트로 선택
        root_idx = max(node_indices, key=lambda i: (nodes[i][1], -nodes[i][0]))
        root_x, root_y, root_num = nodes[root_idx]

        # 전위 순회: 루트 먼저
        preorder.append(root_num)

        # 루트를 제외한 나머지를 x 좌표로 분할
        left_indices = [i for i in node_indices if i != root_idx and nodes[i][0] < root_x]
        right_indices = [i for i in node_indices if i != root_idx and nodes[i][0] > root_x]

        # 재귀
        divide_and_traverse(left_indices)
        divide_and_traverse(right_indices)

        # 후위 순회: 루트 나중
        postorder.append(root_num)

    # 모든 노드의 인덱스로 시작
    divide_and_traverse(list(range(len(nodes))))

    return [preorder, postorder]

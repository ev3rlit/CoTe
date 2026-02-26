# 포인터 없이 재귀 분할로 풀이

def solution_alter(nodeinfo):
    # (x, y, 노드번호) 형태로 변환
    nodes = [(x, y, i+1) for i, (x, y) in enumerate(nodeinfo)]

    # y 내림차순, x 오름차순 정렬
    nodes.sort(key=lambda node: (-node[1], node[0]))

    preorder = []
    postorder = []

    def divide_and_traverse(node_list):
        """
        정렬된 노드 리스트를 재귀적으로 분할하며 순회

        핵심 아이디어:
        1. 첫 번째 노드가 현재 서브트리의 루트 (y가 가장 큼)
        2. 루트의 x 좌표로 왼쪽/오른쪽 서브트리 분할
        3. 재귀적으로 각 서브트리 처리
        """
        if not node_list:
            return

        # 첫 번째 노드 = 루트 (y 좌표가 가장 높음)
        root = node_list[0]
        root_x, root_y, root_num = root

        # 전위 순회: 루트 먼저 방문
        preorder.append(root_num)

        # 루트의 x 좌표를 기준으로 왼쪽/오른쪽 분할
        left_nodes = [n for n in node_list[1:] if n[0] < root_x]
        right_nodes = [n for n in node_list[1:] if n[0] > root_x]

        # 왼쪽 서브트리 재귀
        divide_and_traverse(left_nodes)

        # 오른쪽 서브트리 재귀
        divide_and_traverse(right_nodes)

        # 후위 순회: 루트 나중에 방문
        postorder.append(root_num)

    divide_and_traverse(nodes)

    return [preorder, postorder]

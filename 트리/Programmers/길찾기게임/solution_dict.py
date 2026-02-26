# 딕셔너리로 트리 구성 (포인터 대신 ID 참조)

def solution(nodeinfo):
    # (x, y, 노드번호) 형태로 변환
    nodes = [(x, y, i+1) for i, (x, y) in enumerate(nodeinfo)]

    # y 내림차순, x 오름차순 정렬
    nodes.sort(key=lambda node: (-node[1], node[0]))

    # 트리를 딕셔너리로 표현 {노드번호: {'left': left_id, 'right': right_id}}
    tree = {num: {'left': None, 'right': None} for _, _, num in nodes}
    node_info = {num: (x, y) for x, y, num in nodes}  # 좌표 정보 저장

    # 트리 구성
    root_num = nodes[0][2]

    for i in range(1, len(nodes)):
        x, y, num = nodes[i]

        # 루트부터 시작하여 삽입 위치 찾기
        current = root_num
        while True:
            current_x, _ = node_info[current]

            if x < current_x:  # 왼쪽으로
                if tree[current]['left'] is None:
                    tree[current]['left'] = num
                    break
                current = tree[current]['left']
            else:  # 오른쪽으로
                if tree[current]['right'] is None:
                    tree[current]['right'] = num
                    break
                current = tree[current]['right']

    # 전위 순회
    def preorder(node_num):
        if node_num is None:
            return []

        result = [node_num]
        result.extend(preorder(tree[node_num]['left']))
        result.extend(preorder(tree[node_num]['right']))
        return result

    # 후위 순회
    def postorder(node_num):
        if node_num is None:
            return []

        result = []
        result.extend(postorder(tree[node_num]['left']))
        result.extend(postorder(tree[node_num]['right']))
        result.append(node_num)
        return result

    return [preorder(root_num), postorder(root_num)]

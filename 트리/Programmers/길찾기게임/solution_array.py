# 완전 이진 트리 배열 표현 시도
# 경고: 메모리 비효율적!

def solution(nodeinfo):
    if not nodeinfo:
        return [[], []]

    # (x, y, 노드번호) 형태로 변환
    nodes = [(x, y, i+1) for i, (x, y) in enumerate(nodeinfo)]

    # y 내림차순, x 오름차순 정렬
    nodes.sort(key=lambda node: (-node[1], node[0]))

    # 최대 깊이 추정 (최악: N)
    # 안전하게 충분히 큰 크기 할당
    max_size = min(2 ** 15 - 1, len(nodes) * 100)  # 메모리 제한
    tree = [None] * max_size  # None = 빈 슬롯

    def insert(number, x, y):
        """배열 기반 이진 트리 삽입"""
        idx = 0  # 루트부터 시작

        while True:
            if tree[idx] is None:
                # 빈 슬롯 발견 → 삽입
                tree[idx] = (number, x, y)
                return

            # 현재 노드의 x 좌표
            _, current_x, _ = tree[idx]

            if x < current_x:
                # 왼쪽으로
                idx = 2 * idx + 1
            else:
                # 오른쪽으로
                idx = 2 * idx + 2

            # 배열 범위 초과 체크
            if idx >= max_size:
                raise MemoryError(f"트리가 너무 깊습니다! (idx={idx})")

    # 트리 구성
    for x, y, number in nodes:
        insert(number, x, y)

    # 전위 순회
    def preorder(idx=0):
        if idx >= max_size or tree[idx] is None:
            return []

        number, x, y = tree[idx]
        result = [number]
        result.extend(preorder(2 * idx + 1))  # 왼쪽
        result.extend(preorder(2 * idx + 2))  # 오른쪽
        return result

    # 후위 순회
    def postorder(idx=0):
        if idx >= max_size or tree[idx] is None:
            return []

        number, x, y = tree[idx]
        result = []
        result.extend(postorder(2 * idx + 1))  # 왼쪽
        result.extend(postorder(2 * idx + 2))  # 오른쪽
        result.append(number)
        return result

    return [preorder(), postorder()]

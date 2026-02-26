"""
배열 기반 완전 이진 트리의 반복적(Iterative) 순회 구현

재귀 대신 스택을 사용하여 트리를 순회합니다.
각 순회 방식마다 스택 사용 패턴이 다릅니다.
"""


def iterative_preorder(nodes):
    """
    전위 순회 (반복문)

    패턴: 루트 → 왼쪽 → 오른쪽
    스택 LIFO 특성 활용: 오른쪽 먼저 push

    시간: O(N), 공간: O(H) H는 트리 높이
    """
    if not nodes:
        return ""

    result = []
    stack = [0]  # 루트 인덱스부터 시작

    while stack:
        idx = stack.pop()

        # 범위 체크
        if idx >= len(nodes):
            continue

        # 1. 현재 노드 처리 (전위 = 루트 먼저)
        result.append(str(nodes[idx]))

        # 2. 오른쪽 자식 push (나중에 방문)
        right = 2 * idx + 2
        if right < len(nodes):
            stack.append(right)

        # 3. 왼쪽 자식 push (먼저 방문) - 스택 LIFO
        left = 2 * idx + 1
        if left < len(nodes):
            stack.append(left)

    return " ".join(result)


def iterative_inorder(nodes):
    """
    중위 순회 (반복문)

    패턴: 왼쪽 → 루트 → 오른쪽
    전략: 왼쪽 끝까지 내려가며 push → pop하며 처리 → 오른쪽으로

    시간: O(N), 공간: O(H)
    """
    if not nodes:
        return ""

    result = []
    stack = []
    current = 0  # 현재 인덱스

    while stack or current < len(nodes):
        # 1. 왼쪽 끝까지 계속 push
        while current < len(nodes):
            stack.append(current)
            current = 2 * current + 1  # 왼쪽 자식

        # 2. 스택에서 pop (왼쪽 끝 또는 부모)
        current = stack.pop()

        # 3. 현재 노드 처리 (중위 = 왼쪽 다음에 루트)
        result.append(str(nodes[current]))

        # 4. 오른쪽 서브트리로 이동
        current = 2 * current + 2  # 오른쪽 자식

    return " ".join(result)


def iterative_postorder(nodes):
    """
    후위 순회 (반복문) - 두 스택 방식

    패턴: 왼쪽 → 오른쪽 → 루트
    전략:
      - stack1: 전위 순회의 반대 (루트 → 오른쪽 → 왼쪽)
      - stack2: stack1의 결과를 역순으로 저장

    시간: O(N), 공간: O(N)
    """
    if not nodes:
        return ""

    stack1 = [0]  # 탐색용 스택
    stack2 = []   # 결과 역순 저장용 스택

    # Step 1: 전위 순회의 반대 (루트 → 오른쪽 → 왼쪽)
    while stack1:
        idx = stack1.pop()

        if idx >= len(nodes):
            continue

        # stack2에 push (나중에 역순으로 pop)
        stack2.append(idx)

        # 왼쪽 먼저 push (나중에 방문)
        left = 2 * idx + 1
        if left < len(nodes):
            stack1.append(left)

        # 오른쪽 나중에 push (먼저 방문)
        right = 2 * idx + 2
        if right < len(nodes):
            stack1.append(right)

    # Step 2: stack2를 pop하면 후위 순회 순서
    result = []
    while stack2:
        idx = stack2.pop()
        result.append(str(nodes[idx]))

    return " ".join(result)


def iterative_postorder_single_stack(nodes):
    """
    후위 순회 (반복문) - 단일 스택 + 방문 플래그 방식

    더 복잡하지만 공간 효율적 O(H)
    각 노드를 (인덱스, 방문여부) 튜플로 저장
    """
    if not nodes:
        return ""

    result = []
    stack = [(0, False)]  # (인덱스, 방문했는지)

    while stack:
        idx, visited = stack.pop()

        if idx >= len(nodes):
            continue

        if visited:
            # 이미 자식들을 처리했으면 현재 노드 처리
            result.append(str(nodes[idx]))
        else:
            # 아직 자식 미방문: 역순으로 push
            # 후위는 왼쪽 → 오른쪽 → 루트
            # 스택은 LIFO이므로 루트 → 오른쪽 → 왼쪽 순으로 push

            stack.append((idx, True))  # 루트 (나중에 처리)

            right = 2 * idx + 2
            if right < len(nodes):
                stack.append((right, False))  # 오른쪽

            left = 2 * idx + 1
            if left < len(nodes):
                stack.append((left, False))  # 왼쪽

    return " ".join(result)


# ============================================================
# 테스트 코드
# ============================================================

if __name__ == "__main__":
    # 재귀 버전 import
    import sys
    from pathlib import Path
    sys.path.insert(0, str(Path(__file__).parent))

    from solution import preorder, inorder, postorder

    test_cases = [
        [1, 2, 3, 4, 5, 6, 7],
        [3, 2, 1],
    ]

    for i, tree in enumerate(test_cases, 1):
        print(f"\n{'='*60}")
        print(f"테스트 케이스 {i}: {tree}")
        print(f"{'='*60}")

        # 전위 순회
        print("\n[전위 순회]")
        print(f"재귀:   {preorder(tree)}")
        print(f"반복문: {iterative_preorder(tree)}")
        assert preorder(tree) == iterative_preorder(tree), "❌ 전위 순회 불일치"
        print("✅ 일치")

        # 중위 순회
        print("\n[중위 순회]")
        print(f"재귀:   {inorder(tree)}")
        print(f"반복문: {iterative_inorder(tree)}")
        assert inorder(tree) == iterative_inorder(tree), "❌ 중위 순회 불일치"
        print("✅ 일치")

        # 후위 순회
        print("\n[후위 순회]")
        print(f"재귀:   {postorder(tree)}")
        print(f"반복문 (두 스택):   {iterative_postorder(tree)}")
        print(f"반복문 (단일 스택): {iterative_postorder_single_stack(tree)}")
        assert postorder(tree) == iterative_postorder(tree), "❌ 후위 순회 불일치 (두 스택)"
        assert postorder(tree) == iterative_postorder_single_stack(tree), "❌ 후위 순회 불일치 (단일 스택)"
        print("✅ 일치")

    print(f"\n{'='*60}")
    print("✅ 모든 테스트 통과!")
    print(f"{'='*60}")

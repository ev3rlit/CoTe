def preorder(nodes):

    result = []

    def inner(idx):
        if idx >= len(nodes):
            return 

        result.append(nodes[idx])
        inner(idx*2 + 1)
        inner(idx*2 + 2)

    inner(0)
    return " ".join(map(str,result))

def inorder(nodes):

    result = []

    def inner(idx):
        if idx >= len(nodes):
            return 

        inner(idx*2 + 1)
        result.append(nodes[idx])
        inner(idx*2 + 2)

    inner(0)
    return " ".join(map(str,result))
def postorder(nodes):

    result = []

    def inner(idx):
        if idx >= len(nodes):
            return 

        inner(idx*2 + 1)
        inner(idx*2 + 2)
        result.append(nodes[idx])

    inner(0)
    return " ".join(map(str,result))


def traverse(nodes, order):
    result = []

    def inner(idx):
        if idx >= len(nodes):
            return 

        if order == 'pre':
            result.append(nodes[idx])
        inner(idx*2 + 1)
        if order == 'in':
            result.append(nodes[idx])
        inner(idx*2 + 2)
        if order == 'post':
            result.append(nodes[idx])

    inner(0)
    return " ".join(map(str,result))

def iterate_preorder(nodes):
    result = []
    stack = [0]

    while stack:
        idx = stack.pop()
        if idx >= len(nodes):
            continue

        result.append(nodes[idx])
        # 오른쪽 자식 먼저 추가해야 왼쪽 자식이 먼저 처리됨
        stack.append(idx*2 + 2)
        stack.append(idx*2 + 1)
    
    return " ".join(map(str,result))

def solution(nodes):
    # 트리의 전위 순회, 중위 순회, 후위 순회 출력해보기
    # 배열의 입력을 보아하니 완전 이진 트리 형태를 구성하고 있어서 큰 문제는 없어보임

    # 배열로 구현된 완전 이진 트리에서  순회 구현하는 문제
    return [
        traverse(nodes, 'pre'),
        traverse(nodes, 'in'),
        traverse(nodes, 'post')
    ]
    
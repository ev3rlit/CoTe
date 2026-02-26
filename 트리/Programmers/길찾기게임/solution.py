# 레벨 순회를 가지고  preorder와 postorder하기?
# 음?? 이거 배열 데이터 가지고 순회하는거랑 똑같지 않나?
# 생각해보니 이거는 완전 이진트리를 배열로 한것이 아니네

from dataclasses import dataclass
import sys

sys.setrecursionlimit(10**6)

@dataclass
class Node():
    number : int = 0
    x : int = 0
    y : int = 0
    left = None
    right = None

class BinaryTree():

    def __init__(self) -> None:
        self.root = None

    def insert(self, number, x, y):
        # root가 없으면 root 노드 지정

        node = Node(number,x,y)

        if self.root is None:
            self.root = node
            return
        
        # root 노드를 기준으로  현재 노드와 추가하려는 노드를 비교
        # y 보다 작으면 ok
        # 왼쪽으로 갈지 오른쪽으로 갈지 결정

        parent = self.root
        while True:
            if node.x < parent.x:
                if parent.left is not None:
                    parent = parent.left
                    continue

                parent.left = node
                break
            else:
                if parent.right is not None:
                    parent = parent.right
                    continue

                parent.right = node
                break

    def pre_order(self):

        result = []

        def travel(node):
            if node is None:
                return
            
            result.append(node.number)
            travel(node.left)
            travel(node.right)

        travel(self.root)
        return result

    def post_order(self):

        result = []

        def travel(node):
            if node is None:
                return
            
            travel(node.left)
            travel(node.right)        
            result.append(node.number)
        
        travel(self.root)
        return result


def solution(nodeinfo):
    # 좌표를 가지고 노드를 만든다음 트리를 구성하면됨
    # (x,y) 두가지 가중치를 가지고 트리를 구성하는 문제네.
    # 기존에는 value 하나만 가지고 했다면
    # (x가 작을수록 왼쪽, y가 작을수록 왼쪽)

    # 이진 트리를 구성하는 문제임
    nodes = [(x,y,i+1) for i, (x, y) in enumerate(nodeinfo)]

    # 노드를 가지고 트리를 구성하기 위해서  분산된 좌표를  상하식으로 정렬
    # y 좌표 내림차순,  x 좌표 오름차순
    nodes.sort(key=lambda node : (-node[1], node[0]))

    # 이진 트리를 만들어야지
    tree = BinaryTree()
    for (x,y,number) in nodes:
        tree.insert(number, x, y)
    
    # 전위 순회
    # 후위 순회

    return [
        tree.pre_order(),
        tree.post_order()
    ]
    
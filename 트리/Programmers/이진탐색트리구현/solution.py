from dataclasses import dataclass
from typing import Protocol, TypeVar, Any, Generic, Iterable

class Comparable(Protocol):
    """비교 연산자를 지원하는 타입"""
    def __lt__(self, other: Any, /) -> bool: ...
    def __gt__(self, other: Any, /) -> bool: ...
    def __eq__(self, other: Any, /) -> bool: ...

T = TypeVar('T', bound=Comparable)

@dataclass
class Node(Generic[T]):
    value: T
    left: 'Node[T] | None' = None
    right: 'Node[T] | None' = None

class BinarySearchTree(Generic[T]):
    root: Node[T] | None

    def __init__(self, iterate: Iterable[T] | None = None):
        """
        이진 탐색 트리 생성

        Args:
            iterate: 반복 가능한 객체 (비교 가능한 요소들)
        """
        self.root = None
        if iterate:
            for value in iterate:
                self.insert(value)

    def insert(self, value: T) -> None:
        # 루트 노드가 없으면 새로운 노드를 루트 노드로 추가
        if self.root is None:
            self.root = Node(value=value)
        else:
            # 적합한 위치의 노드 위치를 찾아서 삽입
            cur = self.root
            while True:
                if value < cur.value:
                    if cur.left:
                        cur = cur.left
                    else:
                        cur.left = Node(value=value)
                        break
                else:
                    if cur.right:
                        cur = cur.right
                    else:
                        cur.right = Node(value=value)
                        break

    def exist(self, value: T) -> bool:
        cur = self.root
        while cur:
            if value == cur.value:
                return True
            elif value < cur.value:
                cur = cur.left
            else:
                cur = cur.right

        return False

def solution(lst, search_lst):

    bst = BinarySearchTree(lst)
    answer = []
    for num in search_lst:
        answer.append(True if bst.exist(num) else False)

    return answer
    
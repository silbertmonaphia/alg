from data_structure import Node

class SolutionIterative:
    def reverseList(self, head: Node) -> Node:
        cur, prev = head, None
        while cur:
            cur.next, prev, cur = prev, cur, cur.next
        return prev

class SolutionRecursive:
    def reverseList(self, head: Node, prev=None) -> Node:
        if not head:
            return prev
        cur, head.next = head.next, prev
        return self.reverseList(cur, head)

if __name__ == '__main__':
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n1.next = n2
    n2.next = n3

    from copy import deepcopy
    head = deepcopy(n1)
    new_head = SolutionIterative().reverseList(head)
    new_head.traverse()

    head = deepcopy(n1)
    new_head = SolutionRecursive().reverseList(n1)
    new_head.traverse()
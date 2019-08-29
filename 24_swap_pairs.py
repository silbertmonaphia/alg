from data_struture import Node

class SolutionIterative:
    def swapPairs(self, head: Node) -> Node:
        pre, pre.next = self, head
        while pre.next and pre.next.next:
            a = pre.next
            b = a.next
            pre.next, b.next, a.next = b, a, b.next
            pre = a
        return self.next

if __name__ == '__main__':
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    n5 = Node(5)
    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5

    from copy import deepcopy
    head = deepcopy(n1)
    new_head = SolutionIterative().swapPairs(head)
    new_head.traverse()

    # head = deepcopy(n1)
    # new_head = SolutionRecursive().reverseList(n1)
    # new_head.traverse()
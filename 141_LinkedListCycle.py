from data_structure import Node

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        visited = set()
        while head:
            if head in visited:
                return True
            else:
                visited.add(head)
            head = head.next
        return False

    def hasCycleChasing(self,head):
        """
        :type head: ListNode
        :rtype: bool
        """
        fast = slow = head
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                return True
        return False

if __name__ == '__main__':
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n1.next = n2
    n2.next = n3

    c1 = Node(1)
    c2 = Node(2)
    c3 = Node(3)
    c4 = Node(4)
    c1.next = c2
    c2.next = c3
    c3.next = c4
    c4.next = c2

    has_cycle = Solution().hasCycle(n1)
    assert(has_cycle is False)

    has_cycle = Solution().hasCycleChasing(c1)
    assert(has_cycle is True)
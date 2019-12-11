from data_structure import Stack

class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._stack_in = Stack()
        self._stack_out = Stack()
        self._front = None

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        if self._stack_in.is_empty():
            self._front = x
        self._stack_in.push(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if self.empty():
            return None
        if self._stack_out.is_empty():
            size = self._stack_in.size()
            for i in range(size):
                self._stack_out.push(self._stack_in.pop())
        return self._stack_out.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """
        if self.empty():
            return None
        if self._stack_out.is_empty():
            return self._front
        else:
            return self._stack_out.peek()

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return self._stack_in.is_empty() and self._stack_out.is_empty()
        
queue = MyQueue()
queue.push(1)
assert(queue.pop() == 1)
assert(queue.peek() is None)
queue.push(1)
queue.push(2)
assert(queue.peek() == 1)
assert(queue.pop() == 1)
assert(queue.empty() is False)

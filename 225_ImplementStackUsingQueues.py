from data_structure import Queue

class MyStack(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.input_queue = Queue()
        self.output_queue = Queue()

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: None
        """
        self.input_queue.push(x)

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        size = self.input_queue.size()
        if size == 0:
            return None
        for i in range(size - 1):
            self.output_queue.push((self.input_queue.pop()))
        item = self.input_queue.pop()
        self.input_queue,self.output_queue = self.output_queue,self.input_queue

        return item

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        size = self.input_queue.size()
        if size == 0:
            return None
        for i in range(size - 1):
            self.output_queue.push((self.input_queue.pop()))
        item = self.input_queue.peek()
        self.output_queue.push((self.input_queue.pop()))
        self.input_queue,self.output_queue = self.output_queue,self.input_queue
        return item

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return self.input_queue.is_empty()


# Your MyStack object will be instantiated and called as such:
obj = MyStack()
obj.push('a')
obj.push('b')
obj.push('c')

assert(obj.top() == 'c')
assert(obj.pop() == 'c')
assert(obj.pop() == 'b')
assert(obj.top() == 'a')
assert(obj.empty() is False)
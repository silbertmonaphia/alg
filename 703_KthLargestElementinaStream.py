from data_struture import minHeap

class KthLargest:
    def __init__(self, k, arr):
        self.minheap = minHeap()
        self.minheap.heapify(arr)
        self.k = k

    def add(self, x):
        if self.minheap.size() < self.k:
            self.minheap.push(x)
        elif x > self.minheap.peek():
            self.minheap.pop()
            self.minheap.push(x)

    def sort(self):
        lst = []
        while self.minheap.size:
            lst.append(self.minheap.pop())
        return lst

pq = KthLargest(k=3, arr=[5,4,8])
pq.add(3)
pq.add(5)
pq.add(10)
pq.add(9)
pq.add(4)
assert(pq.sort() == [8,9,10])
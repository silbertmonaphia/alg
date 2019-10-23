class minHeap:
    def __init__(self):
        self.heap = []

    def heapify(self, arr):
        """Transform list into a heap, in-place, in O(len(x)) time."""
        n = len(arr)
        # Transform bottom-up.  The largest index there's any point to looking at
        # is the largest with a child index in-range, so must have 2*i + 1 < n,
        # or i < (n-1)/2.  If n is even = 2*j, this is (2*j-1)/2 = j-1/2 so
        # j-1 is the largest, which is n//2 - 1.  If n is odd = 2*j+1, this is
        # (2*j+1-1)/2 = j so j-1 is the largest, and that's again n//2-1.
        self.heap = arr
        for i in reversed(range(n//2)):
            self._siftup(i)

    def size(self):
        return len(self.heap)

    def peek(self):
        if not self.heap:
            return None
        return self.heap[0]

    def push(self, item):
        """Push item onto heap, maintaining the heap invariant."""
        self.heap.append(item)
        self._siftdown(0, len(self.heap)-1)

    def pop(self):
        """Pop the smallest item off the heap, maintaining the heap invariant."""
        if not self.heap:
            return None
        lastelt = self.heap.pop()    # raises appropriate IndexError if heap is empty
        if self.heap:
            returnitem = self.heap[0]
            self.heap[0] = lastelt
            self._siftup(0)
            return returnitem
        return lastelt

    def _siftup(self, pos):
        endpos = len(self.heap)
        startpos = pos
        newitem = self.heap[pos]
        # Bubble up the smaller child until hitting a leaf.
        leftpos = 2 * pos + 1    # leftmost child position
        while leftpos < endpos:
            # Set leftpos to index of smaller child.
            rightpos = leftpos + 1
            if rightpos < endpos and not self.heap[leftpos] < self.heap[rightpos]:
                leftpos = rightpos
            # Move the smaller child up.
            self.heap[pos] = self.heap[leftpos]
            pos = leftpos
            leftpos = 2 * pos + 1
        # The leaf at pos is empty now.  Put newitem there, and bubble it up
        # to its final resting place (by sifting its parents down).
        self.heap[pos] = newitem
        self._siftdown(startpos, pos)

    def _siftdown(self, startpos, pos):
        newitem = self.heap[pos]
        # Follow the path to the root, moving parents down until finding a place
        # newitem fits.
        while pos > startpos:
            parentpos = (pos - 1) >> 1
            parent = self.heap[parentpos]
            if newitem < parent:
                self.heap[pos] = parent
                pos = parentpos
                continue
            break
        self.heap[pos] = newitem
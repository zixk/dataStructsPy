class MinHeap:
    def __init__(self):
        self.size: int = 0
        self.heap: [int] = []

    def peek(self) -> int:
        if(self.size == 0):
            raise ValueError("Heap is empty")
        return self.heap[0]
    
    def poll(self) -> int:
        if(self.size == 0):
            raise ValueError("Heap is empty")
        first_item = self.heap[0]
        self.heap[0] = self.heap[self.size-1]
        del self.heap[self.size-1]
        self.size -= 1
        self.heapifyDown()
        return first_item

    def add(self, item):
        self.heap.insert(self.size, item)
        self.size += 1
        self.heapifyUp()

    def heapifyDown(self):
        index = 0
        while(self.hasLeftChildIndex(index)):
            smallerChildIndex = self.getLeftChildIndex(index)
            if(self.hasRightChildIndex(index) and self.rightChild(index) < self.leftChild(index)):
                smallerChildIndex = self.getRightChildIndex(index)
            if(self.heap[index] < self.heap[smallerChildIndex]):
                break
            else:
                self.swap(index, smallerChildIndex)
                index = smallerChildIndex

    def heapifyUp(self):
        index = self.size-1
        while(self.hasParentIndex and self.parent(index) > self.heap[index]):
            self.swap(self.getParentIndex(index), index)
            index = self.getParentIndex(index)

    def getLeftChildIndex(self, index) -> int:
        return int(index*2+1)

    def getRightChildIndex(self, index):
        return int(index*2+2)
    
    def getParentIndex(self, index) -> int:
        return int((index-1)/2)


    def hasLeftChildIndex(self, index):
        return self.getLeftChildIndex(index) < self.size

    def hasRightChildIndex(self, index):
        return self.getRightChildIndex(index) < self.size

    def hasParentIndex(self, index):
        return self.getParentIndex(index) >= 0


    def leftChild(self, index):
        return self.heap[self.getLeftChildIndex(index)]

    def rightChild(self, index):
        return self.heap[self.getRightChildIndex(index)]

    def parent(self, index):
        return self.heap[self.getParentIndex(index)]

    def swap(self, indexOne, indexTwo):
        temp = self.heap[indexOne]
        self.heap[indexOne] = self.heap[indexTwo]
        self.heap[indexTwo] = temp
    def toString(self):
        print(self.heap)

if __name__ == "__main__":
    r = MinHeap()
    r.add(10)
    r.toString()
    r.add(15)
    r.toString()
    r.add(20)
    r.toString()
    r.add(17)
    r.toString()
    r.add(25)
    r.toString()
    print(r.getParentIndex(4))
    print(r.peek())
    r.poll()
    r.toString()
    
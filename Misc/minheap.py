class MinHeap():
    def __init__(self, rootValue):
        self.values = [rootValue]

    def getLeftIndex(self, index): return 2 * index + 1
    def getRightIndex(self, index): return 2 * index + 2
    def getParentIndex(self, index): return (index - 1)/2
    def hasLeftChild(self, index): return (self.getLeftIndex(index) + 1) <= len(self.values)
    def hasRightChild(self, index): return (self.getRightIndex(index) + 1) <= len(self.values)
    def hasParent(self, index): return self.getParentIndex(index) >= 0
    def leftChild(self, index): return self.values[self.getLeftIndex(index)]
    def rightChild(self, index): return self.values[self.getRightIndex(index)]
    def parent(self, index): return self.values[self.getParentIndex(index)]

    def swap(self, index1, index2):
        temp = self.values[index1]
        self.values[index1] = self.values[index2]
        self.values[index2] = temp
    
    def heapifyUp(self):
        if len(self.values) <= 1: raise Exception("Please call heapifyUp when self.values has more than 1 item")

        index = len(self.values) - 1
        while self.hasParent(index) and self.parent(index) > self.values[int(index)]:
            self.swap(index, self.getParentIndex(index))
            index = self.getParentIndex(index)

    def heapifyDown(self):
        if len(self.values) <= 1: raise Exception("Please call heapifyDown when self.values has more than 1 item")

        index = 0
        while (self.hasLeftChild(index)):
            smallerChildIndex = self.getLeftIndex(index)
            if self.hasRightChild(index) and (self.rightChild(index) < self.leftChild(index)):
                smallerChildIndex = self.getRightIndex(index)

            if self.values[smallerChildIndex] < self.values[index]:
                self.swap(smallerChildIndex, index)
                index = smallerChildIndex
            else:
                break

    def peek(self):
        if len(self.values) == 0: raise Exception("Heap is empty")
        return self.values[0]
    
    def poll(self):
        item = self.values[0]
        self.values[0] = self.values[-1]
        del self.values[-1]
        self.heapifyDown()
        return item

    def add(self, value):
        self.values.append(value)
        self.heapifyUp()

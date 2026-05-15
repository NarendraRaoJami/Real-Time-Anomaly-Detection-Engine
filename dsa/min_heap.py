class MinHeap:
    def __init__(self):
        self.heap = []

    # helper functions

    def parent(self, i):
        return (i-1)//2
    
    def left(self, i):
        return 2*i + 1
    
    def right(self, i):
        return 2*i + 2
    
    #insert function

    def insert(self, value):
        self.heap.append(value)
        self.heapify_up(len(self.heap)-1)

    def heapify_up(self, i):
        while i > 0:
            p = self.parent(i)
            if self.heap[p] > self.heap[i]:
                self.heap[p],self.heap[i] = self.heap[i],self.heap[p]
                i = p
            else:
                break
    
    def extract_min(self):
        if not self.heap:
            return None
        
        if len(self.heap) == 1:
            return self.heap.pop()
        
        minimum = self.heap[0]

        # move last element to root
        self.heap[0] = self.heap.pop()

        # restore heap property
        self.heapify_down(0)

        return minimum
    
    def heapify_down(self, i):
        size = len(self.heap)

        while True:
            smallest = i
            left = self.left(i)
            right = self.right(i)

            if left < size and self.heap[left] < self.heap[smallest]:
                smallest = left
            
            if right < size and self.heap[right] < self.heap[smallest]:
                smallest = right

            if smallest != i:
                self.heap[i],self.heap[smallest] = (
                    self.heap[smallest],
                    self.heap[i],
                )
                i = smallest
            else:
                break

    # peek
    def peek(self):
        if not self.heap:
            return None
        
        return self.heap[0]
    
    # utility
    def display(self):
        print(self.heap)

    def __len__(self):
        return len(self.heap)

# ---------------- TEST ----------------
if __name__ == "__main__":
    mh = MinHeap()

    values = [10, 4, 15, 1, 7, 20]

    for v in values:
        mh.insert(v)
        print("Inserted:", v)
        mh.display()

    print("\nExtracting minimums:")

    while mh.heap:
        print("Min:", mh.extract_min())
        mh.display()

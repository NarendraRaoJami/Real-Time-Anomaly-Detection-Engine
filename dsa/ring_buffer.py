class RingBuffer:
    def __init__(self, size):
        self.size = size
        self.buffer = [None]*size
        self.index = 0
        self.count = 0

    def append(self, value):
        self.buffer[self.index] = value
        self.index = (self.index + 1) % self.size
        if self.count < self.size:
            self.count += 1

    def get_data(self):
        index_req = self.index
        if self.count < self.size:
            return self.buffer[:self.count]
        return self.buffer[index_req:] + self.buffer[:index_req]
    
if __name__ == "__main__":
    rb = RingBuffer(5)

    for i in range(1,8):
        rb.append(i)
        print("Buffer:",rb.buffer)
        print("Index:",rb.index)
        print("Count:",rb.count)
        print()

    print(rb.get_data())
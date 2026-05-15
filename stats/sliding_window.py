import math
from dsa.ring_buffer import RingBuffer

class SlidingWindowStats:
    def __init__(self, window_size):
        self.window_size = window_size
        self.buffer = RingBuffer(window_size)

    # Add new value into sliding window

    def add(self, value):
        self.buffer.append(value)

    def get_data(self):
        return self.buffer.get_data()
    
    def mean(self):
        data = self.get_data()

        if not data:
            return 0
        
        return sum(data) / len(data)
    
    # variance
    def variance(self):
        data = self.get_data()

        if not data:
            return 0
        
        mu = self.mean()
        variance = sum((x-mu)**2 for x in data) / len(data)

        return variance
    
    def std_dev(self):
        return math.sqrt(self.variance())
    
# ---------------- TEST ----------------
if __name__ == "__main__":
    sw = SlidingWindowStats(5)

    values = [10, 12, 11, 13, 12]

    for v in values:
        sw.add(v)

    print("Data:", sw.get_data())
    print("Mean:", sw.mean())
    print("Variance:", sw.variance())
    print("Std Dev:", sw.std_dev())

    print("\nAdding anomaly: 100\n")

    sw.add(100)

    print("Data:", sw.get_data())
    print("Mean:", sw.mean())
    print("Variance:", sw.variance())
    print("Std Dev:", sw.std_dev())
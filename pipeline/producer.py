import threading
import random
import time

class DataProducer(threading.Thread):
    def __init__(self,queue):
        super().__init__(daemon=True)
        self.queue = queue
        self.running = True

    def run(self):
        while self.running:
            # Mostly normal values
            value = random.randint(10,15)
            # occasionally inject anomaly
            if random.random() < 0.1:
                value = random.randint(80,120)

            print(f"[producer] Generated: {value}")

            self.queue.put(value)
            time.sleep(1)

    def stop(self):
        self.running = False
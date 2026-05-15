import threading
from queue import Empty

class DetectorConsumer(threading.Thread):
    def __init__(self,queue,detector):
        super().__init__(daemon=True)
        self.queue = queue
        self.detector = detector
        self.running = True
    
    def run(self):
        while self.running:
            try:
                value = self.queue.get(timeout=1)
                print(f"[Consumer] Processing: {value}")
                self.detector.process(value)
                self.queue.task_done()
            except Empty:
                continue
            
    def stop(self):
        self.running = False
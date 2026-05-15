from dsa.min_heap import MinHeap
from database.db import DatabaseManager

class Alert_Manager:
    def __init__(self):
        self.heap_class = MinHeap()
        self.alert_history = []
        self.max_history = 200
        self.db = DatabaseManager()

    # Add new alert
    def add_alert(self, alert):
        self.heap_class.insert(alert)
        self.alert_history.append(alert)

        # keep memory bounded
        if len(self.alert_history) > self.max_history:
            self.alert_history.pop(0)
            
        # save to database
        self.db.insert_alert(alert)

    # Process highest priority alert
    def process_alert(self):
        if not self.heap_class.heap:
            print("No alerts")
            return
        
        alert = self.heap_class.extract_min()

        print("\n=== PROCESSING ALERT ===")
        print(alert)
        print("========================\n")
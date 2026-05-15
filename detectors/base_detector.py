from abc import ABC, abstractmethod
from stats.sliding_window import SlidingWindowStats
from alerts.alert import Alert

class AnomalyDetector(ABC):
    def __init__(self, window_size = 5, alert_manager=None):
        self.window_size = window_size
        self.stats = SlidingWindowStats(window_size)
        self.alert_manager = alert_manager

    def add(self, value):
        self.stats.add(value)

    def process(self, value):
        is_anomaly, score = self.is_anomaly(value)

        print(f"Value: {value}")

        if is_anomaly:
            alert = Alert(
                score=score,
                value=value,
                message=f"Detected by {self.__class__.__name__}"
            )
            print(f"ANOMALY  {alert.severity.name}  (score={score:.2f})")
            if self.alert_manager:
                self.alert_manager.add_alert(alert)
            
        else:
            print("NORMAL")

        print()
        self.add(value)

        return {
            "value": value,
            "anomaly": is_anomaly,
            "score": score
        }
    
    @abstractmethod
    def is_anomaly(self, value) -> tuple[bool, float]:
        pass
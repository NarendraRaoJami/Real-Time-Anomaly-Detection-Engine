from detectors.base_detector import AnomalyDetector
import statistics

class IQRDetector(AnomalyDetector):
    def __init__(self, window_size = 5,alert_manager=None):
        super().__init__(window_size,alert_manager)

    # compute quartiles
    def quartiles(self):
        data = sorted(self.stats.get_data())
        n = len(data)

        if n < self.window_size:
            return None, None
        
        mid = n//2

        # split into lower and upper halves
        lower_half = data[:mid]
        upper_half = data[mid+1:] if n%2 else data[mid:]

        q1 = statistics.median(lower_half)
        q3 = statistics.median(upper_half)

        return q1,q3
    
    # check anomaly
    def is_anomaly(self, value):
        q1,q3 = self.quartiles()

        # Warmup period
        if q1 is None or q3 is None:
            return False, 0.0
        
        iqr = q3 - q1

        lower_bound = q1 - 1.5*iqr
        upper_bound = q3 + 1.5*iqr

        if value < lower_bound:
            score = (lower_bound - value) / (iqr if iqr > 0 else 1)
            return True, score
        
        if value > upper_bound:
            score = (value - upper_bound) / (iqr if iqr > 0 else 1)
            return True, score
        
        return False, 0.0 # normal

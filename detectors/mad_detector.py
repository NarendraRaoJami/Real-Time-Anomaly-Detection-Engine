import statistics
from detectors.base_detector import AnomalyDetector

# MAD stands for Median Absolute Deviation
# You already know Z-Score: (value - mean)/std_dev

# The problem with z-score is that mean and std_dev are easily pulled by outliers
# If one extreme value sneaks into the window, the mean shifts and you start missing real anomalies

class MADDetector(AnomalyDetector):
    def __init__(self,window_size=5, threshold=3.5, alert_manager=None):
        super().__init__(window_size, alert_manager)
        self.threshold = threshold
        # threshold=3.5 is the recommended value for MAD
        # values with mad_score > 3.5 considered anomalies.

    def median(self, data):
        return statistics.median(data)
    
    def compute_mad(self, data):
        med = self.median(data)
        dist = [abs(x - med) for x in data]
        mad = statistics.median(dist)
        return mad
    
    def mad_score(self, value, data):
        med = self.median(data)
        mad = self.compute_mad(data)

        if mad == 0:
            if value != med:
                return 999.0
            return 0.0
        
        # 0.6745 is a consistent that makes MAD comparable to z-score
        score = 0.6745*abs(value - med)/mad

        return score
    
    def is_anomaly(self, value):
        data = self.stats.get_data()

        if len(data) < self.window_size:
            return False, 0.0
        
        score = self.mad_score(value, data)

        return score > self.threshold, score
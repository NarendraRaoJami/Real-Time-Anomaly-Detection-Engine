from detectors.base_detector import AnomalyDetector

class ZScoreDetector(AnomalyDetector):
    def __init__(self, window_size=5, threshold=3,alert_manager=None):
        super().__init__(window_size,alert_manager)
        self.threshold = threshold

    # Compute z-score
    def z_score(self, value):
        mean = self.stats.mean()
        std = self.stats.std_dev()

        if std == 0:
            return 0

        return (value - mean) / std

    # Check anomaly
    def is_anomaly(self, value):
        data = self.stats.get_data()

        # Warmup period
        if len(data) < self.window_size:
            return False, 0.0

        z = abs(self.z_score(value))

        return abs(z) > self.threshold, z # returns (is_anomaly, anomaly_score)
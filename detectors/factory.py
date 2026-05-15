from detectors.zscore_detector import ZScoreDetector
from detectors.iqr_detector import IQRDetector
from detectors.mad_detector import MADDetector

class DetectorFactory:
    @staticmethod
    def create_detector(detector_type, window_size = 5, threshold = 3,alert_manager=None):
        detector_type = detector_type.lower()

        if detector_type == "zscore":
            return ZScoreDetector(
                window_size=window_size,
                threshold=threshold,
                alert_manager=alert_manager
            )
        elif detector_type == "iqr":
            return IQRDetector(
                window_size=window_size,
                alert_manager=alert_manager
            )
        elif detector_type == "mad":
            mad_threshold = (threshold if threshold != 3 else 3.5)
            return MADDetector(
                window_size=window_size,
                threshold= mad_threshold,
                alert_manager=alert_manager
            )
        else:
            raise ValueError(f"Unknown detector type: {detector_type}")
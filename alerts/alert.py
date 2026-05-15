from datetime import datetime
from enum import Enum

class SeverityLevel(Enum):
    LOW = 1
    MEDIUM = 2
    HIGH = 3
    CRITICAL = 4

def get_severity_level(score : float) -> SeverityLevel:
    if score >= 10:
        return SeverityLevel.CRITICAL
    elif score >= 5:
        return SeverityLevel.HIGH
    elif score >= 2:
        return SeverityLevel.MEDIUM
    else:
        return SeverityLevel.LOW


class Alert:
    def __init__(self, score: float, value, message):
        self.score = score
        self.severity = get_severity_level(score)
        self.value = value
        self.message = message
        self.timestamp = datetime.now()

    def __lt__(self, other):
        return self.score < other.score
    
    def __repr__(self):
        return (
            f"[severity {self.severity.name}] "
            f"Value = {self.value} "
            f"score = {self.score:.2f} "
            f"Message={self.message} "
        )
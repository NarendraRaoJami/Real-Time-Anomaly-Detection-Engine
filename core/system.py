from alerts.alert_manager import Alert_Manager
from detectors.factory import DetectorFactory
from queue import Queue

from pipeline.producer import DataProducer
from pipeline.consumer import DetectorConsumer

data_queue = Queue()

alert_manager = Alert_Manager()

detector = DetectorFactory.create_detector(
    detector_type="mad",
    window_size=5,
    threshold=3.5,
    alert_manager=alert_manager
)

# shared threads
producer = DataProducer(data_queue)

consumer = DetectorConsumer(
    data_queue,
    detector
)
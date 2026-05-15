from queue import Queue
import time
from alerts.alert_manager import Alert_Manager

from detectors.factory import DetectorFactory
from pipeline.producer import DataProducer
from pipeline.consumer import DetectorConsumer

# data shared between producer and consumer

data_queue = Queue()
alert_manager = Alert_Manager()

# create detector dynamically

detector = DetectorFactory.create_detector(
    "zscore",
    window_size=5,
    threshold=2,
    alert_manager=alert_manager
)
# create threads
producer = DataProducer(data_queue)
consumer = DetectorConsumer(data_queue,detector)

# start threads
producer.start()
consumer.start()

try:
    while True:
        alert_manager.process_alert()
        time.sleep(1)
except KeyboardInterrupt:
    print("\nStopping pipeliine")

    producer.stop()
    consumer.stop()

    producer.join()
    consumer.join()
from fastapi import FastAPI
from core.system import detector,alert_manager,producer,consumer,data_queue
from pydantic import BaseModel

app = FastAPI()

class DataPoint(BaseModel):
    value : float

@app.on_event("startup")
def startup_event():
    producer.start()
    consumer.start()

    print("Pipeline Started")


@app.get("/")
def home():
    return {
        "message" : "Anomaly Detection Engine running"
    }

@app.get("/alerts")
def get_alerts():
    return [
        {
            "severity": alert.severity.name,
            "score": alert.score,
            "value": alert.value,
            "message": alert.message,
            "timestamp": str(alert.timestamp)
        }
        for alert in  alert_manager.alert_history
    ]

@app.get("/metrics")
def get_metrics():
    return {
        "detector": detector.__class__.__name__,
        "window_size": detector.window_size,
        "mean": detector.stats.mean(),
        "std_dev": detector.stats.std_dev(),
        "recent_data": detector.stats.get_data()
    }

@app.post("/ingest")
def ingest_data(data: DataPoint):
    data_queue.put(data.value)

    return {
        "status": "received",
        "value": data.value,
        "queue_size": data_queue.qsize()
    }

@app.get("/alerts/db")
def get_db_alerts():

    alerts = alert_manager.db.fetch_alerts()

    return [
        {
            "severity" : row[0],
            "score" : row[1],
            "value" : row[2],
            "message" : row[3],
            "timestamp" : row[4]
        }
        for row in alerts
    ]

@app.on_event("shutdown")
def shutdown_event():

    print("Stopping pipeline...")

    producer.stop()
    consumer.stop()

    producer.join(timeout=2)
    consumer.join(timeout=2)

    print("Pipeline stopped")

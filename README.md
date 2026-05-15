# Real-Time Anomaly Detection System

## Overview

A real-time anomaly detection engine built using Python, FastAPI, Streamlit, SQLite, threading, and statistical anomaly detection algorithms.

The system continuously generates or ingests streaming numerical data, processes it asynchronously using a producer-consumer pipeline, detects anomalies using multiple statistical methods, prioritizes alerts using a Min Heap, stores alerts in SQLite, and visualizes everything through a Streamlit dashboard.

---

# Features

* Real-time streaming data pipeline
* Producer-consumer multithreaded architecture
* Sliding window statistics
* Multiple anomaly detection algorithms
* Alert prioritization using Min Heap
* SQLite database persistence
* FastAPI REST APIs
* Streamlit live dashboard
* Modular and extensible project structure

---

# Technologies Used

| Technology | Purpose                         |
| ---------- | ------------------------------- |
| Python     | Core programming language       |
| FastAPI    | Backend API framework           |
| Streamlit  | Dashboard and visualization     |
| SQLite     | Database persistence            |
| Threading  | Concurrent processing           |
| Queue      | Producer-consumer communication |
| Pandas     | Data handling for dashboard     |

---

# Project Architecture

```text
Data Producer
      ↓
Queue (Shared Buffer)
      ↓
Consumer Thread
      ↓
Anomaly Detector
      ↓
Alert Manager
      ↓
SQLite Database
      ↓
FastAPI APIs
      ↓
Streamlit Dashboard
```

---

# Implemented Anomaly Detectors

## 1. Z-Score Detector

Uses mean and standard deviation.

Formula:

```text
z = (value - mean) / std_dev
```

Best for normally distributed data.

---

## 2. IQR Detector

Uses quartiles and interquartile range.

Formula:

```text
IQR = Q3 - Q1
```

Anomaly if value lies outside:

```text
Q1 - 1.5 * IQR
Q3 + 1.5 * IQR
```

More robust against outliers.

---

## 3. MAD Detector

Uses Median Absolute Deviation.

Very robust for noisy data and extreme outliers.

Formula:

```text
MAD Score = 0.6475 * |value - median| / MAD
```

---

# Project Structure

```text
real_time_anomaly_detection/
│
├── alerts/
│   ├── alert.py
│   └── alert_manager.py
│
├── api/
│   └── server.py
│
├── core/
│   └── system.py
│
├── dashboard/
│   └── app.py
│
├── database/
│   ├── db.py
│   └── data.db
│
├── detectors/
│   ├── base_detector.py
│   ├── zscore_detector.py
│   ├── iqr_detector.py
│   ├── mad_detector.py
│   └── factory.py
│
├── dsa/
│   ├── min_heap.py
│   └── ring_buffer.py
│
├── pipeline/
│   ├── producer.py
│   └── consumer.py
│
├── stats/
│   └── sliding_window.py
│
├── main.py
├── requirements.txt
└── README.md
```

---

# Threading Architecture

The project uses a producer-consumer architecture.

## Producer Thread

Generates streaming numerical data.

Responsibilities:

* simulate real-time data stream
* inject anomalies occasionally
* push values into shared queue

---

## Consumer Thread

Consumes values from queue and processes them.

Responsibilities:

* retrieve values from queue
* run anomaly detection
* generate alerts
* store alerts in database

---

## Queue

Acts as a thread-safe shared buffer between producer and consumer.

Benefits:

* decouples data generation from processing
* prevents race conditions
* supports asynchronous architecture

---

# FastAPI Endpoints

## Home

```http
GET /
```

Returns system status.

---

## Metrics

```http
GET /metrics
```

Returns:

* detector type
* mean
* standard deviation
* recent data

---

## Alerts (Memory)

```http
GET /alerts
```

Returns recent in-memory alerts.

---

## Alerts (Database)

```http
GET /alerts/db
```

Returns persistent alerts from SQLite database.

---

## Ingest Data

```http
POST /ingest
```

Example:

```json
{
  "value": 120
}
```

Adds external data into processing queue.

---

# Streamlit Dashboard

The dashboard provides:

* detector metrics
* live data visualization
* recent alerts table
* real-time monitoring

---

# Setup Instructions

## 1. Clone Repository

```bash
git clone https://github.com/yourusername/real-time-anomaly-detection.git
```

---

## 2. Create Virtual Environment

### Windows

```bash
python -m venv anomaly_env
anomaly_env\Scripts\activate
```

### Linux/macOS

```bash
python3 -m venv anomaly_env
source anomaly_env/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Run FastAPI Server

```bash
uvicorn api.server:app --reload
```

FastAPI will run at:

```text
http://127.0.0.1:8000
```

Swagger documentation:

```text
http://127.0.0.1:8000/docs
```

---

## 5. Run Streamlit Dashboard

Open another terminal:

```bash
streamlit run dashboard/app.py
```

---

# Key Concepts Learned

* Object-Oriented Programming
* Abstract Base Classes
* Factory Design Pattern
* Threading
* Producer-Consumer Architecture
* Queue Synchronization
* Sliding Window Algorithms
* Heap Data Structure
* REST APIs
* Database Persistence
* Real-Time Data Processing
* Dashboard Visualization

---

# Future Improvements

Possible future enhancements:

* WebSocket real-time streaming
* Docker deployment
* Authentication system
* Kafka integration
* Email/SMS alerts
* Machine Learning based anomaly detection
* Cloud deployment

---

# Author

Narendra Rao Jami

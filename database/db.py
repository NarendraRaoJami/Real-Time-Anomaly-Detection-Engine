import sqlite3

class DatabaseManager:

    def __init__(self, db_name = "anomaly.db"):
        self.conn = sqlite3.connect(db_name, check_same_thread= False)
        # since FastAPI thread and consumer thread may access database
        # but SQLite normally blocks the cross-thread access
        # this setting allows shared usage (critical threading detail)
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS alerts(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            severity TEXT,
            score REAL,
            value REAL,
            message TEXT,
            timestamp TEXT
        )
        """)

        self.conn.commit()

    def insert_alert(self, alert):
        self.cursor.execute("""
        INSERT INTO alerts (
            severity,
            score,
            value,
            message,
            timestamp               
        )
        VALUES (?,?,?,?,?)
        """,(alert.severity.name,alert.score,alert.value,alert.message,str(alert.timestamp)))

        self.conn.commit()

    def fetch_alerts(self):
        self.cursor.execute("""
                            SELECT severity, score, value, message, timestamp
                            FROM alerts
                            ORDER BY id DESC
                            """)
        
        return self.cursor.fetchall()

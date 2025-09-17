from fastapi import FastAPI
import datetime
from prometheus_client import Counter, Gauge, generate_latest

app = FastAPI(
    title="Monitoring Service API",
    description="Tracks uptime, latency, and error rates across all services",
    version="1.0.0"
)

# Prometheus metrics
REQUEST_COUNT = Counter("monitoring_requests_total", "Total requests to monitoring service")
SERVICE_UP = Gauge("service_up", "Service health status (1=up, 0=down)", ["service_name"])

@app.get("/health")
def health_check():
    REQUEST_COUNT.inc()
    return {"status": "ok", "service": "monitoring-service"}

@app.get("/metrics")
def get_metrics():
    REQUEST_COUNT.inc()
    return generate_latest().decode("utf-8")

@app.get("/status/{service_name}")
def service_status(service_name: str):
    # Mock: always up
    SERVICE_UP.labels(service_name=service_name).set(1)
    return {
        "service": service_name,
        "status": "up",
        "timestamp": datetime.datetime.utcnow().isoformat()
    }

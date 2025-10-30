"""Monitoring and metrics for LLMs_OS"""
from prometheus_client import Counter, Histogram, start_http_server
import time

task_counter = Counter('llms_os_tasks_total', 'Total tasks executed', ['action', 'status'])
task_duration = Histogram('llms_os_task_duration_seconds', 'Task execution time', ['action'])

def start_metrics_server(port=9090):
    """Start Prometheus metrics server"""
    try:
        start_http_server(port)
    except Exception:
        pass

def record_task(action, status, duration=0):
    """Record task metrics"""
    task_counter.labels(action=action, status=status).inc()
    if duration > 0:
        task_duration.labels(action=action).observe(duration)

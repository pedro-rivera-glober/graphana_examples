from fastapi import FastAPI
from prometheus_client import Counter, generate_latest

app = FastAPI()

# Prometheus metrics
REQUESTS_TOTAL = Counter(
    'requests_total', 'Total number of requests to the hello world app'
)

@app.get("/")
async def hello_world():
    REQUESTS_TOTAL.inc()  # Increment the counter
    return {"message": "Hello World"}

@app.get("/metrics")
def metrics():
    return generate_latest()
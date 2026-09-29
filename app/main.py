from fastapi import FastAPI

app = FastAPI(title="CloudOps Deployment Platform")


@app.get("/")
def root():
    return {"message": "CloudOps Deployment Platform is running"}

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.get("/version")
def version():
    return {"version": "1.0.1"}

@app.get("/api/status")
def api_status():
    return {
        "application": "CloudOps Deployment Platform",
        "environment": "development",
        "status": "running"
    }


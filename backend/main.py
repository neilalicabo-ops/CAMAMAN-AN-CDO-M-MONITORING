from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="CAMAMAN-AN-CDO-M-MONITORING")

class HealthResponse(BaseModel):
    status: str

class ApiResponse(BaseModel):
    status: str
    message: str

@app.get("/health", response_model=HealthResponse)
def health():
    return HealthResponse(status="ok")

@app.get("/", response_model=ApiResponse)
def root():
    return ApiResponse(status="ok", message="CAMAMAN-AN-CDO-M-MONITORING is running")

@app.get("/api", response_model=ApiResponse)
def api_root():
    return ApiResponse(status="ok", message="CAMAMAN-AN-CDO-M-MONITORING API is running")

@app.get("/api/health", response_model=HealthResponse)
def api_health():
    return HealthResponse(status="ok")

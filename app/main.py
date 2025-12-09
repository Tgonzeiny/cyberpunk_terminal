from fastapi import FastAPI, Query
import time
import platform
from fastapi.middleware.cors import CORSMiddleware
from app.data import get_augmentations, get_district_status, scan_citizen, get_latest_news

app = FastAPI(title="Cyberpunk Terminal API")\

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"status": "online", "message": "Neon Grid Operational"}

@app.get("/augmentations")
def augmentations():
    return get_augmentations()

@app.get("/districts/status")
def district_status():
    return get_district_status()

@app.get("/scan")
def scan(name: str = Query(..., description="Citizen name to scan")):
    return scan_citizen(name)

@app.get("/news/latest")
def news_latest():
    return get_latest_news()

@app.get("/health")
def health():
    return {"status": "healthy"}

start_time = time.time()

@app.get("/sys/info")
def sys_info():
    return {
        "uptime_seconds": round(time.time() - start_time, 2),
        "server": platform.node(),
        "python_version": platform.python_version(),
        "status": "operational"
    }
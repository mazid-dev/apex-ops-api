from fastapi import FastAPI
from fastapi.responses import JSONResponse
import logging, os, json, time
import psycopg2

app = FastAPI()
logging.basicConfig(level=logging.INFO, format="%(message)s")
logger = logging.getLogger("apex")

def log(event, **kw):
    logger.info(json.dumps({"event": event, "ts": time.time(), **kw}))

@app.get("/health")
def health():
    log("health_check")
    return {"status": "ok"}

@app.get("/ready")
def ready():
    try:
        conn = psycopg2.connect(os.environ["DATABASE_URL"], connect_timeout=2)
        conn.close()
        log("readiness_ok")
        return {"status": "ready"}
    except Exception as e:
        log("readiness_fail", error=str(e))
        return JSONResponse(status_code=503, content={"status": "not_ready"})
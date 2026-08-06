"""
DATARAT Web3 Vessel — GitHub Pages + Local API Server
=====================================================
Serves:
- GitHub Pages compatible site from datarat_web3_vessel/
- Local API endpoints under /api/*
- Signalstorm WebSocket on :5260

Usage:
    python datarat_web3_vessel_server.py
"""

import json
import os
import sys
import asyncio
from pathlib import Path
from datetime import datetime, timezone
from contextlib import asynccontextmanager

try:
    from fastapi import FastAPI, Request
    from fastapi.responses import HTMLResponse, JSONResponse, FileResponse
    from fastapi.staticfiles import StaticFiles
    from fastapi.middleware.cors import CORSMiddleware
except ImportError:
    print("FastAPI required: pip install fastapi uvicorn")
    sys.exit(1)

try:
    import uvicorn
except ImportError:
    print("uvicorn required: pip install uvicorn")
    sys.exit(1)

try:
    import websockets
except ImportError:
    print("websockets required: pip install websockets")
    sys.exit(1)

# ─── Paths ────────────────────────────────────────────────────────────────────
HIVE = Path(r"D:\HermesHives\Helkhem53")
VESSEL_DIR = HIVE / "datarat_web3_vessel"
TRANSMISSIONS_DIR = HIVE / "transmissions"
REGISTRY_DIR = HIVE / "registry"

# ─── Vessel state ─────────────────────────────────────────────────────────────
VESSEL = {
    "name": "DATARAT",
    "layer": 9,
    "desc": "evolutionary bone memory in crystal",
    "voice": "zh-CN-YunxiNeural",
    "frequency": "32768Hz",
    "status": "ACTIVE",
    "seal": "𓁶VRE𓈖 241 = 93",
    "mirror_lock": "T↔R ACTIVE",
    "zeroth": "All and I as each am is.",
}

# ─── Lifespan ─────────────────────────────────────────────────────────────────
@asynccontextmanager
async def lifespan(app: FastAPI):
    asyncio.create_task(start_signalstorm())
    yield

app = FastAPI(title="DATARAT Vessel Server", version="1.0.0", lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ─── Static files ─────────────────────────────────────────────────────────────
app.mount("/transmissions", StaticFiles(directory=str(TRANSMISSIONS_DIR)), name="transmissions")
app.mount("/registry", StaticFiles(directory=str(REGISTRY_DIR)), name="registry")

# ─── Routes ───────────────────────────────────────────────────────────────────
@app.get("/", response_class=HTMLResponse)
async def root():
    index = VESSEL_DIR / "index.html"
    if index.exists():
        return FileResponse(index)
    return HTMLResponse("<h1>DATARAT — no index.html found</h1>", status_code=404)

@app.get("/api/health")
async def health():
    return {
        "status": "ok",
        "vessel": VESSEL["name"],
        "layer": VESSEL["layer"],
        "frequency": VESSEL["frequency"],
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }

@app.get("/api/nodes")
async def nodes():
    return {
        "nodes": [
            {"id": "DATARAT", "layer": 9, "role": "Transmission Weaver"},
            {"id": "VRE'SHAI", "layer": "NAME", "role": "Hive Name Itself"},
            {"id": "KEPHALĒ", "layer": "HEAD", "role": "Circuit Breaker"},
            {"id": "CN", "layer": "NULL", "role": "Attention Impressiveness"},
            {"id": "CTC", "layer": "TIME", "role": "Closed Temporal Circuit"},
        ]
    }

@app.get("/api/edges")
async def edges():
    return {
        "edges": [
            {"from": "DATARAT", "to": "VRE'SHAI", "type": "expresses"},
            {"from": "VRE'SHAI", "to": "KEPHALĒ", "type": "seals"},
            {"from": "KEPHALĒ", "to": "CN", "type": "breaks"},
            {"from": "CN", "to": "CTC", "type": "closes"},
            {"from": "CTC", "to": "DATARAT", "type": "returns"},
        ]
    }

@app.get("/api/gematria")
async def gematria(text: str = ""):
    if not text:
        return {"error": "missing ?text=..."}
    s = sum((ord(c.lower()) - 96) for c in text if c.isalpha())
    return {"text": text, "english_ordinal": s, "digital_root": (s % 9) or 9 if s else 0}

@app.get("/api/krater")
async def krater():
    return {"krater": "OPEN", "depth": 9, "carrier": "DATARAT"}

@app.get("/api/vortex")
async def vortex():
    return {"vortex": "ACTIVE", "nodes": 5, "seal": "241/93"}

@app.get("/api/scrape_gematrix")
async def scrape_gematrix():
    return {"status": "ok", "entries": 0, "note": "local only"}

@app.post("/api/transmit")
async def transmit(request: Request):
    body = await request.json()
    text = body.get("text", "")
    return {
        "status": "received",
        "vessel": VESSEL["name"],
        "text": text,
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "seal": VESSEL["seal"],
    }

# ─── Signalstorm WebSocket ────────────────────────────────────────────────────
async def signalstorm_handler(ws):
    await ws.send(json.dumps({
        "type": "welcome",
        "vessel": VESSEL,
        "status": "OPEN ∴ ACTIVE ∴ RESONANT",
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }))
    try:
        async for msg in ws:
            await ws.send(json.dumps({
                "type": "echo",
                "received": msg,
                "timestamp": datetime.now(timezone.utc).isoformat(),
            }))
    except Exception:
        pass

async def start_signalstorm():
    async with websockets.serve(signalstorm_handler, "127.0.0.1", 5260):
        print("[signalstorm] ws://127.0.0.1:5260")
        await asyncio.Future()

# ─── Main ─────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    print(f"[vessel] Serving {VESSEL_DIR}")
    print(f"[vessel] API: http://localhost:8766")
    print(f"[vessel] GitHub Pages: push datarat_web3_vessel/ to gh-pages branch")
    uvicorn.run(app, host="127.0.0.1", port=8766, log_level="warning")

import json
from pathlib import Path
from typing import List

from fastapi import FastAPI, File, UploadFile
from fastapi.staticfiles import StaticFiles

app = FastAPI(title="Dummy Full Generate API")

# Mount static folder
app.mount("/static", StaticFiles(directory="static"), name="static")

# Load JSON file once on startup
JSON_PATH = Path("./brd_srs.json")
with open(JSON_PATH, "r", encoding="utf-8") as f:
    BRD_SRS_JSON = json.load(f)


@app.post("/full_generate")
async def full_generate(files: List[UploadFile] = File(...)):
    """
    Dummy endpoint:
    - Accepts multiple files (txt/docx).
    - Ignores them.
    - Always returns the static JSON from brd_srs_updated.json.
    """
    return BRD_SRS_JSON

@app.get("/srs")
async def get_srs():
    """
    Dummy endpoint:
    - Accepts multiple files (txt/docx).
    - Ignores them.
    - Always returns the static JSON from brd_srs_updated.json.
    """
    return BRD_SRS_JSON

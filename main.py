"""Dummy App"""

import json
from pathlib import Path
from typing import List

from fastapi import FastAPI, File, HTTPException, UploadFile
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI(title="Dummy Full Generate API")

app.mount("/static", StaticFiles(directory="static"), name="static")

BASE_DIR = Path(__file__).resolve().parent
PROJECTS_DIR = BASE_DIR / "projects"

# Load JSON file once on startup
# JSON_PATH = Path("./brd_srs.json")
# with open(JSON_PATH, "r", encoding="utf-8") as f:
#     BRD_SRS_JSON = json.load(f)


@app.post("/full_generate/{document_name}")
async def full_generate(document_name: str, files: List[UploadFile] = File(...)):
    """
    Dummy endpoint:
    - Accepts multiple files (txt/docx).
    - Ignores them.
    - Always returns the static JSON from brd_srs_updated.json.
    """
    project_file = PROJECTS_DIR / f"{document_name}.json"

    if not project_file.exists():
        raise HTTPException(status_code=404, detail="Document not found")

    try:
        with open(project_file, "r", encoding="utf-8") as f:
            project_data = json.load(f)
    except json.JSONDecodeError as e:
        raise HTTPException(status_code=500, detail="Invalid JSON in project file") from e

    return JSONResponse(content=project_data)


@app.get("/srs/{document_name}")
async def get_srs(document_name: str):
    """
    Dummy endpoint:
    - Accepts multiple files (txt/docx).
    - Ignores them.
    - Always returns the static JSON from brd_srs_updated.json.
    """
    project_file = PROJECTS_DIR / f"{document_name}.json"

    if not project_file.exists():
        raise HTTPException(status_code=404, detail="Document not found")

    try:
        with open(project_file, "r", encoding="utf-8") as f:
            project_data = json.load(f)
    except json.JSONDecodeError as e:
        raise HTTPException(status_code=500, detail="Invalid JSON in project file") from e

    return JSONResponse(content=project_data)

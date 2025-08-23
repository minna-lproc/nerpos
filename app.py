# app.py — POS + NER web app (FastAPI + spaCy)
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from typing import List, Dict, Any
import spacy
import os

ALLOW_ORIGINS = os.getenv("ALLOW_ORIGINS", "*").split(",")

app = FastAPI(title="POS & NER API", version="1.0.0")
app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOW_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Serve static UI (./static)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Load spaCy model (included via requirements.txt)
# For other languages, install e.g. de_core_news_sm and load it similarly.
try:
    nlp = spacy.load("en_core_web_sm")
except Exception as e:
    raise RuntimeError(
        "Failed to load spaCy model 'en_core_web_sm'. "
        "Make sure requirements.txt includes the model wheel."
    ) from e

class AnalyzeIn(BaseModel):
    text: str

@app.get("/")
def root():
    return {
        "message": "POS & NER service is running.",
        "try": ["/static/index.html", "/docs", "POST /analyze"],
    }

@app.post("/analyze")
def analyze(payload: AnalyzeIn) -> Dict[str, Any]:
    try:
        doc = nlp(payload.text)
        tokens = [
            {
                "text": t.text,
                "lemma": t.lemma_,
                "pos": t.pos_,
                "tag": t.tag_,
                "idx": t.idx,
            }
            for t in doc
        ]
        ents = [
            {
                "text": ent.text,
                "label": ent.label_,
                "start_char": ent.start_char,
                "end_char": ent.end_char,
            }
            for ent in doc.ents
        ]
        return {"text": payload.text, "tokens": tokens, "ents": ents}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/health")
def health():
    return {"status": "ok", "model": "en_core_web_sm"}

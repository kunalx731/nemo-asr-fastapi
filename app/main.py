from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse
import numpy as np
from io import BytesIO
from app.utils import read_audio
from app.model import load_model
import uvicorn

app = FastAPI()
model = load_model()

@app.post("/transcribe")
async def transcribe(file: UploadFile = File(...)):
    if not file.filename.endswith(".wav"):
        raise HTTPException(status_code=400, detail="Invalid file type. Only .wav allowed")

    audio_bytes = await file.read()
    samples, sr = read_audio(BytesIO(audio_bytes))

    if len(samples) < 16000 * 5 or len(samples) > 16000 * 10:
        raise HTTPException(status_code=400, detail="Audio length must be 5-10 seconds")

    logits = model.transcribe([samples])
    return JSONResponse(content={"transcript": logits[0]})

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
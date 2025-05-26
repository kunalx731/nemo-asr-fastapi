# FastAPI ASR with NVIDIA NeMo

## Overview
This project deploys a Hindi ASR (Automatic Speech Recognition) model using NVIDIA NeMo with FastAPI. It includes ONNX optimization and is containerized using Docker.

## Instructions

### 1. Export model to ONNX
```bash
python model_export.py
```

### 2. Build the Docker container
```bash
docker build -t nemo-asr .
```

### 3. Run the container
```bash
docker run -p 8000:8000 nemo-asr
```

### 4. Test transcription endpoint

You can use the included `sample.wav` file (5–10 seconds, 16kHz mono) to test the transcription:
```bash
curl -X POST "http://localhost:8000/transcribe" -F "test_file.wav"
```

## Notes
- Audio must be a `.wav` file at 16kHz, duration 5–10 seconds.
- This project uses the `stt_hi_conformer_ctc_medium` model from NVIDIA NGC.


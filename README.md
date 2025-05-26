# 🗣️ Nemo-ASR FastAPI for Hindi Speech Recognition

This project provides an API service that transcribes Hindi speech into text using NVIDIA's NeMo toolkit. It leverages a pre-trained speech-to-text model and serves transcriptions through a FastAPI backend. The application supports uploading `.wav` files and returns accurate Hindi transcriptions.

---

## 🧠 Model Information

The system uses the `stt_hi_conformer_ctc_medium` model, a medium-sized Conformer CTC model optimized for Hindi speech recognition.

- 🔗 **Source**: [NVIDIA NGC Catalog - NeMo ASR Models](https://catalog.ngc.nvidia.com/orgs/nvidia/teams/nemo/models/stt_hi_conformer_ctc_medium)
- 🧰 **Framework**: [NVIDIA NeMo](https://developer.nvidia.com/nemo)
- 📤 **Usage**: The model is exported to ONNX using the `model_export.py` script before inference.

---

## 🚀 Features

- ✅ Accepts `.wav` audio input (16 kHz)
- ✅ Returns Hindi text transcription
- ✅ ONNX-accelerated inference
- ✅ REST API built with FastAPI
- ✅ Docker and non-Docker setup options

---

## ⚙️ Local Installation (Without Docker)

You can run the project directly on your machine without using Docker.

### 1. Clone the Repository

```bash
git clone https://github.com/kunalx731/nemo-asr-fastapi.git
cd nemo-asr-fastapi

```

### 2.Set Up a Virtual Environment (Optional but Recommended)
```bash
python -m venv venv
source venv/bin/activate  # For Windows: venv\Scripts\activate
```

### 3.Install Dependencies
```bash
pip install -r requirements.txt
```
### 4.Export the ASR Model to ONNX
This step downloads and converts the NeMo model to ONNX format for optimized inference.
```bash
python model_export.py
```
### 5.Run the FastAPI Server
The server will start at http://127.0.0.1:8000.
```bash
uvicorn app.main:app --reload
```
### 6.Test transcription endpoint

You can use the included `sample.wav` file (5–10 seconds, 16kHz mono) to test the transcription:
```bash
curl -X POST "http://localhost:8000/transcribe" -F "test_file.wav"
```

## Notes
- Audio must be a `.wav` file at 16kHz, duration 5–10 seconds.
- This project uses the `stt_hi_conformer_ctc_medium` model from NVIDIA NGC.


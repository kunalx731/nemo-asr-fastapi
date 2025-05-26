# Development Report

## ✅ Features Implemented
- Downloaded and used the Hindi ASR model from NVIDIA NeMo.
- Exported the model to ONNX format.
- Built a FastAPI application with `/transcribe` endpoint.
- Implemented input validation (file type, duration).
- Created a lightweight Dockerfile for deployment.

## ⚠️ Issues Faced
- Async model inference not fully compatible due to blocking nature of NeMo inference.
- Large container image without further optimization.

## 🛠 Limitations & Future Work
- Use TorchScript for async-friendliness.
- Consider multi-stage Docker build for reduced size.
- Enhance inference pipeline with streaming/batching.

## 🔎 Assumptions
- `.wav` files are mono and sampled at 16kHz.
- Audio clips are less than 10 seconds.
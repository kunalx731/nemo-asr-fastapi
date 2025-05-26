from app.model import load_model, export_to_onnx

model = load_model()
export_to_onnx(model)
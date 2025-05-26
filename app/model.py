import nemo.collections.asr as nemo_asr
import torch
from nemo.export import ExportConfig
from nemo.export.pytorch import export as nemo_export

MODEL_NAME = "stt_hi_conformer_ctc_medium"

def load_model():
    model = nemo_asr.models.EncDecCTCModel.from_pretrained(model_name=MODEL_NAME)
    return model

def export_to_onnx(model, export_path="model.onnx"):
    model.export(
        output=export_path,
        check_trace=False,
        onnx_opset_version=14
    )
    return export_path
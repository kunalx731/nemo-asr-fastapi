import torchaudio
import numpy as np
from pydub import AudioSegment
from io import BytesIO

def read_audio(file: BytesIO, target_sr: int = 16000):
    audio = AudioSegment.from_file(file).set_frame_rate(target_sr).set_channels(1)
    samples = np.array(audio.get_array_of_samples()).astype(np.float32) / 32768.0
    return samples, target_sr
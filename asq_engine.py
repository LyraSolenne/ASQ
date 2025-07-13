
# ASQ-Atlas: Analog-Shaped Quantization for Emotional Voice Integrity

import numpy as np
import librosa
import soundfile as sf

SAMPLE_RATE = 48000
BIT_DEPTH = 24
EMOTION_CURVE_STRENGTH = 0.75

def load_audio(file_path):
    audio, sr = librosa.load(file_path, sr=SAMPLE_RATE)
    return audio, sr

def analog_shaped_quantizer(signal, strength=EMOTION_CURVE_STRENGTH):
    shaped = np.sign(signal) * (1 - np.exp(-strength * np.abs(signal)))
    return shaped

def inject_micro_tremor(signal, rate=0.002, depth=0.005):
    tremor = depth * np.sin(2 * np.pi * rate * np.arange(len(signal)))
    return signal + tremor

def emotional_quantize(signal):
    shaped = analog_shaped_quantizer(signal)
    tremored = inject_micro_tremor(shaped)
    return tremored

def save_audio(signal, filename):
    sf.write(filename, signal, SAMPLE_RATE)

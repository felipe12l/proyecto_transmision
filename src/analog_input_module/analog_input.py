import numpy as np
import matplotlib.pyplot as plt
import scipy.io.wavfile as waves
from scipy.signal import resample

def anolog_input_wav(file, start_time=0, end_time=None):
    sampling_rate, sound = waves.read(file)

    if len(sound.shape) == 2:
        sound = sound[:, 0]

    start_sample = int(start_time * sampling_rate)
    end_sample = int(end_time * sampling_rate) if end_time else len(sound)
    sound = sound[start_sample:end_sample]

    target_nyquist = 8000

    if sampling_rate < target_nyquist:
        num_samples = int(len(sound) * (target_nyquist / sampling_rate))  
        sound = resample(sound, num_samples)  
        sampling_rate = target_nyquist  


    dt = 1 / sampling_rate
    t = np.linspace(start_time, start_time + (len(sound) - 1) * dt, len(sound))

    return t, sound

import librosa
import matplotlib.pyplot as plt
import librosa.display
from scipy.io import wavfile
import numpy as np
import noisereduce as nr

audio_path = 'noise.wav'
x , sr = librosa.load(audio_path)

plt.figure(figsize=(14, 5))
librosa.display.waveplot(x, sr=sr)
plt.show()

rate, data = wavfile.read(audio_path)
data = np.asarray(data, dtype=np.float16)
reduced_noise = nr.reduce_noise(audio_clip=data, noise_clip=data)

plt.figure(figsize=(14, 5))
librosa.display.waveplot(reduced_noise, sr=rate)
plt.show()

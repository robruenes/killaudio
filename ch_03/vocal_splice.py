from scipy.io import wavfile
import numpy as np
import matplotlib.pyplot as plt

if __name__ == "__main__":
    # Vocal.wav is another single channel audio file.
    # The sample rate is 44100, and there are 215444
    # samples.
    sample_rate, data = wavfile.read("Vocal.wav")
    first_slice = data[:47609]
    second_slice = data[123252:]
    final_edit = np.concatenate([first_slice, second_slice])
    wavfile.write("Vocal_edit.wav", sample_rate, final_edit)

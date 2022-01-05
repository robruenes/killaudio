from scipy.io import wavfile
import numpy as np


def create_spliced_edit(sample_rate, data):
    first_slice = data[:47609]
    second_slice = data[123252:]
    final_edit = np.concatenate([first_slice, second_slice])
    wavfile.write("output_wav_files/Vocal_spliced_edit.wav",
                  sample_rate, final_edit)


def create_reversed_edit(sample_rate, data):
    # The below is equivalent to using
    # the flip function in numpy:
    #   reversed = np.flip(data)
    # We use the slice syntax here instead to build off the examples
    # from ch_03.ipynb.
    reversed = data[-1:0:-1]
    wavfile.write("output_wav_files/Vocal_reversed_edit.wav",
                  sample_rate, reversed)


if __name__ == "__main__":
    # Vocal.wav is another single channel audio file.
    # The sample rate is 44100, and there are 215444
    # samples.
    sample_rate, data = wavfile.read("input_wav_files/Vocal.wav")
    create_spliced_edit(sample_rate, data)
    create_reversed_edit(sample_rate, data)

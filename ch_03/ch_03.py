from scipy.io import wavfile
import numpy as np
import matplotlib.pyplot as plt


def print_wav_data(sample_rate, length_in_seconds, data):
    print("Numpy array representing file:")
    print(f"The file is {data.ndim}-dimensional.")
    print(f"There are {data.shape[0]} samples.")
    print(f"The sample rate is {sample_rate} samples/second.")
    print(f"The resulting length is {length_in_seconds} seconds.")


def plot_wav_graph(sample_rate, length_in_seconds, num_samples, data):
    time = np.linspace(0., length_in_seconds, num_samples)
    plt.plot(time, data, label="Single Channel")
    plt.legend()
    plt.xlabel("Time in seconds")
    plt.xscale("logit")
    plt.ylabel("Amplitude")
    plt.show()


if __name__ == "__main__":
    sample_rate, data = wavfile.read("sw440Hz.wav")

    # Write a new file using the same rate and the numpy data.
    wavfile.write("ch_3_output.wav", sample_rate, data)

    # sw440Hz.wav is a single channel input file,
    # so the resulting numpy array is one-dimensional,
    # and data.shape has a single value at index 0
    # corresponding to the number of samples.
    num_samples = data.shape[0]
    length_in_seconds = num_samples / sample_rate
    print_wav_data(sample_rate, length_in_seconds, data)
    plot_wav_graph(sample_rate, length_in_seconds, num_samples, data)

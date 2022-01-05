from scipy.io import wavfile
import numpy as np
import matplotlib.pyplot as plt


def plot_sample_number_against_amplitude(num_samples, sample_rate, data):
    num_samples = data.shape[0]
    sample_number_arr = np.arange(0, num_samples)
    plt.plot(sample_number_arr, data)
    plt.xlabel("Sample number")
    plt.ylabel("Amplitude")
    plt.show()


def plot_time_against_amplitude(num_samples, sample_rate, data):
    time_interval = 1 / sample_rate
    length_in_seconds = num_samples / sample_rate
    time_arr = np.arange(0, length_in_seconds, time_interval)
    plt.plot(time_arr, data)
    plt.xlabel("Time (sec.)")
    plt.ylabel("Amplitude")
    plt.show()


if __name__ == "__main__":
    sample_rate, data = wavfile.read("sw20Hz.wav")
    num_samples = data.shape[0]
    plot_sample_number_against_amplitude(num_samples, sample_rate, data)
    plot_time_against_amplitude(num_samples, sample_rate, data)

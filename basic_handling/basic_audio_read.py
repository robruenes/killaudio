from scipy.io import wavfile
import numpy as np
import matplotlib.pyplot as plt


def main():
    sample_rate, data = wavfile.read("sw440Hz.wav")
    print("Numpy array representing file:")
    print(f"The file is {data.ndim}-dimensional.")

    num_samples = data.shape[0]
    print(f"There are {num_samples} samples.")
    print(f"The sample rate is {sample_rate} samples/second.")
    length = data.shape[0] / sample_rate
    print(f"The resulting length is {length}s")


if __name__ == "__main__":
    main()

from scipy.io import wavfile

if __name__ == "__main__":
    sample_rate, data = wavfile.read("input_wav_files/sw440Hz.wav")

    # Write a new file using the same rate and the numpy data.
    wavfile.write("output_wav_files/sw440Hz_copy.wav", sample_rate, data)

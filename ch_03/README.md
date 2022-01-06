# Chapter 3: Basics of Audio in Python

Below is a quick explanation of the files in this directory.

## ch_03.ipynb

This IPython notebook file contains examples of creating, reading, and manipulating
single and multidimensional numpy arrays, which act as the primary representation
of audio files throughout futher examples.

## copy_wav_file.py

This script reads the file `input_wav_files/sw440Hz.wav`, and produces the
copy `output_wav_files/sw440Hz_copy.wav`.

## visualize_waveform.py

This script produces two graphs of the waveform in the `input_wav_files/sw20Hz.wave` file.

## vocal_modifications.py

This script reads the file `input_wav_files/Vocal.wav`, and produces two
output files in the `output_wav_files` directory.

- `Vocal_spliced_edit.wav`, which contains a subset of the audio from `Vocal.wav`
- `Vocal_reversed_edit.wav`, which contains reversed audio generated from `Vocal.wav`.

### Quick note on running these scripts

As written:
  
  - The scripts must be run from inside this ch_03 directory to find the input files.
  - The directory `output_wav_files` needs to exist (but can be empty) in order to produce
    the output wav files.


# killaudio

This directory contains python implementations of the exercises in Eric Tarr's [*Hack Audio: An Introduction to Computer Programming and Digital Signal Processing in Matlab*](https://www.mathworks.com/academia/books/hack-audio-tarr.html).

Why _killaudio_? The name _Hack Audio_ reminded me of the [comic book series Kill Audio](https://www.simonandschuster.com/books/Kill-Audio/Claudio-Sanchez/9781608862924) by Coheed and Cambria's frontman, Claudio Sanchez.

# Project Setup

This project uses [Anaconda](https://www.anaconda.com) for dependency and environment management, and I use a MacBook Pro as my development machine.

First, install Anaconda using the [command line installer](https://docs.anaconda.com/anaconda/install/mac-os/#using-the-command-line-install).

Afterwards, we'll want to set up a new environment and install [NumPy](https://numpy.org), [SciPy](http://scipy.org), [Matplotlib](https://matplotlib.org), and [Jupyter Notebooks](https://jupyter.org/install).

```
$ conda create -n killaudio
$ conda activate killaudio
$ conda install numpy
$ conda install scipy
$ conda install matplotlib
$ conda install jupyterlab
```
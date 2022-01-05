# killaudio

This directory contains Python implementations of the exercises in Eric Tarr's [*Hack Audio: An Introduction to Computer Programming and Digital Signal Processing in Matlab*](https://www.mathworks.com/academia/books/hack-audio-tarr.html).

Why _killaudio_? The name _Hack Audio_ reminded me of the [comic book series Kill Audio](https://www.simonandschuster.com/books/Kill-Audio/Claudio-Sanchez/9781608862924) by Coheed and Cambria's frontman, Claudio Sanchez.

# Project Setup

This project uses [Anaconda](https://www.anaconda.com) for dependency and environment management. I use a MacBook Pro as my development machine, and I primarily work on the command line. 

The instructions below should work largely as-written on a Linux machine, but if you're using Windows, you'll either want to consider using the [Windows Subsystem for Linux](https://docs.microsoft.com/en-us/windows/wsl/install) (so you can follow along using the same instructions below), or will need to spend some time investigating getting everything up and running for a Windows environment.

## Installing Anaconda

First, install Anaconda.

- If you're using a Mac, follow these [command line installer instructions](https://docs.anaconda.com/anaconda/install/mac-os/#using-the-command-line-install)
- If you're running Linux, [follow these instructions](https://docs.anaconda.com/anaconda/install/linux/).

## Create a dedicated environment

Next, we're going to create a dedicated environment for the dependencies we need. The official documentation for doing so [is here](https://docs.anaconda.com/anaconda/install/linux/).

In the example below, I've chosen to name the environment *killaudio*.

```
$ conda create -n killaudio
$ conda activate killaudio
```

## Installing dependencies

We need the following dependencies for the examples in this repository.
- [NumPy](https://numpy.org)
- [SciPy](http://scipy.org)
- [Matplotlib](https://matplotlib.org)
- [Jupyter Notebooks](https://jupyter.org/install)
- [Pyaudio](https://people.csail.mit.edu/hubert/pyaudio/)

```
$ conda install numpy
$ conda install scipy
$ conda install matplotlib
$ conda install jupyterlab
$ conda install pyaudio
```

### Note on Jupyter Notebooks and Google Colab

In some directories, you'll find files ending with the `.ipynb` extension. These are *interactive Python notebook files*, which allow you to write Python code and execute it in realtime inside of the notebook, along formatted documentation, etc.

In the course of creating these examples, I'm creating notebooks in [Google Colab](https://research.google.com/colaboratory/), which is a free to use, in-browser environment for interactive Python notebooks (using Google's computing resources).

If you clone this repository and want to open the files in Jupyter Notebooks *instead* of Google Colab, you can run the following:

`$ jupyter-lab <filename>`

## Troubleshooting Environments
If at any point you need to list out the environments
on your development machine, you can run:

`$ conda info --envs`

And to apply a given environment, run:

`$ conda activate <envname>`

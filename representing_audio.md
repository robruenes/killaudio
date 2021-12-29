# Representing Audio

Audio signals can be represented as a function of amplitude over continuous time.


> _Audio Signal = A(t)_

Unlike electric representations of sound (voltage or current over time) and acoustic representations of sound (sound pressure over time), digital representations are sampled.

_T<sub>s_ is known as the _sampling period_. 

> _Sampling Period = T<sub>s_

This is the interval in which an amplitude value is captured from a given analog signal. The unit of measurement is seconds per sample.

In turn, the _sampling rate, F<sub>s_, is the number of samples per second.

> _Sampling Rate = F<sub>s</sub> = $\frac{1}{T_s}$_

The _Nyquist frequency_ is half of the sampling rate.

> _Nyquist frequency_ = $\frac{F_s}{2}$

As long as all of the frequencies _f_ in the signal are less than the Nyquist frequency of the sampler, the digital signal can be reconstructed as an analog signal. This is known as the [Nyquist-Shannon sampling theorem](https://en.wikipedia.org/wiki/Nyquist–Shannon_sampling_theorem).

Because digital signals are functions of discrete time, and in turn only have amplitude values whenever a sample occurs, they are represented using a different notation, _A[n]_.

A digital signal, _x[n]_, with _N_ total samples, has individual samples _x[1], x[2], ..., x[N]_, and can be written:

> _x = {x<sub>1</sub>, x<sub>2</sub>,..., x<sub>N</sub>}_

This representation naturally translates to arrays.

Typically, a mono signal will be represented by an array with a single column and many rows. A stereo signal, on the other hand, is represented by a two-column array, with the first column representing the left channel, and the second column representing the right channel. The value in every row represents the amplitude of the signal for that individual sample, _x[n]_.
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
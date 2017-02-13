# Ricker Wavelet Generator
[Ricker wavelet](http://wiki.seg.org/wiki/Dictionary:Ricker_wavelet) (Mexican hat signal) is widely used in synthetic seismic simulation. Although, [SciPy](https://github.com/scipy/scipy#id1) offers a nice [ricker](https://docs.scipy.org/doc/scipy-0.18.1/reference/generated/scipy.signal.ricker.html) generator, it is very basic and limited in flexibility. After repeated writing similar code to generate a shifted Ricker wavelet, I decided to write a small tool for it.  

## Dependancy
*[NumPy](http://www.numpy.org/)
# Ricker Wavelet Generator

[![Build Status](https://travis-ci.org/gatechzhu/ricker.svg?branch=master)](https://travis-ci.org/gatechzhu/ricker)

## Introduction
[Ricker wavelet](http://wiki.seg.org/wiki/Dictionary:Ricker_wavelet) (Mexican hat signal) is widely used in synthetic seismic simulation. Although, [SciPy](https://github.com/scipy/scipy#id1) offers a nice [ricker](https://docs.scipy.org/doc/scipy-0.18.1/reference/generated/scipy.signal.ricker.html) generator, it is very basic and limited in flexibility. After repeated writing similar code to generate a shifted Ricker wavelet, I decided to write a small tool for it.  

## Dependancy
- [NumPy](http://www.numpy.org/)

## Installation
The main program should run under py26, py27, py33, py34; however, I only 
support py34 and up due to syntax conventions (mainly function annotation). 
Anyone can fork this repo and do some modification so that it will work 
perfectly fine in py33 and below.

### From source file
Under the root directory, type:

```
python setup.py install
```

In counter of any trouble, contact *gatechzhu@gmail.com*

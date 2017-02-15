# Ricker Wavelet Generator

[![PyPI version](https://badge.fury.io/py/ricker.svg)](https://badge.fury.io/py/ricker) 
[![Build Status](https://travis-ci.org/gatechzhu/ricker.svg?branch=master)](https://travis-ci.org/gatechzhu/ricker)

## Introduction
[Ricker wavelet](http://wiki.seg.org/wiki/Dictionary:Ricker_wavelet) (Mexican hat signal) is widely used in synthetic seismic simulation. Although, [SciPy](https://github.com/scipy/scipy#id1) offers a nice [ricker](https://docs.scipy.org/doc/scipy-0.18.1/reference/generated/scipy.signal.ricker.html) generator, it is very basic and limited in flexibility. After repeated writing similar code to generate a shifted Ricker wavelet, I decided to write a small tool for it.  

## Dependancy
- [NumPy](http://www.numpy.org/)

## Installation
### From PyPI
```
pip install ricker
```

### From source file
Download srouce file from [releases page](https://github.com/gatechzhu/ricker/releases). Under the root directory, type:

```
python setup.py install
```

## Contact

In counter of any trouble, contact *gatechzhu@gmail.com*

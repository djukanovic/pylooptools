# pylooptools
pylooptools is a python bindings package for the LoopTools package http://www.feynarts.de/looptools/. 

Note that this is **NOT an official LoopTools release** and I refer to http://www.feynarts.de/looptools/ for the official version. 

## Installation
We provide a python setup.py script that 
 * fetches LoopTools from http://www.feynarts.de/looptools/ (using urllib)
 * compiles the library with suitable flags and applies necessary patches to produce a shared library
 * install the python modules giving access to the LoopTools functions via Python ctypes returning numpy objects.
 The installation can be done in the commandline using
  
 ```bash
python setup.py install
```
## Usage
The python package has to be in the PYTHONPATH. A simple example python script using the library is given by

 
 ```python
#!/usr/bin/python
from pylooptools.ltools import *
# Initialize the LoopTools library

init_ltools()

print A0(.12)
```
Output of the above script is 
``` bash
 ====================================================
   FF 2.0, a package to evaluate one-loop integrals
 written by G. J. van Oldenborgh, NIKHEF-H, Amsterdam
 ====================================================
 for the algorithms used see preprint NIKHEF-H 89/17,
 'New Algorithms for One-loop Integrals', by G.J. van
 Oldenborgh and J.A.M. Vermaseren, published in
 Zeitschrift fuer Physik C46(1990)425.
 ====================================================
\mu is 1.000000
\Delta is -1.000000
(0.254431624344+0j)
```
 

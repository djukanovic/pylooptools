#!/usr/bin/env python
import numpy as np
import ctypes
from ctypes import (CDLL, POINTER, ARRAY, c_void_p,
                    c_int, byref,c_double, c_char,c_float,
                    c_char_p, create_string_buffer,Structure)
from numpy.ctypeslib import ndpointer

aa0=1

bb0=1
bb1=4
bb00=7
bb11=10
bb001=13
bb111=16
dbb0=19
dbb1=22
dbb00=25
dbb11=28
dbb001=31


cc0=1     
cc1=4
cc2=7
cc00=10
cc11=13
cc12=16
cc22=19
cc001=22
cc002=25
cc111=28
cc112=31
cc122=34
cc222=37
cc0000=40
cc0011=43
cc0012=46
cc0022=49
cc1111=52
cc1112=55
cc1122=58
cc1222=61
cc2222=64


DLL_NAME=SHAREDLIBNAME
 
libtest=ctypes.cdll.LoadLibrary(DLL_NAME)
c_int_p = POINTER(c_int)
class Complex(Structure):
	_fields_ = [("real", c_double), ("imag", c_double)]


def A0i(aa,x):
	res=Complex()
	libtest.a0i_(byref(res),byref(c_int(aa)),byref(c_double(x)),c_int_p(c_int(0)))
	return np.complex(res.real,res.imag)

def A0(x):
	res=Complex()
	libtest.a0_(byref(res),byref(c_double(x)),c_int_p(c_int(0)))
	return np.complex(res.real,res.imag)

def B0(ps,m1,m2):
	res=Complex()
	libtest.b0_(byref(res),byref(c_double(ps)),byref(c_double(m1)),byref(c_double(m2)))
	return np.complex(res.real,res.imag)

def B0i(bb,ps,m1,m2):
	res=Complex()
	libtest.b0i_(byref(res),byref(c_int(bb)),byref(c_double(ps)),byref(c_double(m1)),byref(c_double(m2)))
	return np.complex(res.real,res.imag)

def C0(p1s,p2s,p3s,m1,m2,m3):
	res=Complex()
	libtest.c0_(byref(res),byref(c_double(p1s)),byref(c_double(p2s)),byref(c_double(p3s)),byref(c_double(m1)),byref(c_double(m2)),byref(c_double(m3)))
	return np.complex(res.real,res.imag)

def C0i(cc,p1s,p2s,p3s,m1,m2,m3):
	res=Complex()
	libtest.c0i_(byref(res),byref(c_int(cc)),byref(c_double(p1s)),byref(c_double(p2s)),byref(c_double(p3s)),byref(c_double(m1)),byref(c_double(m2)),byref(c_double(m3)))
	return np.complex(res.real,res.imag)

def init_ltools():
	libtest.ltini_()
	#libtest.setmudim_(byref(c_double(np.power(.9383,2))))
	libtest.setmudim_(byref(c_double(np.power(1,2))))
	libtest.setdelta_(byref(c_double(-1.)))
	libtest.getmudim_.restype=c_double
	libtest.getdelta_.restype=c_double
	print "\mu is %lf"  %libtest.getmudim_()
	print "\Delta is %lf " %libtest.getdelta_()



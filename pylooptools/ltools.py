#!/usr/bin/env python
import numpy as np
import ctypes
from ctypes import (CDLL, POINTER, ARRAY, c_void_p,
                    c_int, byref,c_double, c_char,c_float,
                    c_char_p, create_string_buffer,Structure)
from numpy.ctypeslib import ndpointer

aa0=1
aa00=4

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

dd0=1
dd1=4
dd2=7
dd3=10
dd00=13
dd11=16
dd12=19
dd13=22
dd22=25
dd23=28
dd33=31
dd001=34
dd002=37
dd003=40
dd111=43
dd112=46
dd113=49
dd122=52
dd123=55
dd133=58
dd222=61
dd223=64
dd233=67
dd333=70
dd0000=73
dd0011=76
dd0012=79
dd0013=82
dd0022=85
dd0023=88
dd0033=91
dd1111=94
dd1112=97
dd1113=100
dd1122=103
dd1123=106
dd1133=109
dd1222=112
dd1223=115
dd1233=118
dd1333=121
dd2222=124
dd2223=127
dd2233=130
dd2333=133
dd3333=136
dd00001=139
dd00002=142
dd00003=145
dd00111=148
dd00112=151
dd00113=154
dd00122=157
dd00123=160
dd00133=163
dd00222=166
dd00223=169
dd00233=172
dd00333=175
dd11111=178
dd11112=181
dd11113=184
dd11122=187
dd11123=190
dd11133=193
dd11222=196
dd11223=199
dd11233=202
dd11333=205
dd12222=208
dd12223=211
dd12233=214
dd12333=217
dd13333=220
dd22222=223
dd22223=226
dd22233=229
dd22333=232
dd23333=235
dd33333=238

ee0=1
ee1=4
ee2=7
ee3=10
ee4=13
ee00=16
ee11=19
ee12=22
ee13=25
ee14=28
ee22=31
ee23=34
ee24=37
ee33=40
ee34=43
ee44=46
ee001=49
ee002=52
ee003=55
ee004=58
ee111=61
ee112=64
ee113=67
ee114=70
ee122=73
ee123=76
ee124=79
ee133=82
ee134=85
ee144=88
ee222=91
ee223=94
ee224=97
ee233=100
ee234=103
ee244=106
ee333=109
ee334=112
ee344=115
ee444=118
ee0000=121
ee0011=124
ee0012=127
ee0013=130
ee0014=133
ee0022=136
ee0023=139
ee0024=142
ee0033=145
ee0034=148
ee0044=151
ee1111=154
ee1112=157
ee1113=160
ee1114=163
ee1122=166
ee1123=169
ee1124=172
ee1133=175
ee1134=178
ee1144=181
ee1222=184
ee1223=187
ee1224=190
ee1233=193
ee1234=196
ee1244=199
ee1333=202
ee1334=205
ee1344=208
ee1444=211
ee2222=214
ee2223=217
ee2224=220
ee2233=223
ee2234=226
ee2244=229
ee2333=232
ee2334=235
ee2344=238
ee2444=241
ee3333=244
ee3334=247
ee3344=250
ee3444=253
ee4444=256

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

def D0(p1s,p2s,p3s,p4s,p1p2s,p2p3s,m1,m2,m3,m4):
	res=Complex()
	libtest.d0_(byref(res),byref(c_double(p1s)),byref(c_double(p2s)),byref(c_double(p3s)),byref(c_double(p4s)),byref(c_double(p1p2s)),byref(c_double(p2p3s)),byref(c_double(m1)),byref(c_double(m2)),byref(c_double(m3)),byref(c_double(m4)))
	return np.complex(res.real,res.imag)

def D0i(dd,p1s,p2s,p3s,p4s,p1p2s,p2p3s,m1,m2,m3,m4):
	res=Complex()
	libtest.d0i_(byref(res),byref(c_int(dd)),byref(c_double(p1s)),byref(c_double(p2s)),byref(c_double(p3s)),byref(c_double(p4s)),byref(c_double(p1p2s)),byref(c_double(p2p3s)),byref(c_double(m1)),byref(c_double(m2)),byref(c_double(m3)),byref(c_double(m4)))
	return np.complex(res.real,res.imag)

def E0(p1s,p2s,p3s,p4si,p5s,p1p2s,p2p3s,p3p4s,p4p5s,p5p1s,m1,m2,m3,m4,m5):
	res=Complex()
	libtest.e0_(byref(res),byref(c_double(p1s)),byref(c_double(p2s)),byref(c_double(p3s)),byref(c_double(p4s)),byref(c_double(p5s)),byref(c_double(p1p2s)),byref(c_double(p2p3s)),byref(c_double(p3p4s)),byref(c_double(p4p5s)),byref(c_double(p5p1s)),byref(c_double(m1)),byref(c_double(m2)),byref(c_double(m3)),byref(c_double(m4)),byref(c_double(m5)))
	return np.complex(res.real,res.imag)

def E0i(ee,p1s,p2s,p3s,p4s,p5s,p1p2s,p2p3s,p3p4s,p4p5s,p5p1s,m1,m2,m3,m4,m5):
	res=Complex()
	libtest.e0i_(byref(res),byref(c_int(ee)),byref(c_double(p1s)),byref(c_double(p2s)),byref(c_double(p3s)),byref(c_double(p4s)),byref(c_double(p5s)),byref(c_double(p1p2s)),byref(c_double(p2p3s)),byref(c_double(p3p4s)),byref(c_double(p4p5s)),byref(c_double(p5p1s)),byref(c_double(m1)),byref(c_double(m2)),byref(c_double(m3)),byref(c_double(m4)),byref(c_double(m5)))
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



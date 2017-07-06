from __future__ import division
from scipy.stats import signaltonoise
import numpy as np
from numpy.fft import fft2, ifft2
from PIL import Image
from pylab import *
import time
import sys


d = {}
comm_no_of_px = []
cprob_d = {}
	
# <Contrast Stretching/>...

def count(mat):
	m,n = mat.shape
	for i in xrange(m):
		for j in xrange(n):
			s = str(mat[i][j])
			dt = d.get(s,0)
			d[s] = dt + 1
	comm_no_of_px.append(d.get("0",0))
	for i in xrange(1,256):
		z = str(i)
		comm_no_of_px.append(d.get(z,0)+comm_no_of_px[i-1])

	#for i in xrange(256):
	#	print i,"-->",d.get(str(i),0),comm_no_of_px[i]

def Partition():
	max = 0
	m_i = 0
	for i in xrange(195):
		if(comm_no_of_px[i+60]-comm_no_of_px[i] > max):
			max = comm_no_of_px[i+60]-comm_no_of_px[i]
			m_i = i
	return m_i


def cont_fun(x,p):
	p1, p2 = (p,25), (p+60,230)
	x1,y1 = p1
	x2,y2 = p2
	if(x <= 100):
		return (float(y1)/x1)*x
	elif(x >= 155):
		m = float(255-y2)/(255-x2)
		return y2 + m*x - m*x2
	else:
		m = float(y2-y1)/(x2-x1)
		return y1 + m*x - m*x1

#contrast limited histogram equilisation
def contrasting(mat_c):
	mat = mat_c[:][:]
	p = Partition()
	print p
	(m,n) = mat.shape
	for i in xrange(m):
		for j in xrange(n):
			mat[i][j] = cont_fun(mat[i][j],p)
	con_i = Image.fromarray(mat)
	#con_i.show()
	con_i.save("/media/semicolon/SourceCodes/ExploProject/RESULT/contrasting.png")
	print "contrasting:",signaltonoise(mat,axis=None)


im = Image.open(sys.argv[1]).convert('L')
im = array(im)
print "Original Image : ",signaltonoise(im,axis=None)
mat = im[:][:]
count(mat)
contrasting(mat)

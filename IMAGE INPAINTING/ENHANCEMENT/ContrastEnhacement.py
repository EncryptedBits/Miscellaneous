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

def cont_fun(x):
	p = 90
	p1, p2 = (p,35), (p+60,220)
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


def contrasting(mat_c):
	mat = mat_c[:][:]
	(m,n) = mat.shape
	for i in xrange(m):
		for j in xrange(n):
			mat[i][j] = cont_fun(mat[i][j])
	print "Unsharp Masking:",signaltonoise(mat,axis=None)
	con_i = Image.fromarray(mat)
	#con_i.show()
	con_i.save("/media/semicolon/SourceCodes/ExploProject/RESULT/StaticContrasting.png")
	print "contrasting:",signaltonoise(mat,axis=None)


im = Image.open(sys.argv[1]).convert('L')
im = array(im)
print "Original Image : ",signaltonoise(im,axis=None)
mat = im[:][:]
contrasting(mat)

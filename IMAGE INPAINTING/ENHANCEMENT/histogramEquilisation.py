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





def hist_equil(mat_h):
	mat = mat_h[:][:]
	tot = comm_no_of_px[255]
	m,n = mat.shape
	for i in xrange(m):
		for j in xrange(n):
			if cprob_d.get(str(mat[i][j]),0) != 0:
				mat[i][j] = cprob_d[str(mat[i][j])]
			else:
				cprob_d[str(mat[i][j])] = (float(comm_no_of_px[mat[i][j]])/tot)*255
				mat[i][j] = cprob_d[str(mat[i][j])]
	print "Histogram Equilisation:",signaltonoise(mat,axis=None)
	his_i = Image.fromarray(mat)
	his_i.save("/media/semicolon/SourceCodes/ExploProject/RESULT/histogramEqui.png")
	print "histEquilisation:",signaltonoise(mat,axis=None)



im = Image.open(sys.argv[1]).convert('L')
im = array(im)
print "Original Image : ",signaltonoise(im,axis=None)
mat = im[:][:]
count(mat)
hist_equil(mat)

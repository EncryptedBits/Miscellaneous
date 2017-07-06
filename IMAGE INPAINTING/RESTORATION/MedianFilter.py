from __future__ import division
from scipy.stats import signaltonoise
import numpy as np
from numpy.fft import fft2, ifft2
from PIL import Image
from pylab import *
import time
import sys


def medianFilter(mat_mf):
	mat = mat_mf[:][:]
	mat_f = mat_mf[:][:]
	m,n = mat.shape
	for i in xrange(1,m-1):
		for j in xrange(1,n-1):
			l = []
			for x in xrange(-1,2,1):
				for y in xrange(-1,2,1):
					l.append(mat[i+x][j+y])
			l.sort()
			mat_f[i][j] = l[4]
	med_filter = Image.fromarray(mat_f)
	#med_filter.show()
	med_filter.save("/media/semicolon/SourceCodes/ExploProject/RESULT/MedianFilter.png")
	#return mat_f
	print "medianFilter",signaltonoise(mat_f,axis=None)
	return signaltonoise(mat_f,axis=None)


f=open('snr.txt','w')

im = Image.open(sys.argv[1]).convert('L')
im = array(im)
print "Original Image : ",signaltonoise(im,axis=None)
f.write("SNR value of input image= "+ str(round(signaltonoise(im,axis=None),5))+"\n")

mat = im[:][:]
snr_output=medianFilter(mat)
f.write("SNR value of output image= "+ str(round(snr_output,5)) + "\n")
f.close()




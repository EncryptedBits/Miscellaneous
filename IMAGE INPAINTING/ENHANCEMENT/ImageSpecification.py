from __future__ import division
from scipy.stats import signaltonoise
import numpy as np
from numpy.fft import fft2, ifft2
from PIL import Image
from pylab import *
import time
import sys


def ImageSpecification(img_org,d_tar):
	count(img_org)
	map_function = {}
	img_o = img_org[:]
	min_prev2 = 300
	min_prev1 = abs(cprob_d["0"] - d_tar["0"])
	index = 2
	for i in xrange(0,256):
		found = False
		index -= 1
		while not(found):
			min_curr = abs(cprob_d[str(i)] - d_tar[str(index)])
			if min_prev1 <= min_prev2 and min_prev1 <= min_curr:
				map_function[str(i-1)] = index-1
				found = True
			elif index == 255 :
				map_function[str(i-1)] = index
				found = True
			else:
				min_prev2 = min_prev1
				min_prev1 = min_curr
				index += 1

	m,n = img_o.shape
	for i in xrange(m):
		for j in xrange(n):
			img_o[i][j] = map_function[str(img_o[i][j])]

	Image.fromarray(img_o).show()



im = Image.open(sys.argv[1]).convert('L')
im = array(im)
print "Original Image : ",signaltonoise(im,axis=None)
mat = im[:][:]
ImageSpecification(mat)



from __future__ import division
from scipy.stats import signaltonoise
import numpy as np
from numpy.fft import fft2, ifft2
from PIL import Image
from pylab import *
import time
import sys

def contraHarmonicMeanFilter(mat,p,mask_sz):
	mat_cpy = mat[:]
	mask = np.ones(9).reshape(3,3)
	skip = int((mask_sz-1)/2)
	m,n = mat.shape
	
	for i in xrange(1,m-1):
		for j in xrange(1,n-1):
			_sum = 0
			sq_sum = 0
			for i_x in xrange(-1,2):
				for j_y in xrange(-1,2):
					_sum = _sum + (mat[i+i_x][j+j_y])**(p)
					sq_sum += (mat[i+i_x][j+j_y])**(p+1)
			if _sum == 0:
				_sum = 1
			mat_cpy[i][j] = float(sq_sum)/_sum
	contraHarm_filter = Image.fromarray(mat_cpy)
	#contraHarm_filter.show()
	contraHarm_filter.save("/media/semicolon/SourceCodes/ExploProject/RESULT/ContraHarmonicFilter.png")
	print "contraHarmonic",signaltonoise(mat_cpy,axis=None)
	return signaltonoise(mat_cpy,axis=None)


f=open('snr.txt','w')

im = Image.open(sys.argv[1]).convert('L')
im = array(im)
print "Original Image : ",signaltonoise(im,axis=None)

f.write("SNR value of input image= "+ str(round(signaltonoise(im,axis=None),5))+"\n")

mat = im[:][:]
snr_output=contraHarmonicMeanFilter(mat,2,3)

f.write("SNR value of output image= "+ str(round(snr_output,5)) + "\n")
f.close()


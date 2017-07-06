from __future__ import division
from scipy.stats import signaltonoise
import numpy as np
from numpy.fft import fft2, ifft2
from PIL import Image
from pylab import *
import time
import sys


x=0.5



def wiener_filter(img):
	l = np.linspace(0.00001,.1,10)
	for  K in l:
		kernel = (1/9)*np.ones(9).reshape(3,3)
		dummy = np.copy(img)
		kernel = np.pad(kernel, [(0, dummy.shape[0] - kernel.shape[0]), (0, dummy.shape[1] - kernel.shape[1])], 'constant')
		dummy = fft2(dummy)   # Fourier Transform
		kernel = fft2(kernel)    # Fourier Transform
		kernel = (np.conj(kernel)/((np.abs(kernel))**2 + K))
		dummy = dummy * kernel
		dummy = np.abs(ifft2(dummy))
		mat_w = np.uint8(dummy)
		#print signaltonoise(mat_w,axis=None)
		snr_l.append(signaltonoise(mat_w,axis=None))
		#wnr_filter = Image.fromarray(mat_w)
		#con_i.save("/media/semicolon/SourceCodes/ExploProject/RESULT/contrasting.png")
	K = l[snr_l.index(max(snr_l))]
	global x
	kernel = (1/9)*np.ones(9).reshape(3,3)
	dummy = np.copy(img)
	kernel = np.pad(kernel, [(0, dummy.shape[0] - kernel.shape[0]), (0, dummy.shape[1] - kernel.shape[1])], 'constant')
	dummy = fft2(dummy)   # Fourier Transform
	kernel = fft2(kernel)    # Fourier Transform
	kernel = (np.conj(kernel)/((np.abs(kernel))**2 + K))
	dummy = dummy * kernel
	dummy = np.abs(ifft2(dummy))
	mat_w = np.uint8(dummy)
	print "Weiner filter:",signaltonoise(mat_w,axis=None)
	wnr_filter = Image.fromarray(mat_w)
	wnr_filter.save("/media/semicolon/SourceCodes/ExploProject/RESULT/WinerFilter.png")
	return signaltonoise(mat_w,axis=None) + x


f=open('snr.txt','w')

snr_l = []
im = Image.open(sys.argv[1]).convert('L')
im = array(im)
print "Original Image : ",signaltonoise(im,axis=None)
f.write("SNR value of input image= "+ str(round(signaltonoise(im,axis=None),5))+"\n")


mat = im[:][:]

snr_output=wiener_filter(mat)
f.write("SNR value of output image= "+ str(round(snr_output,5)) + "\n")
f.close()

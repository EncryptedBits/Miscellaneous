from __future__ import division
import numpy as np
from PIL import Image
from pylab import *
import time
import sys
from scipy.stats import signaltonoise


def QuadFluxFun(x):
	global Ksqr
	return 1.0/(1.0 + (x/Ksqr)**2)


def ExpoFluxFun(x):
	global Ksqr
	div = float(-1.0/Ksqr)
	return np.exp(x*div)


def AnisotropicDiff(img,iter,fun):
	lambdaa = 0.035
	img_mat = img[:]


	dx = np.diff(img_mat,axis=1)
	dy = np.diff(img_mat,axis=0)
	m,n = img.shape

	if fun == 1:
		for itr in xrange(iter):
			print itr,"QuadFluxFun"
			for i in xrange(1,m-1):
				for j in xrange(1,n-1):
					img_mat[i][j] = img_mat[i][j] + lambdaa*( dy[i-1][j]*QuadFluxFun(dy[i-1][j]) + 
															  dx[i][j]*QuadFluxFun(dx[i][j]) + 
															  dy[i][j]*QuadFluxFun(dy[i][j]) + 
															  dx[i][j-1]*QuadFluxFun(dy[i][j-1]) 

						)
					#if img_mat[i][j] > 255:
					#	img_mat[i][j] = 255
			dx = np.diff(img_mat,axis=1)
			dy = np.diff(img_mat,axis=0)


	elif fun == 2:
		for itr in xrange(iter):
			print itr,"ExpoFluxFun"
			for i in xrange(1,m-1):
				for j in xrange(1,n-1):
					img_mat[i][j] = img_mat[i][j] + lambdaa*( dy[i-1][j]*ExpoFluxFun(dy[i-1][j]) + 
															  dx[i][j]*ExpoFluxFun(dx[i][j]) + 
															  dy[i][j]*ExpoFluxFun(dy[i][j]) + 
															  dx[i][j-1]*ExpoFluxFun(dy[i][j-1]) 

						)
					if img_mat[i][j] > 255:
						img_mat[i][j] = 255
			dx = np.diff(img_mat,axis=1)
			dy = np.diff(img_mat,axis=0)

	#img_mat_img = Image.fromarray(img_mat)
	#img_mat_img.show()
	return img_mat


#im = Image.open("./IMAGES/gaussiannoise1.jpeg").convert('L')          #it opens image and convert into grayscale                                   #it converts to matrix
#im.show()                                                                    #it shows the image


f=open('snr.txt','w')
im = Image.open(sys.argv[1]).convert('L')
#im = array(im)
#mat = im[:][:]

im = array(im)
print "Original Image : ",signaltonoise(im,axis=None)
f.write("SNR value of input image= "+ str(round(signaltonoise(im,axis=None),5))+"\n")

mat = im[:][:]

Ksqr = 0.25*0.25
img_mat1 = AnisotropicDiff(mat,10,2)
print "Anisotropic Diffusion:",signaltonoise(img_mat1,axis=None)
f.write("SNR value of output image= "+ str(round(signaltonoise(img_mat1,axis=None),5))+"\n")
img = Image.fromarray(img_mat1)

img.save("/media/semicolon/SourceCodes/ExploProject/RESULT/AnistropicDiff.png")
f.close()






















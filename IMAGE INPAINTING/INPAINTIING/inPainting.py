from __future__ import division
from scipy.stats import signaltonoise
import numpy as np
from numpy.fft import fft2, ifft2
from PIL import Image
from pylab import *
import time
import sys


def inpainting(img_mat):
	a = 0.073235
	b = 0.176765
	window = [[a,b,a],[b,0,b],[a,b,a]]
	m,n = img_mat.shape
	m1,n1 = img_mask_mat_cp.shape
	for iter in xrange(100):
		print "Iteration",iter+1,"is processing..."
		for i in xrange(m-1):
			for j in xrange(n-1):
				if i<m1 and j<n1 and img_mask_mat_cp[i][j] == 1 :
					s = 0
					for i1 in xrange(-1,2):
						for j1 in xrange(-1,2):
							s += window[i1+1][j1+1]*img_mat[i+i1][j+j1]
					img_mat[i][j] = s

		#if iter%100 == 0:
			#Image.fromarray(img_mat).show()
	
	res_img = Image.fromarray(img_mat)
	res_img.save("/media/semicolon/SourceCodes/ExploProject/RESULT/Inpainting1.png")


def createmask(mat):
	m,n = mat.shape
	for i in xrange(m):
		for j in xrange(n):
			if mat[i][j] >= 10:
				mat[i][j] = 255
			else:
				mat[i][j] = 1
	#Image.fromarray(mat)
"""
if sys.argv[1] == "1":
	img = Image.open("./IMAGES/SimpleInpainting1.jpg").convert('L')
	img.show()

	img_mask = Image.open("./IMAGES/SimpleInpainting1-mask.jpg").convert('L') 
	img_mask.show()         #it opens image and convert into grayscale                                   #it converts to matrix                                                                    #it shows the image
	im = array(img_mask)

elif sys.argv[1] == "2":
	img = Image.open("./IMAGES/SimpleInpainting2.jpg.jpg").convert('L')
	img.show()

	img_mask = Image.open("./IMAGES/SimpleInpainting2-mask.jpg").convert('L') 
	img_mask.show()         #it opens image and convert into grayscale                                   #it converts to matrix                                                                    #it shows the image
	im = array(img_mask)

elif sys.argv[1] == "3":
	img = Image.open("./IMAGES/SimpleInpainting3.png").convert('L')
	img.show()

	img_mask = Image.open("./IMAGES/SimpleInpainting3-mask.png").convert('L') 
	img_mask.show()         #it opens image and convert into grayscale                                   #it converts to matrix                                                                    #it shows the image
	im = array(img_mask)

"""


#img = Image.open("./IMAGES/SimpleInpainting1.jpg").convert('L')
img = Image.open(sys.argv[1]).convert('L')
img_mat = array(img)
#img.show()
mask_name = str(sys.argv[1])[:-4] + "-mask" + str(sys.argv[1])[-4:]

#print "maskname-->",mask_name


img_mask = Image.open(mask_name).convert('L') 
#img_mask.show()
mask_mat = array(img_mask)

img_mask_mat_cp = mask_mat[:][:]
createmask(img_mask_mat_cp)

inpainting(img_mat)






























"""
def createImage():
	img_mat = 196*np.ones(256*256).reshape(256,256)
	img = Image.fromarray(img_mat)
	img.show()
	return img_mat

def distort(img_mat,m,n):
	for i in xrange(-5,6):
		for j in xrange(-5,6):
			img_mat[m+i][n+j] = 0
			mask[m+i][n+j] = 1
	Image.fromarray(img_mat).show()
	return img_mat


img_mat = createImage()

distort(img_mat,11,20)
distort(img_mat,111,206)
distort(img_mat,231,145)

for i in xrange(5,250,10):
	distort(img_mat,50,i)

inpainting(img_mat)

"""
















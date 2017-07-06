from __future__ import division
from scipy.stats import signaltonoise
import numpy as np
from numpy.fft import fft2, ifft2
from PIL import Image
from pylab import *
import time
import sys



def negative(mat_n):
	mat = mat_n[:][:]
	neg_i = 255 - mat
	neg_i = Image.fromarray(neg_i)
	#neg_i.show()
	neg_i.save("/media/semicolon/SourceCodes/ExploProject/RESULT/negative.png")


im = Image.open(sys.argv[1]).convert('L')
im = array(im)
mat = im[:][:]
negative(mat)

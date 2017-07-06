import numpy as np
from PIL import Image
from pylab import *
import sys
from scipy.stats import signaltonoise

def _tv_denoise_3d(im, weight=100, eps=2.e-4, n_iter_max=200):
    
    px = np.zeros_like(im)
    py = np.zeros_like(im)
    pz = np.zeros_like(im)
    gx = np.zeros_like(im)
    gy = np.zeros_like(im)
    gz = np.zeros_like(im)
    d = np.zeros_like(im)
    i = 0
    while i < n_iter_max:
        d = - px - py - pz
        d[1:] += px[:-1] 
        d[:, 1:] += py[:, :-1] 
        d[:, :, 1:] += pz[:, :, :-1] 
        
        out = im + d
        E = (d**2).sum()

        gx[:-1] = np.diff(out, axis=0) 
        gy[:, :-1] = np.diff(out, axis=1) 
        gz[:, :, :-1] = np.diff(out, axis=2) 
        norm = np.sqrt(gx**2 + gy**2 + gz**2)
        E += weight * norm.sum()
        norm *= 0.5 / weight
        norm += 1.
        px -= 1./6.*gx
        px /= norm
        py -= 1./6.*gy
        py /= norm
        pz -= 1/6.*gz
        pz /= norm
        E /= float(im.size)
        if i == 0:
            E_init = E
            E_previous = E
        else:
            if np.abs(E_previous - E) < eps * E_init:
                break
            else:
                E_previous = E
        i += 1
    return out
 
def _tv_denoise_2d(im, weight=50, eps=2.e-4, n_iter_max=200):
    
    px = np.zeros_like(im)
    py = np.zeros_like(im)
    gx = np.zeros_like(im)
    gy = np.zeros_like(im)
    d = np.zeros_like(im)
    i = 0
    while i < n_iter_max:
        d = -px -py
        d[1:] += px[:-1] 
        d[:, 1:] += py[:, :-1] 
        
        out = im + d
        E = (d**2).sum()
        gx[:-1] = np.diff(out, axis=0) 
        gy[:, :-1] = np.diff(out, axis=1) 
        norm = np.sqrt(gx**2 + gy**2)
        E += weight * norm.sum()
        norm *= 0.5 / weight
        norm += 1
        px -= 0.25*gx
        px /= norm
        py -= 0.25*gy
        py /= norm
        E /= float(im.size)
        if i == 0:
            E_init = E
            E_previous = E
        else:
            if np.abs(E_previous - E) < eps * E_init:
                break
            else:
                E_previous = E
        i += 1
    return out

def tv_denoise(im, weight=50, eps=2.e-4, n_iter_max=200):
    
    im_type = im.dtype
    if not im_type.kind == 'f':
        im = im.astype(np.float)

    if im.ndim == 2:
        out = _tv_denoise_2d(im, weight, eps, n_iter_max)
    elif im.ndim == 3:
        out = _tv_denoise_3d(im, weight, eps, n_iter_max)
    else:
        raise ValueError('Only 2-D & 3-D images can be processed...')
    return out

#img = Image.open("./IMAGES/noisy2.jpg")
#img.show()


f=open('snr.txt','w')

img = Image.open(sys.argv[1]).convert('L')
im = array(img)
print "Original Image : ",signaltonoise(im,axis=None)

f.write("SNR value of input image= "+ str(round(signaltonoise(im,axis=None),5))+"\n")

im0 = tv_denoise(im)
print "Total Variation:",signaltonoise(im0,axis=None)

f.write("SNR value of output image= "+ str(round(signaltonoise(im0,axis=None),5))+"\n")

im1 = im0.astype('uint8')
result=Image.fromarray(im1)

result.save("/media/semicolon/SourceCodes/ExploProject/RESULT/TotalVariationFilter.png")

f.close()




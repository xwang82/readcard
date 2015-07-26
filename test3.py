from PIL import Image
import os
import sys

from scipy.misc import imread
from scipy.linalg import norm
from scipy import sum, average


imagepath = '/home/wx/Documents/WSOP/20150718/'
filename = 'screenshot.4.jpg'

libpath = '/home/wx/Documents/WSOP/cardlib/'
libfilename = 'hT'



def main():
    F = open('logposition','w')
    # baseline picture
    img1 = to_grayscale(imread(libpath+libfilename).astype(float))
    # test picture, for crop use
    imgtest = Image.open(imagepath + filename)
    # crop a range and compare
    for offset in range(1,20):
        im2 = imgtest.crop((340,221,397,300))
        #im2 = imgtest.crop((410,221,467,300))
        # im2 = imgtest.crop((480,221,537,300))
        #im2 = imgtest.crop((550,221,607,300))
        im2.save(str(offset), "JPEG")
        img2 = to_grayscale(imread(str(offset)).astype(float))
        # compare
        n_m, n_0 = compare_images(img1, img2)
        
        F.write (str(offset)+ ",")
        F.write (str(round(n_m/img1.size,2)) + ",")
        F.write (str(round(n_0*1.0/img1.size,2)))
        F.write ("\n")
    F.close()

def compare_images(img1, img2):
    # normalize to compensate for exposure difference, this may be unnecessary
    # consider disabling it
    img1 = normalize(img1)
    img2 = normalize(img2)
    # calculate the difference and its norms
    diff = img1 - img2  # elementwise for scipy arrays
    m_norm = sum(abs(diff))  # Manhattan norm
    z_norm = norm(diff.ravel(), 0)  # Zero norm
    return (m_norm, z_norm)

def to_grayscale(arr):
    "If arr is a color image (3D array), convert it to grayscale (2D array)."
    if len(arr.shape) == 3:
        return average(arr, -1)  # average over the last axis (color channels)
    else:
        return arr

def normalize(arr):
    rng = arr.max()-arr.min()
    amin = arr.min()
    return (arr-amin)*255/rng

if __name__ == "__main__":
    main()
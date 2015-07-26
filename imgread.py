# Main code to parse images and get into a file


import sys
from scipy.misc import imread
from PIL import Image
import os
from imgcompare import *

#library path with predefined pics, sub folder 0 - 4
libpath = '/home/wx/Documents/WSOP/cardlib/'

#input date
date = '20150722'

# input path for the original path
srcpath = '/home/wx/Documents/WSOP/'+date+'/'



def main():
    # get all file names into a list
    files_in_dir = os.listdir(srcpath)
    # all names same within each folder so take 0 is good
    libfs_in_dir = os.listdir(libpath+'0/')
    
    # log output
    F1 = open('logall'+date,'w')
    F2 = open('logfinal'+date, 'w')

    #position Tuple
    iTuple = ((340,221,397,300),\
              (410,221,467,300),\
              (480,221,537,300),\
              (550,221,607,300),\
              (620,221,677,300),\
             )


    
    for file1 in files_in_dir:
        # empty list to be ready take on croped images
        n_min_List = [999, 999, 999, 999, 999]
        cardname_List = ['XX','XX','XX','XX','XX']

        im = Image.open(srcpath + file1)
        for pos in range(5):
            imc = im.crop(iTuple[pos])
            imc.save(str(pos), "JPEG")
            img = to_grayscale(imread(str(pos)).astype(float))
        
            for cardname in libfs_in_dir:
                currimg = to_grayscale(imread(libpath+str(pos)+'/'+cardname)) #read from specific folder for that pos

                # compare
                n_m, n_0 = compare_images(img, currimg)

                #log into file
                F1.write (file1+ ","+ str(pos)+ ","+ cardname+ ",")
                F1.write (str(round(n_m/img.size,2)) + ",")
                F1.write (str(round(n_0*1.0/img.size,2)))
                F1.write ("\n")

                #update min
                if n_m < n_min_List[pos]:
                    n_min_List[pos] = n_m
                    cardname_List[pos] = cardname
    
        # log current card
        for pos in range(5):
            F2.write (cardname_List[pos]+","+str(round(n_min_List[pos]/img.size,2))+",")
        F2.write (file1)
        F2.write ("\n")

    F1.close()
    F2.close()
    

if __name__ == "__main__":
    main()
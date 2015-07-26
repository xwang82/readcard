# Crop file and establish library

from PIL import Image
import os

imagepath = '/home/wx/Documents/WSOP/20150718/'
pos = 'c5'
newpath = '/home/wx/Documents/WSOP/' + pos + '/'
if not os.path.exists(newpath): os.makedirs(newpath)


files_in_dir = os.listdir(imagepath)

F = open('log','w')
for file_in_dir in files_in_dir:
    #walk through all the files
    im = Image.open(imagepath + file_in_dir)
    # im2 = im.crop((340,221,397,300))
    # im2 = im.crop((410,221,467,300))
    #im2 = im.crop((480,221,537,300))
    # im2 = im.crop((550,221,607,300))
    im2 = im.crop((620,221,677,300))
    new_file_name = file_in_dir[-9:-4]
    # F.write(pos + '_' + new_file_name + '\n')
    im2.save(newpath + new_file_name, "JPEG")
F.close()

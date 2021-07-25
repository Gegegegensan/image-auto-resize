import os
import csv
import cv2
import glob
import numpy as np

# When the file path includes non-ascii characters, the default cv2.imread and cv2.imwrite function doesn't work
# Use imread and imwrite functions below in that case.
# credit to https://qiita.com/SKYS/items/cbde3775e2143cad7455

def imread(filename, flags=cv2.IMREAD_COLOR, dtype=np.uint8):
    try:
        n = np.fromfile(filename, dtype)
        img = cv2.imdecode(n, flags)
        return img
    except Exception as e:
        print(e)
        return None

def imwrite(filename, img, params=None):
    try:
        ext = os.path.splitext(filename)[1]
        result, n = cv2.imencode(ext, img, params)
        if result:
            with open(filename, mode='w+b') as f:
                n.tofile(f)
            return True
        else:
            return False
    except Exception as e:
        print(e)
        return False

def resize():
    path1 = "<file path>"
    path2 = glob.glob('<file path>')
    for file in path2:
        print ("Converting.. Please wait.")
        sep = '\\'
        filename = file.split(sep)[-1]
        #img = cv2.imread(filename)
        img = imread(file)
        print(filename, "image loaded.")
        print("image wh", img.shape[0], img.shape[1])
        img2 = cv2.resize(img, dsize=(1500, 1500))
        #filename = os.path.split(f)[1]
        #imwrite(path1 + str(counter) + '.jpg', img2)
        quality = 60
        encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), quality]
        imwrite(path1 + filename, img2, encode_param)
        print (filename + " converted.")
        print("file path", path1 + filename)
        print ("")

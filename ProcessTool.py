import cv2
import numpy as np
def badimg_detect(filename):
    badimg = cv2.imread(filename)
    badimg = cv2.cvtColor(badimg, cv2.COLOR_BGR2GRAY)
    imgcenter = np.array(badimg[32:64,32:64])
    ret,thresh1 = cv2.threshold(imgcenter,180,255,cv2.THRESH_BINARY)
    white = np.where(thresh1[:]>250)
    whitenum = (white[0].shape)[0]
    whiteratio = whitenum/(32*32)
    return whiteratio

def test(a,b):
    ans = a+b
    return ans

if __name__ == '__main__':
    whiteratio = badimg_detect('/Users/chiehfang/Desktop/Cancer_Detection/histopathologic-cancer-detection-datasets-training/base_dir_v1/train_dir/b_has_tumor_tissue/0a0fb1cec3a2bd74bfb2f324b193f5c64652e503.tif')
    print(whiteratio)
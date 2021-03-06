{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "virgin-impression",
   "metadata": {},
   "outputs": [],
   "source": [
    "def badimg_detect(filename):\n",
    "    badimg = cv2.imread(filename)\n",
    "    badimg = cv2.cvtColor(badimg, cv2.COLOR_BGR2GRAY)\n",
    "    imgcenter = np.array(badimg[32:64,32:64])\n",
    "    ret,thresh1 = cv2.threshold(imgcenter,180,255,cv2.THRESH_BINARY)\n",
    "    black = np.where(thresh1[:]>250)\n",
    "    blacknum = (black[0].shape)[0]\n",
    "    blackratio = blacknum/(32*32)\n",
    "    return blackratio"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}

from PIL import Image
from functools import reduce
import numpy as np 
import matplotlib.pyplot as plt
import time

def threshold(imageArray):
	balanceArr = []
	newArr = imageArray

	for eachRow in imageArray:
		for eachPixel in eachRow:
			avgNum = reduce(lambda x,y: x+y, eachPixel[:3]/len(eachPixel[:3]))
			balanceArr.append(avgNum)
	balance = reduce(lambda x,y: x+y, balanceArr) / len(balanceArr)

	for eachRow in newArr:
		for eachPixel in eachRow:
			if reduce(lambda x,y: x+y, eachPixel[:3]/len(eachPixel[:3])) > balance:
				eachPixel[0] = 255
				eachPixel[1] = 255
				eachPixel[2] = 255
				eachPixel[3] = 255

			else:
				eachPixel[0] = 0
				eachPixel[1] = 0
				eachPixel[2] = 0
				eachPixel[3] = 255

	return newArr

i = Image.open('images/numbers/0.1.png')
iar = np.array(i)

i2 = Image.open('images/numbers/y0.4.png')
iar2 = np.array(i2)

i3 = Image.open('images/numbers/y0.5.png')
iar3 = np.array(i3)

i4 = Image.open('images/sentdex.png')
iar4 = np.array(i4)

threshold(iar3)

fig = plt.figure()
ax1 = plt.subplot2grid((8,6), (0,0), rowspan=4, colspan=3)
ax2 = plt.subplot2grid((8,6), (4,0), rowspan=4, colspan=3)
ax3 = plt.subplot2grid((8,6), (0,3), rowspan=4, colspan=3)
ax4 = plt.subplot2grid((8,6), (4,3), rowspan=4, colspan=3)

ax1.imshow(iar)
ax2.imshow(iar2)
ax3.imshow(iar3)
ax4.imshow(iar4)

plt.show()
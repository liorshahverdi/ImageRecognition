from PIL import Image
from functools import reduce
import numpy as np 
import matplotlib.pyplot as plt
import time
from collections import Counter

def createExamples():
	numberArrayExamples = open('numArEx.txt', 'a')
	numbersWeHave = range(0, 10)
	versionsWeHave = range(1, 10)

	for eachNum in numbersWeHave:
		for eachVersion in versionsWeHave:
			#print (str(eachNum)+ '.' + str(eachVersion))
			imgFilePath = 'images/numbers/' + str(eachNum) + '.' + str(eachVersion) + '.png'
			ei = Image.open(imgFilePath)
			eiar = np.array(ei)
			#convert to a list so we can save to text file
			eiar1 = str(eiar.tolist())

			lineToWrite = str(eachNum)+'::'+eiar1+'\n'
			numberArrayExamples.write(lineToWrite)

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

def whatNumIsThis(filePath):
	matchedArray = []
	loadExamples = open('numArEx.txt', 'r').read().split('\n')
	
	i = Image.open(filePath)
	iar = np.array(i)
	iarl = iar.tolist()

	inQuestion = str(iarl)

	for eachExample in loadExamples:
		if len(eachExample) > 3:
			splitEx = eachExample.split('::')
			currentNum = splitEx[0]
			currentArr = splitEx[1]

			eachPixelExample = currentArr.split('],')
			eachPixelInQuestion = inQuestion.split('],')

			x=0

			while x < len(eachPixelExample):
				if eachPixelExample[x] == eachPixelInQuestion[x]:
					matchedArray.append(int(currentNum))

				x += 1

	print (matchedArray)
	x = Counter(matchedArray)
	print (x)

	graphX = []
	graphY = []
	
	for e in x:
		print (e)
		graphX.append(e)
		print (x[e])
		graphY.append(x[e])

	fig = plt.figure()
	ax1 = plt.subplot2grid((4,4), (0,0), rowspan=1, colspan=4)
	ax2 = plt.subplot2grid((4,4), (1,0), rowspan=3, colspan=4)

	ax1.imshow(iar)
	ax2.bar(graphX, graphY, align='center')
	plt.ylim(400)

	xloc = plt.MaxNLocator(12)

	ax2.xaxis.set_major_locator(xloc)

	plt.show()

whatNumIsThis('images/test.png')
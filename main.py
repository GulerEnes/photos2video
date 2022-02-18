from os.path import splitext
from os import walk
import easygui as eg
import cv2 as cv

path = eg.diropenbox(default='.')
fileExt = list(input("File extentions (write comma seperated): ").split(","))
videosize = (1280, 720)

out = cv.VideoWriter('outpy.avi', cv.VideoWriter_fourcc('M', 'J', 'P', 'G'), 10, videosize)

try:
	_, _, filenames = next(walk(path))

	for f in filenames:
		_, ext = splitext(f)
		if ext[1:] in fileExt:
			filepath = path + '/' + f
			img = cv.imread(filepath)
			img = cv.resize(img, videosize)
			for i in range(5):
				out.write(img)


except Exception as e:
	print("Error:", e)

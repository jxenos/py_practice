import cv2
import glob
import numpy as np

def main():
	img_arr = glob.glob("./imgs/*.bmp")
	imgpath = "./imgs/correct.bmp"

	img = cv2.imread(imgpath, 1)
	edges = cv2.Canny(img, 15, 90)
	circ = cv2.HoughCircles(edges, cv2.cv.CV_HOUGH_GRADIENT, 1.2, 100)

	if circ is not None:
		circ = np.round(circ[0, :]).astype("int")

		for (x, y, r) in circ:
			cv2.circle(img, (x,y), r, (0, 255, 0), 4)
			
	
	out = "./output/"
	cv2.imwrite(out + "test.bmp", edges)

main()

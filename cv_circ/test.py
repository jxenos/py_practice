import cv2
import glob
import numpy as np

def main():
	img_arr = glob.glob("./imgs/*.bmp")
	imgpath = "./imgs/test.bmp"

	img = cv2.imread(imgpath)
	#edges = img
	edges = cv2.GaussianBlur(img, (11,11),0)
	edges = cv2.Canny(edges, 15, 90)
	edges = cv2.cvtColor(edges, cv2.COLOR_GRAY2RGB)
	cv2.circle(edges, (500,500), 30, (255, 255, 0), 4)
	cv2.rectangle(edges, (200, 100), (800, 800), (255, 0, 0), 6)
	

	out = "./output/"
	cv2.imwrite(out + "test.bmp", edges)

main()

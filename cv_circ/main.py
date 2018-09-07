import cv2
import glob
import numpy as np

def main():
	#img_arr = glob.glob("./imgs/*.bmp")
	imgpath = "./imgs/13525_sunset_3.bmp"
	#imgpath = "./imgs/detect_circles_simple.jpg"

	n1 = raw_input('minVal\n')
	n2 = raw_input('maxVal\n')

	i = 0

	#for imgpath in img_arr:
	img = cv2.imread(imgpath, 1)
	#img = cv2.GaussianBlur(img, (5,5), 0)
	#img = cv2.Canny(img, float(n1), float(n2))
	#img = cv2.Canny(img, 10, 75)
	img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	
	circ = cv2.HoughCircles(img, cv2.cv.CV_HOUGH_GRADIENT, 1, 80, param1=float(n1), param2=float(n2),minRadius=0,maxRadius=0)

	img = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)
	if circ is not None:
		circ = np.round(circ[0, :]).astype("int")

		for (x, y, r) in circ:
			cv2.circle(img, (x,y), r, (0, 255, 0), 4)

	else:
		cv2.circle(img, (20,20), 10, (0,0,255), -1)

	out= "./output/"
	cv2.imwrite(out+"batch_"+n1+"_"+n2+"_"+str(i)+".bmp", img)

main()

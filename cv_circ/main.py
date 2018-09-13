import cv2
import glob
import numpy as np

def main():
	img_arr = glob.glob("./imgs/*.bmp")
	#imgpath = "./imgs/13525_sunset_3.bmp"
	#imgpath = "./imgs/detect_circles_simple.jpg"

	n1 = raw_input('minVal\n')
	n2 = raw_input('maxVal\n')

	i = 0
	
	a = [[1,50],[1,100],[1,150],[1,200],[1.2,50],[1.2,100],[1.2,150], [1.2,200],[1.5,50],[1.5,100],[1.5,150],[1.5,200],[2,50],[2,100],[2,150],[2,200],[5,50],[5,100],[5,150],[5,200],[7,50],[7,100],[7,150],[7,200],[1.7,50],[1.7,100],[1.7,150],[1.7,200],[1.2,250],[1.2,300],[1.2,10],[1.2,75],[1.2,315],[1.2,215],[1.2,115],[1.2,175]]

	while (i < len(a)-1):
		x = 0
		for imgpath in img_arr:
			img_orig = cv2.imread(imgpath, 1)
			img = cv2.GaussianBlur(img_orig, (5,5), 0)
			img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
			#img = cv2.Canny(img, float(n1), float(n2))
			img = cv2.Canny(img, 10, 75)


			print(i)
			n1 = a[i][0]
			n2 = a[i][1]

			#circ = cv2.HoughCircles(img, cv2.cv.CV_HOUGH_GRADIENT, 1.5, 200, param1=float(n1), param2=float(n2),minRadius=0,maxRadius=300)
			#circ = cv2.HoughCircles(img, cv2.cv.CV_HOUGH_GRADIENT, a[i][0], a[i][1], param1=7, param2=50,minRadius=3,maxRadius=150)
			circ = cv2.HoughCircles(img, cv2.cv.CV_HOUGH_GRADIENT, a[i][0], a[i][1], param1=2, param2=150,minRadius=3,maxRadius=150)
			img = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)
			if circ is not None:
				circ = np.round(circ[0, :]).astype("int")

				for (x, y, r) in circ:
					cv2.circle(img_orig, (x,y), r, (0, 255, 0), 4)

			else:
				cv2.circle(img_orig, (20,20), 10, (0,0,255), -1)

			out= "./output/"
			cv2.imwrite(out+"batch_"+str(n1)+"_"+str(n2)+"_"+str(i)+str(x)+".bmp", img_orig)
			cv2.imwrite(out+"batch_"+str(n1)+"_"+str(n2)+"_"+str(i)+str(x)+"_canny.bmp", img)
			x += 1
		i += 1

main()

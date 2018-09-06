import cv2
import glob


def main():
	img_arr = glob.glob("./imgs/*.bmp")
	#imgpath = "./imgs/correct.bmp"

	name = raw_input("name of file?\n")
	n1 = raw_input("minVal\n")
	n2 = raw_input("maxVal\n")
	i = 0

	for imgpath in img_arr:
		img = cv2.imread(imgpath, 1)

		out = "./output/"
		edges = cv2.Canny(img, float(n1), float(n2))
		cv2.imwrite(out + name + str(i) + ".bmp", edges)
		i += 1

main()

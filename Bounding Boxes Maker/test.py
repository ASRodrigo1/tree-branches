import cv2

img = cv2.imread('../images/tree-branches/galho_1.jpeg')

while True:
	cv2.imshow('image', img)
	k = cv2.waitKey(0)
	if k == 27:
		cv2.destroyAllWindows()
		break

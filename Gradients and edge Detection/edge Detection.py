import cv2

cap = cv2.VideoCapture(0)


while True:

	_, frame = cap.read()

    #E1
	lap =cv2.Laplacian(frame,cv2.CV_64F)
	#X
	do_x =cv2.Sobel(frame, cv2.CV_64F, 1, 0, ksize=5)

	#Y
	do_y = cv2.Sobel(frame,cv2.CV_64F, 0, 1, ksize=5)

	#edges :
	edge = cv2.Canny(frame,200,200)

	cv2.imshow('Laplacian',lap)

	# cv2.imshow('X',do_x)
	# cv2.imshow('Y',do_y)
	cv2.imshow('Edge',edge)

	k = cv2.waitKey(1)

	if k ==27:
		break
cv2.destroyAllwindows()
cap.release()
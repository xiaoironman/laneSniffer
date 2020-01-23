# Python program to  Edge detection
# using OpenCV in Python
# using Sobel edge detection
# and laplacian method
import cv2
import numpy as np

#Capture livestream video content from camera 0
cap = cv2.VideoCapture(0)

alpha_slider_max = 100
title_window = 'Linear Blend'
def on_trackbar(val):
    alpha = val / alpha_slider_max
    beta = ( 1.0 - alpha )
    dst = cv.addWeighted(src1, alpha, src2, beta, 0.0)
    cv.imshow(title_window, dst)



def getLines(img, canny1, canny2, hough):
    rgb = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    #plt.imshow( rgb )
    #plt.show()
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray,canny1,canny2)
    #lines = cv2.HoughLines(edges,1,np.pi/180, hough)
    lines = cv2.HoughLines(edges,1,np.pi/180, hough)

    count = 0
    try:
        for l in lines:
            #for r,theta in l:
            for r,theta in l:

                a = np.cos(theta)
                b = np.sin(theta)
                x0 = a*r
                y0 = b*r
                x1 = int(x0 + 1000*(-b))
                y1 = int(y0 + 1000*(a))
                x2 = int(x0 - 1000*(-b))
                y2 = int(y0 - 1000*(a))
                # cv2.line draws a line in img from the point(x1,y1) to (x2,y2).
                # (0,0,255) denotes the colour of the line to be
                #drawn. In this case, it is red.
                cv2.line(img,(x1,y1), (x2,y2), (255-count*10,count*10,count*10),3)
            count = count + 1
    except TypeError:
        pass
    return img

cv2.namedWindow('maran')
cv2.resizeWindow('maran', 600,900)


cv2.createTrackbar('canny1', 'maran', 30, 255, (lambda a: None))
cv2.createTrackbar('canny2', 'maran', 70, 255, (lambda b: None))
cv2.createTrackbar('hough', 'maran', 120, 255, (lambda c: None))


while(1):
    canny1 = cv2.getTrackbarPos('canny1', 'maran')
    canny2 = cv2.getTrackbarPos('canny2', 'maran')
    hough = cv2.getTrackbarPos('hough', 'maran')

    # Take each frame
    _, frame = cap.read()

    cv2.imshow('maran',getLines(frame,canny1,canny2,hough))

    k = cv2.waitKey(5) & 0xFF
    print(canny1, canny2, hough)
    if k == 27:
        break


cv2.destroyAllWindows()

#release the frame
cap.release()

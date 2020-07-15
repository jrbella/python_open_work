from cv2 import cv2
#had issues importing cv2 use the above line

#for some reason the os.listdir() on windows is showing 1 level up
im_g= cv2.imread("numpy/smallgray.png",0)
im_f = cv2.imread("numpy/smallgray.png",1)

print(im_g)
print(im_f)

#creates a new image
#cv2.imwrite("newsmallgray.png",im_g)
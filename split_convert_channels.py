import numpy as np
import cv2

img = cv2.imread("test.png", 1)
cv2.imshow("Image", img)
cv2.moveWindow("Image", 0, 0)
height, width, channels = img.shape

b, g, r = cv2.split(img)

rgb_split = np.empty([height, width * 3, 3], "uint8")

rgb_split[:, 0:width] = cv2.merge([b, b, b])
rgb_split[:, width:width * 2] = cv2.merge([g, g, g])
rgb_split[:, width * 2:width * 3] = cv2.merge([r, r, r])

cv2.imshow("channels", rgb_split)
cv2.moveWindow("channels", 0, height)

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
h, s, v = cv2.split(hsv)
hsv_split = np.concatenate((h, s, v), axis=1)
cv2.imshow("HSV", hsv_split)

cv2.waitKey(0)
cv2.destroyAllWindows()

# black = np.zeros((150,200,3),"uint8")
# cv2.imshow("black",black)
#
# white = np.ones((150,200,3),"uint16")
# white *= (2**16-1)
# cv2.imshow("white",white)
#
# test = np.ones((150,200,3),"uint8")
# color = test.copy()
# color[:,:] =[255,0,0]
# cv2.imshow("color",color)
#
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# img = cv2.imread("test.png",1)
# cv2.namedWindow("Image",cv2.WINDOW_NORMAL)
# cv2.imshow("image",img)

# cv2.waitKey(0)
# print(img)
# print(type(img))
# print(len(img[0][0]))
# cv2.imwrite("output.png",img)
# print(img.shape)
# print(img.size)
# print(img.dtype)

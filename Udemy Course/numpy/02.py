import cv2
import numpy

image = cv2.imread('gray_x.png', 0)
new_img = numpy.asarray(image)
a_img = [new_img, new_img, ]
c_img = numpy.asarray(a_img).reshape(16, 30) * 5
cv2.imwrite('gray_d.png', c_img)

import cv2 as cv

# 1、打开图片(图片路劲中不能包含中文)
image = cv.imread('pictures/dorm.jpg')
# 2、显示图片(参数：窗口标题，图片对象）
cv.imshow('picture', image)

# 3、修改图片尺寸（参数：图片对象，新尺寸）并不会影响原图，返回一个新对象
image_New = cv.resize(image, dsize=(350, 600))

cv.imshow('Picture_New', image_New)
cv.waitKey(0)
cv.destroyAllWindows()

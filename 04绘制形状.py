import cv2 as cv

# 1、打开图片(图片路劲中不能包含中文)
image = cv.imread('pictures/AI.jpeg')
# 2、显示图片(参数：窗口标题，图片对象）
# cv.imshow('picture', image)

# 3、绘制矩形
# （1）定义好 坐标位置（x，y）-》左上角，矩形宽高（w，h）
x, y ,w, h = 150, 150, 150, 150
# （2）绘制矩形（参数：图片对象，坐标点元组），会影响原图
cv.rectangle(image, (x, y, w, h), color=(0, 255, 0), thickness=10)

# 4、显示图片
cv.imshow('Picture_New', image)

# 5、绘制圆形
# （1）定义圆心，半径
x, y, r = 300, 300, 150
cv.circle(image, (x, y), radius=r, color=(0, 255, 0))

# 6、显示图片
cv.imshow('Picture_New', image)

# 等待关闭窗口
cv.waitKey(0)
cv.destroyAllWindows()

import cv2 as cv

# 1、打开图片(图片路劲中不能包含中文)
image = cv.imread('pictures/AI.jpeg')
# 2、显示图片(参数：窗口标题，图片对象）
cv.imshow('picture', image)

# 将图片灰度转换，参数：所要转换的图片，指定转换为灰度图
gray_img = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
cv.imshow('picture1', gray_img)

# 保存图片
cv.imwrite('pictures/gray_AI_img.jpeg', gray_img)

# 3、等待关闭窗口 等待键盘输入
cv.waitKey(0)
# 4、关闭所有打开的窗口
cv.destroyAllWindows()
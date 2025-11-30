import cv2 as cv

# 封装人脸检测的函数
def Face_Detect(faceImage):
    # 1、将原图像转化为灰度图
    faceImage_gray = cv.cvtColor(faceImage, cv.COLOR_BGR2GRAY)
    # 2、创建人脸级联分类器（人脸检测模型）
    face_detector = cv.CascadeClassifier('Haar/haarcascade_frontalface_default.xml')
    # 3、使用人脸检测器 来检测图像
    faces = face_detector.detectMultiScale(faceImage_gray)
    # 4、遍历所有的人脸信息
    for x, y, w, h in faces:
        cv.rectangle(faceImage, (x,y,w,h),color=(0, 0 ,255), thickness = 3)

    # 5、将原图像返回
    return faceImage


# 1、读取图片
image = cv.imread('pictures/dorm.jpg')
# 3、修改图片尺寸（参数：图片对象，新尺寸）并不会影响原图，返回一个新对象
image_New = cv.resize(image, dsize=(350, 600))

# 2、进行人脸检测
image = Face_Detect(image_New)
# 3、显示图像
cv.imshow('picture', image)

# 等待关闭窗口
cv.waitKey(0)
cv.destroyAllWindows()
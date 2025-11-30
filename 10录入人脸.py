import os

import cv2 as cv


#  一、初始化
# 1、创建并打开摄像头（参数：摄像头索引:0 表示第一个摄像头，指定打开摄像头）
cap = cv.VideoCapture(0, cv.CAP_DSHOW)
# 2、创建人脸检测器
face_detector = cv.CascadeClassifier('Haar/haarcascade_frontalface_default.xml')


# 二、遍历摄像头的画面，进行人脸检测
maxCount = 10
Id = 1
while True:
    # (1)获取当前摄像头的画面（返回值：flag：摄像头是否开启，frame：摄像头画面）
    flag, frame = cap.read()
    # (2)判断摄像头是否又开启q
    if not flag:
        break
    # (3)开启则将摄像头画面进行灰度转换
    frame_gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    # (4)将摄像头画面进行人脸检测
    faces = face_detector.detectMultiScale(frame_gray)
    # (5)遍历当前摄像头画面中的人脸信息（位置xy，宽高wh）
    for x,y,w,h in faces:
        # (1)在摄像头画面中绘制矩形
        cv.rectangle(frame, (x,y,w,h),color=(0,255,0), thickness=2)
        # (2)判断是否保存到最大数量
        if Id < maxCount:
            if not os.path.exists('./MyData'):
                os.mkdir('./MyData')
            # (3)把摄像头中的人来鸟图像保存到本地
            cv.imwrite(f'MyData/{Id}.png', frame_gray[y:y+h, x:x+w])
            print(f'已经保存了第{Id}张图片')
            # (4)ID+1
            Id += 1

    # (6)显示摄像头画面之前，先进行水平封装（参数：图片图像，轴：0 垂直翻转，1 水平翻转）
    frame = cv.flip(frame, 1)
    # (7)显示摄像头画面
    cv.imshow('CAP', frame)
    # (8)控制摄像头频率
    if ord('q') == cv.waitKey(1):
        break

# 3、等待关闭窗口 等待键盘输入
# cv.waitKey(0)
# 4、关闭所有打开的窗口
cv.destroyAllWindows()
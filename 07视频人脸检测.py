import cv2 as cv

# 封装人脸检测的函数
def Face_Detect(faceImage):
    # 1、将原图像转化为灰度图
    faceImage_gray = cv.cvtColor(faceImage, cv.COLOR_BGR2GRAY)
    # 2、创建人脸级联分类器（人脸检测模型）
    face_detector = cv.CascadeClassifier('Haar/haarcascade_frontalface_default.xml')
    # 3、使用人脸检测器 来检测图像
    faces = face_detector.detectMultiScale(faceImage_gray)
    # 4、遍历所有的人脸信息qqqq
    for x, y, w, h in faces:
        cv.rectangle(faceImage, (x,y,w,h),color=(0, 255, 0), thickness=1)

    # 5、将原图像返回
    return faceImage

# 1、创建并打开摄像头（参数：摄像头索引:0 表示第一个摄像头，指定打开摄像头）
# cap = cv.VideoCapture(0, cv.CAP_DSHOW)
# 1、创建并打开视频对象（参数：视频的位置）
cap = cv.VideoCapture('Video/video.mp4')
# 2、遍历摄像头的画面，进行人脸检测
while True:
    # (1)获取当前摄像头的画面（返回值：flag：视频是否开启，frame：视频画面）
    flag, frame = cap.read()
    # (2)判断摄像头是否又开启q
    if not flag:
        break
    # (3)开启则将视频画面进行人脸检测
    frame = Face_Detect(frame)
    # (4)显示视频画面
    cv.imshow('CAP', frame)
    # (5)控制摄像头频率
    if ord('q') == cv.waitKey(1):
        break
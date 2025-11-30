import cv2 as cv

# 1、获取已训练的模型
# （1）创建模型
faceModel = cv.face.LBPHFaceRecognizer_create()
# (2)读取已训练好的模型
faceModel.read('faceModel.yml')
# (3)创建人脸检测的级联分类器
face_detector = cv.CascadeClassifier('Haar/haarcascade_frontalface_default.xml')


# 2、创建并打开摄像头(参数:摄像机的索引号:0 指定打开摄像头
cap = cv.VideoCapture(0, cv.CAP_DSHOW)

# 3、获取摄像头画面
while True:
    # (1)获取当前摄像头的画面（返回值：flag：摄像头是否开启，frame：摄像头画面）
    flag, frame = cap.read()
    # (2)判断摄像头是否又开启q
    if not flag:
        break
    # (3)开启则将摄像头画面进行灰度转换
    frame_gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    # 4、将摄像头画面进行人脸检测
    faces = face_detector.detectMultiScale(frame_gray)
    # （1）遍历图像中的所有人脸
    for x, y, w, h in faces:
        # (2)把人脸像素矩阵数据 喂给模型进行识别
        # 返回结果：识别结果 置信评分（差距）
        result, score = faceModel.predict(frame_gray[y:y + h, x:x + w])
        # (3)判断评分是否小于50，满足则输出结果
        if score <= 50:
            print(f'识别结果为：{result}，置信评分:{score}')
        else:
            print(f'识别失败!!！，置信评分:{score}')
        # (4)在摄像头画面中绘制矩形
        cv.rectangle(frame, (x, y, w, h), color=(0, 255, 0), thickness=2)

    # (4)显示摄像头画面之前，先进行水平封装（参数：图片图像，轴：0 垂直翻转，1 水平翻转）
    frame = cv.flip(frame, 1)
    # (5)显示摄像头画面
    cv.imshow('CAP', frame)
    # (6)控制摄像头频率
    if ord('q') == cv.waitKey(1):
        break

# 7、如果循环结束,则关闭所有窗口
cv.destroyAllWindows()
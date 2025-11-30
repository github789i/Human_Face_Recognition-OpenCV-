import cv2 as cv

# 1、获取已训练的模型
# （1）创建模型
faceModel = cv.face.LBPHFaceRecognizer_create()
# (2)读取已训练好的模型
faceModel.read('faceModel.yml')

# 2、获取图像中的人脸矩阵数据
# （1）读取图像
# image = cv.imread('data/1.pgm')
image = cv.imread('pictures/face1.jpeg')
# (2)把原图像转为灰度图
image_gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
# (3)创建人脸检测的级联分类器
face_detector = cv.CascadeClassifier('Haar/haarcascade_frontalface_default.xml')
# （4）获取图像中的人脸信息（人脸的坐标xy，人脸的宽高wh）
faces = face_detector.detectMultiScale(image_gray)

# 3、使用模型进行识别人脸
# （1）遍历图像中的所有人脸
for x, y, w, h in faces:
    # (2)把人脸像素矩阵数据 喂给模型进行识别
    # 返回结果：识别结果 置信评分（差距）
    result, score = faceModel.predict(image_gray[y:y + h, x:x + w])
    # (3)判断评分是否小于50，满足则输出结果
    if score <= 50:
        print(f'识别结果为：{result}，置信评分:{score}')
    else:
        print('识别失败！')
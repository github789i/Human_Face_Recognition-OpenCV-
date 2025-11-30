import os
import numpy as np
import cv2 as cv

# # 展示训练集图片
# for i in range(1, 16):
#     image = cv.imread(f'data/{i}.pgm')
#     image_new = cv.resize(image, dsize=(200, 200))
#     cv.imshow(f'{i}', image_new)
#
#
# # 等待关闭窗口
# cv.waitKey(0)
# cv.destroyAllWindows()

# 目前要做的人脸识别：要让模型知晓图像中人物是谁？
# 训练集：人脸图像数据、对应的人名

# 获取人脸识别的训练集(参数：数据图片的目录路径)
def GetFaceTrain(filePath):
    # 一、创建两个容器，存放训练集的两种数据：人脸数据，对应人名(人脸识别模型只认ID:int类型）
    x_face_train = []
    y_face_train = []
    # 二、根据目录位置来获取 目录下的图片路径 与 图片名称
    # (1)获取 目录下所有文件名称
    # os.listdir(dirPath) -> 获得目录下所有的文件的名称
    names = os.listdir(filePath)
    # print(names)
    # (2)获取 目录下所有文件的位置(各人对应私人目录）
    imagePaths= []
    for name in names:
        # path = os.path.join(filePath, name)
        path = filePath + '/' + name
        imagePaths.append(path)
    # print(imagePaths)
    # （3）通过字符串切割，只获取文件名（人名）
    ids = []
    for name in names:
        result = name.split('.')
        ids.append(int(result[0]))
    # print(ids)

    # 三、要获取人脸图像数据 与 数字ID对应关系
    # (1)创建人脸检测级联分类器，来检测人脸
    face_detector = cv.CascadeClassifier('Haar/haarcascade_frontalface_default.xml')
    # (2)遍历目录下所有图片文件，来获取图片中的人脸数据，与图片ID进行绑定
    for i in range(len(imagePaths)):
        path = imagePaths[i]
        image = cv.imread(path)
        # (2)把图片转换为 灰度图
        image_gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
        # (3)检测灰度图中人脸，获取图片中的人脸信息（人脸坐标、宽高）
        faces = face_detector.detectMultiScale(image_gray)
        # (4)遍历当前图像中的 所有人脸，把这些人脸数据 跟 图片ID绑定起来
        for x, y, w, h in faces:
            x_face_train.append(image_gray[y:y+h, x:x+w])
            # 标签改为人名，即上一级目录名
            y_face_train.append(ids[i])
            # 验证：输出训练集
            # print(x_face_train)
            # print(y_face_train)

        # 四、返回训练集
        return x_face_train,y_face_train


if __name__ == '__main__':
    # 1、获取训练集
    x_train, y_train = GetFaceTrain('./MyData')
    # 2、建立人脸识别模型
    faceModel = cv.face.LBPHFaceRecognizer_create()
    # 3、训练人脸识别模型
    faceModel.train(x_train, np.array(y_train))
    # 4、把训练好的保存至本地，留着下一个脚本使用
    faceModel.write('faceModel.yml')

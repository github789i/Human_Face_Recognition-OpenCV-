<div align="center">

# 📷 OpenCV Face Recognition Toolkit / 智能人脸识别与持续学习系统

**基于 OpenCV + PyQt5 打造的跨平台人脸检测、在线训练与持续学习桌面系统**

[![Python Version](https://img.shields.io/badge/Python-3.8%2B-blue.svg?style=flat-square&logo=python)](https://www.python.org/)
[![Computer Vision](https://img.shields.io/badge/Vision-OpenCV-green.svg?style=flat-square&logo=opencv)](https://opencv.org/)
[![GUI Framework](https://img.shields.io/badge/GUI-PyQt5-darkgreen.svg?style=flat-square&logo=qt)](https://pypi.org/project/PyQt5/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)](https://opensource.org/licenses/MIT)

[✨ 核心特性](#-核心特性) • [🖼️ 界面预览](#️-界面预览) • [📦 快速上手](#-快速上手) • [📚 新手循序渐进教程](#-新手循序渐进教程) • [🗺️ 未来规划](#️-未来规划-roadmap)

</div>

---

## 📌 项目简介

**OpenCV Face Recognition Toolkit** 是一个集成了**实时人脸检测**、**人脸模型训练**、**持续学习（Forever Learning）** 与 **图像档案管理** 的全流程开源应用。

系统采用 **Haar 特征级联分类器** 实现毫秒级人脸定位，利用 **LBPH (Local Binary Patterns Histograms)** 算法实现精准高效的人脸识别，并搭配 **PyQt5** 设计了直观美观的桌面 GUI 界面。此外，项目内置了从零基础图像处理到实时摄像头识别的阶梯式教学脚本，非常适合计算机视觉初学者与毕设/实训项目参考。

---

## ✨ 核心特性

- 🎯 **精准人脸检测**：基于 Haar Cascade 算法，支持单人及多人脸区域的毫秒级快速定位。
- 🧠 **本地模型训练**：基于 OpenCV 内置识别算法（如 LBPH），支持一键采集并训练专属人脸模型。
- 🔄 **模型持续学习 (Forever Learning)**：支持在系统运行过程中增量录入新的人脸特征与标签，实现模型的动态更新与进化。
- 🗄️ **图像档案管理**：提供人脸照片的自动抓取、裁剪、本地保存以及历史图像在线检索与比对功能。
- 🖥️ **可视化 UI 界面**：采用 PyQt5 构建，将摄像头采集、识别交互与模型管理无缝集成于一个干净的桌面应用中。

---

## 🖼️ 界面预览

系统主界面展示（包含人脸图像录入、实时识别监控与状态输出）：

<p align="center">
  <img width="450" height="450" alt="c231c512258d5f9a8c54248363753336" src="https://github.com/user-attachments/assets/d74d2dbc-5b92-4abc-b97a-4954849b9607">
</p>

---

## 🛠️ 技术栈与架构

| 模块 | 使用技术/算法 | 功能说明 |
| :--- | :--- | :--- |
| **GUI 界面** | PyQt5 / Qt Designer | 构建主控制台、视频流渲染区域与用户交互控件 |
| **人脸检测** | OpenCV (Haar Cascades) | 使用级联分类器快速提取图像/视频流中的人脸 ROI 区域 |
| **人脸识别** | OpenCV (LBPH Recognizer) | 提取局部二值模式直方图特征并完成身份比对 |
| **模型持续学习** | Python + OpenCV FileStorage | 支持本地人脸数据增量更新，不断迭代改进模型准确率 |
| **图像存储** | OpenCV / OS IO | 自动格式化人脸裁剪图并归档命名 |

---

## 📦 快速上手

### 1. 环境要求 (Prerequisites)

- **Python** 3.8 或更高版本
- 标配 USB 摄像头或笔记本内置摄像头

### 2. 安装依赖

克隆本仓库并安装所需的 Python 扩展库：

```bash
# 克隆仓库
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name

# 安装基础依赖库
pip install opencv-python opencv-contrib-python PyQt5 pillow
```

### 3. 运行主程序

```bash
# 启动图形化界面主程序
python main.py
```

---

## 📚 新手循序渐进教程

如果你是计算机视觉与 OpenCV 的初学者，建议按照以下**11个递进式脚本**顺序学习，从基础图像操作逐步掌握实时人脸识别系统构建：

```text
├── 基础图像处理
│   ├── 01读取图片.py              # 图像加载与窗口展示
│   ├── 02图片灰度转换.py           # 彩色图转灰度图 (降低计算复杂度)
│   ├── 03修改图片尺寸.py           # 图像 Resize 与缩放技巧
│   └── 04绘制形状.py              # 在图像上绘制矩形框与文本标注
│
├── 人脸检测基础
│   ├── 05人脸检测.py              # 单张静态图片中的人脸 Haar 检测
│   ├── 06摄像头人脸识别.py         # 调起本地摄像头并绘制检测框
│   └── 07视频人脸检测.py           # 读取本地视频文件进行逐帧检测
│
└── 模型训练与系统实战
    ├── 08训练人脸识别模型_origin.py # 人脸特征提取与基础模型训练
    ├── 08训练人脸识别模型_plus.py   # 模型训练进阶版 (数据增强/参数调优)
    ├── 09识别人脸.py              # 使用训练好的模型比对静态图像
    ├── 10录入人脸.py              # 动态抓取人脸并自动建立个人数据集
    └── 11摄像头的人脸识别.py        # 整合模型实现实时视频流身份辨识
```

---

## 🗺️ 未来规划 (Roadmap)

- [x] 基于 Haar 特征的静态与动态人脸检测
- [x] LBPH 模型训练与图像持久化保存
- [x] 基于 PyQt5 的可视化桌面交互界面
- [x] 支持增量人脸录入与模型持续学习
- [ ] 升级人脸检测算法（集成 InsightFace / RetinaFace 提升复杂光照下的鲁棒性）
- [ ] 增加 SQLite 数据库集成，实现更高效的个人身份信息管理
- [ ] 增加活体检测（Anti-Spoofing）功能，防止照片攻击

---

## 🤝 贡献指南 (Contributing)

非常欢迎提交 Issue 或 Pull Request 来完善这个项目！

1. **Fork** 本仓库
2. 创建特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交修改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 发起一个 **Pull Request**

---

## 📄 开源协议与致谢

本项目采用 [MIT License](LICENSE) 开源协议。

**致谢与参考：**
- [OpenCV Official Documentation](https://docs.opencv.org/)
- [PyQt5 Reference Guide](https://www.riverbankcomputing.com/software/pyqt/)

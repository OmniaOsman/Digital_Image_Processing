# # import sys
# #
# # from PyQt5 import QtWidgets
# # from PyQt5.QtWidgets import QMainWindow
# #
# #
# # def browseFilePushButton_4(self):
# #     fileName4 = QFileDialog.getOpenFileName(self.pushButton_4, 'open file')
# #     imagePatch4 = fileName4[0]
# #     pixmap4 = QPixmap(imagePatch4)
# #     self.label.setPixmap(QPixmap(pixmap4))
# #     # self.resize(pixmap4.width(), pixmap4.height())
# #
# #
# # def browseFilePushButton_3(self):
# #     fileName3 = QFileDialog.getOpenFileName(self.pushButton_3, 'open file')
# #     imagePatch3 = fileName3[0]
# #     pixmap3 = QPixmap(imagePatch3)
# #     self.label_2.setPixmap(QPixmap(pixmap3))
# #
# #
# # def browseFilePushButton_2(self):
# #     fileName2 = QFileDialog.getOpenFileName(self.pushButton_2, 'open file')
# #     imagePatch2 = fileName2[0]
# #     pixmap2 = QPixmap(imagePatch2)
# #     self.label_5.setPixmap(QPixmap(pixmap2))
# #
# #         self.pushButton_4.clicked.connect(self.browseFilePushButton_4)
# #         self.pushButton_3.clicked.connect(self.browseFilePushButton_3)
# #         self.pushButton_2.clicked.connect(self.browseFilePushButton_2)
# #
# # class myWindow(QMainWindow):
# #     def __init__(self):
# #         super(myWindow, self).__init__()
# #         self.setWindowTitle('Image Processing Project')
# #         self.setStyleSheet('background-color: #c0cccc')
# #         self.setGeometry(180, 50, 1000, 700)
# #         self.initUI()
# #
# #     # Click Event
# #     def clicked(self):
# #         self.fusion = imgFusion()
# #
# #
# #     def initUI(self):
# #
# #         # Add Main label
# #         self.text1 = QtWidgets.QLabel(self)
# #         self.text1.setText('Welcome to Digital Image Processing')
# #         self.text1.setStyleSheet('color: #000000; font-family: Baloo Bhaijaan 2; font-size: 32px')
# #         self.text1.move(250, 5)
# #         self.text1.adjustSize()
# #
# #         # Fusion Button
# #         self.btn1 = QtWidgets.QPushButton(self)
# #         self.btn1.setText('Fusion using Wavelet transformation')
# #         self.btn1.setStyleSheet('color: black; font-family: Baloo Bhaijaan 2;'
# #                                 'background-color: #d57276; font-size: 20px;')
# #         self.btn1.move(300, 50)
# #         self.btn1.adjustSize()
# #         self.btn1.clicked.connect(self.clicked)
# #
# #         # Noise Reduction Button
# #         self.btn2 = QtWidgets.QPushButton(self)
# #         self.btn2.setText('Noise Reduction')
# #         self.btn2.setStyleSheet('color: black; font-family: Baloo Bhaijaan 2;'
# #                                 'background-color: #d57276; font-size: 20px;')
# #         self.btn2.move(300, 70)
# #         self.btn2.adjustSize()
# #
# #
# # class imgFusion(QMainWindow):
# #     def __init__(self):
# #         super(imgFusion, self).__init__()
# #         self.setWindowTitle('Image Fusion')
# #         self.setStyleSheet('background-color: #c0cccc')
# #         self.setGeometry(180, 50, 1000, 700)
# #         self.initUI()
# #
# #     def initUI(self):
# #         # Add Main label
# #         self.text = QtWidgets.QLabel(self)
# #         self.text.setText('Welcome to Digital Image Processing')
# #         self.text.setStyleSheet('color: #d57276; font-family: Baloo Bhaijaan 2; font-size: 32px')
# #         self.text.move(250, 100)
# #         self.text.adjustSize()
# #
# #
# # def mainWindow():
# #     # Generate window
# #     app = QtWidgets.QApplication(sys.argv)
# #     window = myWindow()
# #     window.setWindowTitle('Image Processing Project')
# #     window.setStyleSheet('background-color: #c0cccc')
# #     window.setGeometry(180, 50, 1000, 700)
# #
# #     window.show()
# #     sys.exit(app.exec_())
# #
# #
# # mainWindow()
#
#
# from PyQt5 import QtCore, QtGui, QtWidgets
# from PyQt5.QtGui import QPixmap
# from PyQt5.QtWidgets import QFileDialog
#
# from fusion import fusion
#
#
# class Ui_MainWindow(object):
#     def setupUi(self, MainWindow):
#         MainWindow.setObjectName("MainWindow")
#         MainWindow.resize(1042, 675)
#         self.centralwidget = QtWidgets.QWidget(MainWindow)
#         self.centralwidget.setObjectName("centralwidget")
#         self.line = QtWidgets.QFrame(self.centralwidget)
#         self.line.setGeometry(QtCore.QRect(510, 20, 16, 611))
#         self.line.setFrameShape(QtWidgets.QFrame.VLine)
#         self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
#         self.line.setObjectName("line")
#         self.label = QtWidgets.QLabel(self.centralwidget)
#         self.label.setGeometry(QtCore.QRect(40, 80, 181, 181))
#         self.label.setFrameShape(QtWidgets.QFrame.StyledPanel)
#         self.label.setText("")
#         self.label.setObjectName("label")
#         self.label_2 = QtWidgets.QLabel(self.centralwidget)
#         self.label_2.setGeometry(QtCore.QRect(290, 80, 181, 181))
#         self.label_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
#         self.label_2.setText("")
#         self.label_2.setObjectName("label_2")
#         self.label_3 = QtWidgets.QLabel(self.centralwidget)
#         self.label_3.setGeometry(QtCore.QRect(120, 20, 261, 41))
#         font = QtGui.QFont()
#         font.setFamily("Baloo Bhaijaan 2")
#         font.setPointSize(28)
#         font.setBold(False)
#         font.setUnderline(False)
#         font.setWeight(50)
#         self.label_3.setFont(font)
#         self.label_3.setAlignment(QtCore.Qt.AlignCenter)
#         self.label_3.setObjectName("label_3")
#         self.label_4 = QtWidgets.QLabel(self.centralwidget)
#         self.label_4.setGeometry(QtCore.QRect(670, 20, 261, 41))
#         font = QtGui.QFont()
#         font.setFamily("Baloo Bhaijaan 2")
#         font.setPointSize(28)
#         font.setBold(False)
#         font.setUnderline(False)
#         font.setWeight(50)
#         self.label_4.setFont(font)
#         self.label_4.setAlignment(QtCore.Qt.AlignCenter)
#         self.label_4.setObjectName("label_4")
#         self.label_5 = QtWidgets.QLabel(self.centralwidget)
#         self.label_5.setEnabled(True)
#         self.label_5.setGeometry(QtCore.QRect(700, 80, 181, 181))
#         sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
#         sizePolicy.setHorizontalStretch(0)
#         sizePolicy.setVerticalStretch(0)
#         sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
#         self.label_5.setSizePolicy(sizePolicy)
#         self.label_5.setBaseSize(QtCore.QSize(0, 0))
#         self.label_5.setAcceptDrops(False)
#         self.label_5.setAutoFillBackground(False)
#         self.label_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
#         self.label_5.setText("")
#         self.label_5.setObjectName("label_5")
#         self.label_6 = QtWidgets.QLabel(self.centralwidget)
#         self.label_6.setGeometry(QtCore.QRect(170, 440, 181, 181))
#         self.label_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
#         self.label_6.setText("")
#         self.label_6.setObjectName("label_6")
#         self.label_7 = QtWidgets.QLabel(self.centralwidget)
#         self.label_7.setGeometry(QtCore.QRect(570, 390, 181, 181))
#         self.label_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
#         self.label_7.setText("")
#         self.label_7.setObjectName("label_7")
#         self.pushButton = QtWidgets.QPushButton(self.centralwidget)
#         self.pushButton.setGeometry(QtCore.QRect(740, 330, 111, 31))
#         self.pushButton.setObjectName("pushButton")
#         self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
#         self.pushButton_2.setGeometry(QtCore.QRect(740, 280, 111, 31))
#         self.pushButton_2.setObjectName("pushButton_2")
#         self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
#         self.pushButton_3.setGeometry(QtCore.QRect(330, 290, 111, 31))
#         self.pushButton_3.setObjectName("pushButton_3")
#         self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
#         self.pushButton_4.setGeometry(QtCore.QRect(80, 290, 111, 31))
#         self.pushButton_4.setObjectName("pushButton_4")
#         self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
#         self.pushButton_5.setGeometry(QtCore.QRect(200, 370, 111, 31))
#         self.pushButton_5.setObjectName("pushButton_5")
#         self.label_8 = QtWidgets.QLabel(self.centralwidget)
#         self.label_8.setGeometry(QtCore.QRect(820, 390, 181, 181))
#         self.label_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
#         self.label_8.setText("")
#         self.label_8.setObjectName("label_8")
#         self.label_9 = QtWidgets.QLabel(self.centralwidget)
#         self.label_9.setGeometry(QtCore.QRect(570, 580, 181, 31))
#         font = QtGui.QFont()
#         font.setFamily("Baloo Bhaijaan 2")
#         font.setPointSize(16)
#         font.setBold(False)
#         font.setUnderline(False)
#         font.setWeight(50)
#         self.label_9.setFont(font)
#         self.label_9.setAlignment(QtCore.Qt.AlignCenter)
#         self.label_9.setObjectName("label_9")
#         self.label_10 = QtWidgets.QLabel(self.centralwidget)
#         self.label_10.setGeometry(QtCore.QRect(820, 580, 181, 31))
#         font = QtGui.QFont()
#         font.setFamily("Baloo Bhaijaan 2")
#         font.setPointSize(16)
#         font.setBold(False)
#         font.setUnderline(False)
#         font.setWeight(50)
#         self.label_10.setFont(font)
#         self.label_10.setAlignment(QtCore.Qt.AlignCenter)
#         self.label_10.setObjectName("label_10")
#         MainWindow.setCentralWidget(self.centralwidget)
#         self.menubar = QtWidgets.QMenuBar(MainWindow)
#         self.menubar.setGeometry(QtCore.QRect(0, 0, 1042, 21))
#         self.menubar.setObjectName("menubar")
#         MainWindow.setMenuBar(self.menubar)
#         self.statusbar = QtWidgets.QStatusBar(MainWindow)
#         self.statusbar.setObjectName("statusbar")
#         MainWindow.setStatusBar(self.statusbar)
#
#         self.retranslateUi(MainWindow)
#         QtCore.QMetaObject.connectSlotsByName(MainWindow)
#
#         self.pushButton_4.clicked.connect(self.browseFilePushButton_4)
#         self.pushButton_3.clicked.connect(self.browseFilePushButton_3)
#         self.pushButton_2.clicked.connect(self.browseFilePushButton_2)
#         self.pushButton_5.clicked.connect(self.executePushButton_5)
#
#     def retranslateUi(self, MainWindow):
#         _translate = QtCore.QCoreApplication.translate
#         MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
#         self.label_3.setText(_translate("MainWindow", "Image Fusion"))
#         self.label_4.setText(_translate("MainWindow", "Noise Reduction"))
#         self.pushButton.setText(_translate("MainWindow", "Execute"))
#         self.pushButton_2.setText(_translate("MainWindow", "Upload image"))
#         self.pushButton_3.setText(_translate("MainWindow", "Upload image"))
#         self.pushButton_4.setText(_translate("MainWindow", "Upload image"))
#         self.pushButton_5.setText(_translate("MainWindow", "Execute"))
#         self.label_9.setText(_translate("MainWindow", "Gaussian Filter"))
#         self.label_10.setText(_translate("MainWindow", "Madian Filter"))
#
#     def browseFilePushButton_4(self):
#         global fileName4
#         fileName4 = QFileDialog.getOpenFileName(self.pushButton_4, 'open file')
#         imagePatch4 = fileName4[0]
#         pixmap4 = QPixmap(imagePatch4)
#         self.label.setPixmap(QPixmap(pixmap4))
#         # self.resize(pixmap4.width(), pixmap4.height())
#
#     def browseFilePushButton_3(self):
#         global fileName3
#         fileName3 = QFileDialog.getOpenFileName(self.pushButton_3, 'open file')
#         imagePatch3 = fileName3[0]
#         pixmap3 = QPixmap(imagePatch3)
#         self.label_2.setPixmap(QPixmap(pixmap3))
#
#     def browseFilePushButton_2(self):
#         global fileName2
#         fileName2 = QFileDialog.getOpenFileName(self.pushButton_2, 'open file')
#         imagePatch2 = fileName2[0]
#         pixmap2 = QPixmap(imagePatch2)
#         self.label_5.setPixmap(QPixmap(pixmap2))
#
#     def executePushButton_5(self):
#         e = fusion(fileName4, fileName3)
#         imagePatch5 = e
#         pixmap5 = QPixmap(imagePatch5)
#         self.label.setPixmap(QPixmap(pixmap5))
#
#
# if __name__ == "__main__":
#     import sys
#
#     app = QtWidgets.QApplication(sys.argv)
#     MainWindow = QtWidgets.QMainWindow()
#     ui = Ui_MainWindow()
#     ui.setupUi(MainWindow)
#     MainWindow.show()
#     sys.exit(app.exec_())
#


#     self.label_7.setPixmap(QPixmap(pixmap))self.pushButton_4.clicked.connect(self.browseFilePushButton_4)
#     self.pushButton_3.clicked.connect(self.browseFilePushButton_3)
#     self.pushButton_2.clicked.connect(self.browseFilePushButton_2)
#     self.pushButton.clicked.connect(self.executeNoiseReduction)
#
#
# def browseFilePushButton_4(self):
#     fileName4 = QFileDialog.getOpenFileName(self.pushButton_4, 'open file')
#     imagePatch4 = fileName4[0]
#     pixmap4 = QPixmap(imagePatch4)
#     self.label.setPixmap(QPixmap(pixmap4))
#     # self.resize(pixmap4.width(), pixmap4.height())
#
#
# def browseFilePushButton_3(self):
#     fileName3 = QFileDialog.getOpenFileName(self.pushButton_3, 'open file')
#     imagePatch3 = fileName3[0]
#     pixmap3 = QPixmap(imagePatch3)
#     self.label_2.setPixmap(QPixmap(pixmap3))
#
#     # Noise Reduction upload button
#
#
# def browseFilePushButton_2(self):
#     fileName2 = QFileDialog.getOpenFileName(self.pushButton_2, 'open file')
#     imagePatch2 = fileName2[0]
#     pixmap2 = QPixmap(imagePatch2)
#     self.label_5.setPixmap(QPixmap(pixmap2))
#
#
# def executeNoiseReduction(self):
#     # median Filter
#     img = imread(fileName2)
#     # turn image in gray scale value
#     gray = cvtColor(img, COLOR_BGR2GRAY)
#
#     # get values with two different mask size
#     median3x3 = median_filter(gray, 3)
#     median5x5 = median_filter(gray, 5)
#
#     # show result images
#     imagePatchMedian = median3x3[0]
#     pixmap = QPixmap(imagePatchMedian)
#     self.label_7.setPixmap(QPixmap(pixmap))
# imshow("median filter with 3x3 mask", median3x3)
# imshow("median filter with 5x5 mask", median5x5)
# waitKey(0)

def convert_cv_qt(self, cv_img):
    """Convert from an opencv image to QPixmap"""
    rgb_image = cvtColor(cv_img, COLOR_BGR2GRAY)
    h, w, ch = rgb_image.shape
    bytes_per_line = ch * w
    convert_to_Qt_format = QtGui.QImage(rgb_image.data, w, h, bytes_per_line, QtGui.QImage.Format_RGB888)
    p = convert_to_Qt_format.scaled(self.disply_width, self.display_height, Qt.KeepAspectRatio)
    return QPixmap.fromImage(p)


def browseFilePushButton_4(self):
    fileName4 = QFileDialog.getOpenFileName(self.pushButton_4, 'open file')
    imagePatch4 = fileName4[0]
    pixmap4 = QPixmap(imagePatch4)
    self.label.setPixmap(QPixmap(pixmap4))
    # self.resize(pixmap4.width(), pixmap4.height())


def browseFilePushButton_3(self):
    fileName3 = QFileDialog.getOpenFileName(self.pushButton_3, 'open file')
    imagePatch3 = fileName3[0]
    pixmap3 = QPixmap(imagePatch3)
    self.label_2.setPixmap(QPixmap(pixmap3))


# Noise Reduction upload button
def browseFilePushButton_2(self):
    self.fileName2 = QFileDialog.getOpenFileName(self.pushButton_2, 'open file')
    self.imagePatch2 = self.fileName2[0]
    pixmap2 = QPixmap(self.imagePatch2)
    self.label_5.setPixmap(pixmap2)
    self.label_5.resize(200, 200)


def executeNoiseReductionMedianFilter(self):
    # median Filter
    self.img = imread(self.imagePatch2)
    # turn image in gray scale value
    gray = cvtColor(self.img, COLOR_BGR2GRAY)

    # get values with two different mask size
    median5x5 = median_filter(gray, 5)
    # median3x3 = median5x5(gray, 3)
    # convert median5x5 from GRAY scale to RGB
    color = cvtColor(median5x5, COLOR_BGR2RGB)
    # QImage to QPixmap
    height, width, bytesPerComponent = color.shape
    bytesPerLine = bytesPerComponent * width
    img_ = QImage(color, width, height, bytesPerLine, QImage.Format_RGB888)
    # display image in label
    self.label_8.setPixmap(QPixmap.fromImage(img_))
    self.label_8.resize(200, 200)

    # show result images
    # m = QImage(median3x3)
    # self.label_8.setPixmap(mm)


def executeNoiseReductionGaussianFilter(self):
    # Gaussian Filter
    self.img = imread(self.imagePatch2)
    # turn image in gray scale value
    gray = cvtColor(self.img, COLOR_BGR2GRAY)

    # get values with two different mask size
    gaussian3x3 = gaussian_filter(gray, 3, sigma=1)
    # gaussian5x5 = gaussian_filter(gray, 5, sigma=0.8)

    # convert median5x5 from GRAY scale to RGB
    color = cvtColor(gaussian3x3, COLOR_BGR2RGB)

    # QImage to QPixmap
    height, width, bytesPerComponent = color.shape
    bytesPerLine = bytesPerComponent * width
    img_ = QImage(color, width, height, bytesPerLine, QImage.Format_RGB888)
    # display image in label
    self.label_8.setPixmap(QPixmap.fromImage(img_))
    self.label_8.resize(200, 200)




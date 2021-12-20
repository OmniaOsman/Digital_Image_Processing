from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtWidgets import QFileDialog
from cv2 import cvtColor, COLOR_BGR2GRAY, imread, COLOR_BGR2RGB, imshow
from scipy.ndimage import median_filter
from gaussian import gaussian_filter
import fusion as fuse


class Ui_MainWindow(object):
    def __init__(self):
        self.display_height = None
        self.generatedImage = None
        self.imagePatch4 = None
        self.imagePatch3 = None
        self.display_width = None
        self.median3x3 = None
        self.height = None
        self.width = None
        self.img = None
        self.imagePatch2 = None
        self.fileName2 = None
        self.fileName3 = None
        self.fileName4 = None
        self.label_8 = None
        self.pushButton = None
        self.label_6 = None
        self.menubar = None
        self.pushButton_4 = None
        self.pushButton_5 = None
        self.pushButton_2 = None
        self.pushButton_6 = None
        self.statusbar = None
        self.pushButton_3 = None
        self.label_5 = None
        self.label_4 = None
        self.label_3 = None
        self.label_2 = None
        self.label = None
        self.line = None
        self.centralwidget = None

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1060, 712)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(510, 20, 16, 651))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 80, 191, 191))
        self.label.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(290, 80, 191, 191))
        self.label_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(120, 20, 261, 41))
        font = QtGui.QFont()
        font.setFamily("Baloo Bhaijaan 2")
        font.setPointSize(28)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(650, 20, 261, 41))
        font = QtGui.QFont()
        font.setFamily("Baloo Bhaijaan 2")
        font.setPointSize(28)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setEnabled(True)
        self.label_5.setGeometry(QtCore.QRect(690, 70, 201, 191))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setBaseSize(QtCore.QSize(0, 0))
        self.label_5.setAcceptDrops(False)
        self.label_5.setAutoFillBackground(False)
        self.label_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(160, 440, 201, 191))
        self.label_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(730, 330, 121, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(730, 280, 121, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(330, 290, 111, 31))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(80, 290, 111, 31))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(200, 370, 111, 31))
        self.pushButton_5.setObjectName("pushButton_5")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(550, 420, 191, 191))
        self.label_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(730, 370, 121, 31))
        self.pushButton_6.setObjectName("pushButton_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(560, 630, 181, 20))
        font = QtGui.QFont()
        font.setFamily("Baloo Bhaijaan 2")
        font.setPointSize(16)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(830, 419, 191, 191))
        self.label_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_9.setText("")
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(840, 630, 181, 20))
        font = QtGui.QFont()
        font.setFamily("Baloo Bhaijaan 2")
        font.setPointSize(16)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.label_10.setFont(font)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1060, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.pushButton_4.clicked.connect(self.browseFilePushButton_4)
        self.pushButton_3.clicked.connect(self.browseFilePushButton_3)
        self.pushButton_2.clicked.connect(self.browseFilePushButton_2)
        self.pushButton.clicked.connect(self.executeNoiseReductionMedianFilter)
        self.pushButton_6.clicked.connect(self.executeNoiseReductionGaussianFilter)
        self.pushButton_5.clicked.connect(self.executeFusion)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_3.setText(_translate("MainWindow", "Image Fusion"))
        self.label_4.setText(_translate("MainWindow", "Noise Reduction"))
        self.pushButton.setText(_translate("MainWindow", "Execute median filter"))
        self.pushButton_2.setText(_translate("MainWindow", "Upload image"))
        self.pushButton_3.setText(_translate("MainWindow", "Upload image"))
        self.pushButton_4.setText(_translate("MainWindow", "Upload image"))
        self.pushButton_5.setText(_translate("MainWindow", "Execute"))
        self.pushButton_6.setText(_translate("MainWindow", "Execute gaussian filter"))
        self.label_7.setText(_translate("MainWindow", "3X3 Mask"))
        self.label_10.setText(_translate("MainWindow", "5X5 Mask"))

    def convert_cv_qt(self, cv_img):
        """Convert from an opencv image to QPixmap"""
        rgb_image = cvtColor(cv_img, COLOR_BGR2GRAY)
        h, w, ch = rgb_image.shape
        bytes_per_line = ch * w
        convert_to_Qt_format = QtGui.QImage(rgb_image.data, w, h, bytes_per_line, QtGui.QImage.Format_RGB888)
        p = convert_to_Qt_format.scaled(self.display_width, self.display_height, Qt.KeepAspectRatio)
        return QPixmap.fromImage(p)

    def browseFilePushButton_4(self):
        self.fileName4 = QFileDialog.getOpenFileName(self.pushButton_4, 'open file')
        self.imagePatch4 = self.fileName4[0]
        pixmap4 = QPixmap(self.imagePatch4)
        self.label.setPixmap(QPixmap(pixmap4))
        # self.resize(pixmap4.width(), pixmap4.height())

    def browseFilePushButton_3(self):
        self.fileName3 = QFileDialog.getOpenFileName(self.pushButton_3, 'open file')
        self.imagePatch3 = self.fileName3[0]
        pixmap3 = QPixmap(self.imagePatch3)
        self.label_2.setPixmap(QPixmap(pixmap3))

    # Noise Reduction upload button
    def browseFilePushButton_2(self):
        self.fileName2 = QFileDialog.getOpenFileName(self.pushButton_2, 'open file')
        self.imagePatch2 = self.fileName2[0]
        pixmap2 = QPixmap(self.imagePatch2)
        self.label_5.setPixmap(pixmap2)

    def executeNoiseReductionMedianFilter(self):
        # median Filter
        self.img = imread(self.imagePatch2)
        # turn image in gray scale value
        gray = cvtColor(self.img, COLOR_BGR2GRAY)

        # get values with two different mask size
        median5x5 = median_filter(gray, 5)
        median3x3 = median_filter(gray, 3)
        # convert from GRAY scale to RGB
        color3x3 = cvtColor(median3x3, COLOR_BGR2RGB)
        color5x5 = cvtColor(median5x5, COLOR_BGR2RGB)
        # QImage to QPixmap for mask 3x3
        height, width, bytesPerComponent = color3x3.shape
        bytesPerLine = bytesPerComponent * width
        img_ = QImage(color3x3, width, height, bytesPerLine, QImage.Format_RGB888)
        # display image in label for mask 3x3
        self.label_8.setPixmap(QPixmap.fromImage(img_))

        # QImage to QPixmap for mask 5x5
        height, width, bytesPerComponent = color5x5.shape
        bytesPerLine = bytesPerComponent * width
        img_ = QImage(color5x5, width, height, bytesPerLine, QImage.Format_RGB888)
        # display image in label for mask 5x5
        self.label_9.setPixmap(QPixmap.fromImage(img_))

    # Noise Reduction using Gaussian Filter
    def executeNoiseReductionGaussianFilter(self):
        # Gaussian Filter
        self.img = imread(self.imagePatch2)
        # turn image in gray scale value
        gray = cvtColor(self.img, COLOR_BGR2GRAY)

        # get values with two different mask size
        gaussian3x3 = gaussian_filter(gray, 3, sigma=1)
        gaussian5x5 = gaussian_filter(gray, 5, sigma=0.8)

        # convert median5x5 from GRAY scale to RGB
        color3x3 = cvtColor(gaussian3x3, COLOR_BGR2RGB)
        color5x5 = cvtColor(gaussian5x5, COLOR_BGR2RGB)

        # QImage to QPixmap for mask 3x3
        height, width, bytesPerComponent = color3x3.shape
        bytesPerLine = bytesPerComponent * width
        img_ = QImage(color3x3, width, height, bytesPerLine, QImage.Format_RGB888)

        # display image in label
        self.label_8.setPixmap(QPixmap.fromImage(img_))

        # QImage to QPixmap for mask 5x5
        height, width, bytesPerComponent = color5x5.shape
        bytesPerLine = bytesPerComponent * width
        img_ = QImage(color5x5, width, height, bytesPerLine, QImage.Format_RGB888)

        # display image in label
        self.label_9.setPixmap(QPixmap.fromImage(img_))

    # Image Fusion
    def executeFusion(self):
        self.generatedImage = fuse.fusion(self.imagePatch3, self.imagePatch4)

        color = cvtColor(self.generatedImage, COLOR_BGR2RGB)
        height, width, bytesPerComponent = color.shape
        bytesPerLine = bytesPerComponent * width
        img_ = QImage(color, width, height, bytesPerLine, QImage.Format_RGB888)

        # display image in label
        self.label_6.setPixmap(QPixmap.fromImage(img_))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.setWindowTitle('Digital Image Processing')
    MainWindow.setGeometry(150, 50, 1050, 700)
    MainWindow.show()
    sys.exit(app.exec_())

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\Home_Page.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(964, 574)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(61, 61, 61))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(91, 91, 91))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(76, 76, 76))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(30, 30, 30))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 40, 40))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(61, 61, 61))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(30, 30, 30))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(61, 61, 61))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(91, 91, 91))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(76, 76, 76))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(30, 30, 30))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 40, 40))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(61, 61, 61))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(30, 30, 30))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(30, 30, 30))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(61, 61, 61))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(91, 91, 91))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(76, 76, 76))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(30, 30, 30))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 40, 40))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(30, 30, 30))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(30, 30, 30))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(61, 61, 61))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(61, 61, 61))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(61, 61, 61))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        MainWindow.setPalette(palette)
        MainWindow.setStyleSheet("QStatusBar\n"
"{\n"
"    color: white;\n"
"    \n"
"    font: 9pt \"Montserrat\";\n"
"}\n"
"QStatusBar::item\n"
"{\n"
"    border: 0px transparent dark;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        palette = QtGui.QPalette()
        gradient = QtGui.QLinearGradient(0.489, 0.0113636, 0.506, 1.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(72, 72, 72))
        gradient.setColorAt(1.0, QtGui.QColor(30, 30, 30))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        gradient = QtGui.QLinearGradient(0.489, 0.0113636, 0.506, 1.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(72, 72, 72))
        gradient.setColorAt(1.0, QtGui.QColor(30, 30, 30))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        gradient = QtGui.QLinearGradient(0.489, 0.0113636, 0.506, 1.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(72, 72, 72))
        gradient.setColorAt(1.0, QtGui.QColor(30, 30, 30))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        gradient = QtGui.QLinearGradient(0.489, 0.0113636, 0.506, 1.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(72, 72, 72))
        gradient.setColorAt(1.0, QtGui.QColor(30, 30, 30))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        gradient = QtGui.QLinearGradient(0.489, 0.0113636, 0.506, 1.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(72, 72, 72))
        gradient.setColorAt(1.0, QtGui.QColor(30, 30, 30))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        gradient = QtGui.QLinearGradient(0.489, 0.0113636, 0.506, 1.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(72, 72, 72))
        gradient.setColorAt(1.0, QtGui.QColor(30, 30, 30))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        gradient = QtGui.QLinearGradient(0.489, 0.0113636, 0.506, 1.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(72, 72, 72))
        gradient.setColorAt(1.0, QtGui.QColor(30, 30, 30))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(30, 30, 30))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        gradient = QtGui.QLinearGradient(0.489, 0.0113636, 0.506, 1.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(72, 72, 72))
        gradient.setColorAt(1.0, QtGui.QColor(30, 30, 30))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        gradient = QtGui.QLinearGradient(0.489, 0.0113636, 0.506, 1.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(72, 72, 72))
        gradient.setColorAt(1.0, QtGui.QColor(30, 30, 30))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.centralwidget.setPalette(palette)
        self.centralwidget.setStyleSheet("#centralwidget{\n"
"    \n"
"    background-color: qlineargradient(spread:pad, x1:0.489, y1:0.0113636, x2:0.506, y2:1, stop:0 rgba(72, 72, 72, 255), stop:1 rgba(30, 30, 30, 255));\n"
"    \n"
"    border-image: url(./UI/images/TgFZH.jpg);\n"
"}\n"
"QLabel{\n"
"    color: white;\n"
"}\n"
"QPushButton\n"
"{\n"
"    color: #eff0f1;\n"
"    background-color: qlineargradient(x1: 0.5, y1: 0.5 x2: 0.5, y2: 1, stop: 0 #3b4045, stop: 0.5 #31363b);\n"
"    border-width: 0.1ex;\n"
"    border-color: #76797c;\n"
"    border-style: solid;\n"
"    padding:2ex;\n"
"    border-radius: 0.2ex;\n"
"    outline: none;\n"
"}\n"
"\n"
"QPushButton:disabled\n"
"{\n"
"    background-color: #31363b;\n"
"    border-width: 0.1ex;\n"
"    border-color: #454545;\n"
"    border-style: solid;\n"
"    padding-top: 0.5ex;\n"
"    padding-bottom: 0.5ex;\n"
"    padding-left: 1ex;\n"
"    padding-right: 1ex;\n"
"    border-radius: 0.2ex;\n"
"    color: #454545;\n"
"}\n"
"\n"
"QPushButton:focus\n"
"{\n"
"    color: white;\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"    background-color: #31363b;\n"
"    padding-top: -1.5ex;\n"
"    padding-bottom: -1.7ex;\n"
"}\n"
"\n"
"QComboBox\n"
"{\n"
"    selection-background-color: #3daee9;\n"
"    border-style: solid;\n"
"    border: 0.1ex solid #76797c;\n"
"    border-radius: 0.2ex;\n"
"    padding: 0.5ex;\n"
"    min-width: 7.5ex;\n"
"}\n"
"\n"
"QPushButton:checked\n"
"{\n"
"    background-color: #76797c;\n"
"    border-color: #6A6969;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"    background-color: qlineargradient(x1: 0.5, y1: 0.5 x2: 0.5, y2: 1, stop: 0 #454a4f, stop: 0.5 #3b4045);\n"
"    border: 0.1ex solid #3daee9;\n"
"    color: #eff0f1;\n"
"}\n"
"\n"
"QPushButton:checked:hover\n"
"{\n"
"    background-color: qlineargradient(x1: 0.5, y1: 0.5 x2: 0.5, y2: 1, stop: 0 #808386, stop: 0.5 #76797c);\n"
"    border: 0.1ex solid #3daee9;\n"
"    color: #eff0f1;\n"
"}")
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setMinimumSize(QtCore.QSize(627, 309))
        self.frame_2.setStyleSheet("#frame_2{\n"
"    border: none;\n"
"}")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_3.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.pushButton_connect = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_connect.setMaximumSize(QtCore.QSize(120, 50))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_connect.setFont(font)
        self.pushButton_connect.setObjectName("pushButton_connect")
        self.gridLayout_3.addWidget(self.pushButton_connect, 5, 3, 1, 1)
        self.frame_4 = QtWidgets.QFrame(self.frame_2)
        self.frame_4.setMaximumSize(QtCore.QSize(100, 50))
        self.frame_4.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.checkBox_tls = QtWidgets.QCheckBox(self.frame_4)
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(11)
        self.checkBox_tls.setFont(font)
        self.checkBox_tls.setText("")
        self.checkBox_tls.setChecked(True)
        self.checkBox_tls.setObjectName("checkBox_tls")
        self.horizontalLayout_2.addWidget(self.checkBox_tls)
        self.label_7 = QtWidgets.QLabel(self.frame_4)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_2.addWidget(self.label_7)
        self.gridLayout_3.addWidget(self.frame_4, 3, 3, 1, 1)
        self.frame = QtWidgets.QFrame(self.frame_2)
        self.frame.setStyleSheet("#frame{\n"
"    margin-left: 20px;\n"
"    border: none;\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setContentsMargins(-1, 0, -1, 25)
        self.gridLayout.setVerticalSpacing(2)
        self.gridLayout.setObjectName("gridLayout")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setEnabled(True)
        self.label_3.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Noto Sans Arabic")
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setEnabled(True)
        self.label_4.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Noto Sans Arabic")
        font.setPointSize(11)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 1, 1, 1, 1)
        self.lineEdit_proxy_ip = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_proxy_ip.setEnabled(True)
        self.lineEdit_proxy_ip.setMaximumSize(QtCore.QSize(439, 30))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(10)
        self.lineEdit_proxy_ip.setFont(font)
        self.lineEdit_proxy_ip.setStyleSheet("#lineEdit_proxy_ip{\n"
"    border: 0.3ex solid white;\n"
"    border-radius: 5px;\n"
"    padding: 5px 10px;\n"
"}\n"
"#lineEdit_proxy_ip:disabled{\n"
"    border: 0.3ex solid #9a9a9a;\n"
"    border-radius: 5px;\n"
"    padding: 5px 10px;\n"
"    color: rgb(203, 203, 203);\n"
"    background-color: rgb(163, 163, 163);\n"
"}\n"
"\n"
"#lineEdit_proxy_ip::hover{\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(34, 34, 34);\n"
"    padding-left: 15px;\n"
"}")
        self.lineEdit_proxy_ip.setObjectName("lineEdit_proxy_ip")
        self.gridLayout.addWidget(self.lineEdit_proxy_ip, 2, 0, 1, 1)
        self.lineEdit_proxy_port = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_proxy_port.setEnabled(True)
        self.lineEdit_proxy_port.setMaximumSize(QtCore.QSize(115, 30))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(10)
        self.lineEdit_proxy_port.setFont(font)
        self.lineEdit_proxy_port.setStyleSheet("#lineEdit_proxy_port{\n"
"    border: 0.3ex solid white;\n"
"    border-radius: 5px;\n"
"    padding: 5px 10px;\n"
"}\n"
"#lineEdit_proxy_port:disabled{\n"
"    border: 0.3ex solid #9a9a9a;\n"
"    border-radius: 5px;\n"
"    padding: 5px 10px;\n"
"    color: rgb(203, 203, 203);\n"
"    background-color: rgb(163, 163, 163);\n"
"}\n"
"\n"
"#lineEdit_proxy_port::hover{\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(34, 34, 34);\n"
"    padding-left: 15px;\n"
"}")
        self.lineEdit_proxy_port.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.lineEdit_proxy_port.setText("")
        self.lineEdit_proxy_port.setMaxLength(5)
        self.lineEdit_proxy_port.setObjectName("lineEdit_proxy_port")
        self.gridLayout.addWidget(self.lineEdit_proxy_port, 2, 1, 1, 1)
        self.gridLayout_3.addWidget(self.frame, 4, 1, 1, 3)
        self.frame_5 = QtWidgets.QFrame(self.frame_2)
        self.frame_5.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.frame_5)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.lineEdit_address = QtWidgets.QLineEdit(self.frame_5)
        self.lineEdit_address.setMaximumSize(QtCore.QSize(465, 30))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(10)
        self.lineEdit_address.setFont(font)
        self.lineEdit_address.setStyleSheet("#lineEdit_address{\n"
"    border: 0.3ex solid white;\n"
"    border-radius: 5px;\n"
"    padding: 5px 10px;\n"
"}\n"
"#lineEdit_address:disabled{\n"
"    border: 0.3ex solid #9a9a9a;\n"
"    border-radius: 5px;\n"
"    padding: 5px 10px;\n"
"    color: rgb(203, 203, 203);\n"
"    background-color: rgb(163, 163, 163);\n"
"}\n"
"\n"
"#lineEdit_address::hover{\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(34, 34, 34);\n"
"    padding-left: 15px;\n"
"}")
        self.lineEdit_address.setObjectName("lineEdit_address")
        self.gridLayout_4.addWidget(self.lineEdit_address, 1, 0, 1, 1)
        self.lineEdit_address_port = QtWidgets.QLineEdit(self.frame_5)
        self.lineEdit_address_port.setMaximumSize(QtCore.QSize(115, 30))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(10)
        self.lineEdit_address_port.setFont(font)
        self.lineEdit_address_port.setStyleSheet("#lineEdit_address_port{\n"
"    border: 0.3ex solid white;\n"
"    border-radius: 5px;\n"
"    padding: 5px 10px;\n"
"}\n"
"#lineEdit_address_port:disabled{\n"
"    border: 0.3ex solid #9a9a9a;\n"
"    border-radius: 5px;\n"
"    padding: 5px 10px;\n"
"    color: rgb(203, 203, 203);\n"
"    background-color: rgb(163, 163, 163);\n"
"}\n"
"\n"
"#lineEdit_address_port::hover{\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(34, 34, 34);\n"
"    padding-left: 15px;\n"
"}")
        self.lineEdit_address_port.setText("")
        self.lineEdit_address_port.setMaxLength(5)
        self.lineEdit_address_port.setObjectName("lineEdit_address_port")
        self.gridLayout_4.addWidget(self.lineEdit_address_port, 1, 2, 1, 1)
        self.label = QtWidgets.QLabel(self.frame_5)
        self.label.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Noto Sans Arabic")
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout_4.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.frame_5)
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Noto Sans Arabic")
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout_4.addWidget(self.label_2, 0, 2, 1, 1)
        self.gridLayout_3.addWidget(self.frame_5, 0, 1, 1, 3)
        self.frame_3 = QtWidgets.QFrame(self.frame_2)
        self.frame_3.setMaximumSize(QtCore.QSize(150, 16777215))
        self.frame_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.checkBox_socks5 = QtWidgets.QCheckBox(self.frame_3)
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(11)
        self.checkBox_socks5.setFont(font)
        self.checkBox_socks5.setStyleSheet("")
        self.checkBox_socks5.setText("")
        self.checkBox_socks5.setChecked(False)
        self.checkBox_socks5.setObjectName("checkBox_socks5")
        self.horizontalLayout.addWidget(self.checkBox_socks5)
        self.label_6 = QtWidgets.QLabel(self.frame_3)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout.addWidget(self.label_6)
        self.gridLayout_3.addWidget(self.frame_3, 3, 1, 1, 1)
        self.gridLayout_2.addWidget(self.frame_2, 2, 1, 1, 2)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 2, 3, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 2, 0, 1, 1)
        self.label_logo = QtWidgets.QLabel(self.centralwidget)
        self.label_logo.setMaximumSize(QtCore.QSize(16777215, 100))
        self.label_logo.setStyleSheet("background-color: white;")
        self.label_logo.setText("")
        self.label_logo.setPixmap(QtGui.QPixmap("./UI/images/YfZiodQJx.png"))
        self.label_logo.setAlignment(QtCore.Qt.AlignCenter)
        self.label_logo.setObjectName("label_logo")
        self.gridLayout_2.addWidget(self.label_logo, 0, 0, 1, 4)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem2, 1, 0, 1, 4)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem3, 3, 0, 1, 4)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 964, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.label_7.setBuddy(self.checkBox_tls)
        self.label_3.setBuddy(self.lineEdit_proxy_ip)
        self.label_4.setBuddy(self.lineEdit_proxy_port)
        self.label.setBuddy(self.lineEdit_address)
        self.label_2.setBuddy(self.lineEdit_address_port)
        self.label_6.setBuddy(self.checkBox_socks5)

        self.retranslateUi(MainWindow)
        self.lineEdit_proxy_port.returnPressed.connect(self.pushButton_connect.click)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.checkBox_socks5, self.lineEdit_proxy_ip)
        MainWindow.setTabOrder(self.lineEdit_proxy_ip, self.lineEdit_proxy_port)
        MainWindow.setTabOrder(self.lineEdit_proxy_port, self.pushButton_connect)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Torpoker - Home"))
        self.pushButton_connect.setText(_translate("MainWindow", "Connect"))
        self.label_7.setText(_translate("MainWindow", "TLS"))
        self.label_3.setStatusTip(_translate("MainWindow", "socks5 IP address"))
        self.label_3.setText(_translate("MainWindow", "IP Address"))
        self.label_4.setStatusTip(_translate("MainWindow", "Socks5 IP port"))
        self.label_4.setText(_translate("MainWindow", "Port"))
        self.lineEdit_proxy_ip.setStatusTip(_translate("MainWindow", "socks5 IP address"))
        self.lineEdit_proxy_port.setStatusTip(_translate("MainWindow", "Socks5 IP port"))
        self.lineEdit_address.setStatusTip(_translate("MainWindow", "Host to connect to"))
        self.lineEdit_address_port.setStatusTip(_translate("MainWindow", "address port to connect"))
        self.label.setStatusTip(_translate("MainWindow", "Address to connect to"))
        self.label.setText(_translate("MainWindow", "Host"))
        self.label_2.setStatusTip(_translate("MainWindow", "address port to connect"))
        self.label_2.setText(_translate("MainWindow", "Port"))
        self.checkBox_socks5.setStatusTip(_translate("MainWindow", "check to enable socks5 proxy connection"))
        self.label_6.setText(_translate("MainWindow", "Socks5 Proxy"))

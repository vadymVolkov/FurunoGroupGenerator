# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designe.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(687, 293)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_day1 = QtWidgets.QLabel(self.centralwidget)
        self.label_day1.setGeometry(QtCore.QRect(55, 10, 60, 20))
        self.label_day1.setObjectName("label_day1")
        self.label_day2 = QtWidgets.QLabel(self.centralwidget)
        self.label_day2.setGeometry(QtCore.QRect(225, 10, 60, 20))
        self.label_day2.setObjectName("label_day2")
        self.day_backward_button = QtWidgets.QPushButton(self.centralwidget)
        self.day_backward_button.setGeometry(QtCore.QRect(350, 38, 150, 35))
        self.day_backward_button.setObjectName("day_backward_button")
        self.day_forward_button = QtWidgets.QPushButton(self.centralwidget)
        self.day_forward_button.setGeometry(QtCore.QRect(520, 38, 150, 35))
        self.day_forward_button.setObjectName("day_forward_button")
        self.browse_group_folder_button = QtWidgets.QPushButton(self.centralwidget)
        self.browse_group_folder_button.setGeometry(QtCore.QRect(10, 90, 150, 35))
        self.browse_group_folder_button.setObjectName("browse_group_folder_button")
        self.path_group_folder_label = QtWidgets.QLabel(self.centralwidget)
        self.path_group_folder_label.setGeometry(QtCore.QRect(180, 95, 31, 20))
        self.path_group_folder_label.setObjectName("path_group_folder_label")
        self.create_new_group_button = QtWidgets.QPushButton(self.centralwidget)
        self.create_new_group_button.setGeometry(QtCore.QRect(10, 130, 150, 35))
        self.create_new_group_button.setObjectName("create_new_group_button")
        self.generate_test_files_button = QtWidgets.QPushButton(self.centralwidget)
        self.generate_test_files_button.setGeometry(QtCore.QRect(10, 170, 150, 35))
        self.generate_test_files_button.setObjectName("generate_test_files_button")
        self.status_label = QtWidgets.QLabel(self.centralwidget)
        self.status_label.setGeometry(QtCore.QRect(20, 210, 651, 20))
        self.status_label.setText("")
        self.status_label.setObjectName("status_label")
        self.exit_button = QtWidgets.QPushButton(self.centralwidget)
        self.exit_button.setGeometry(QtCore.QRect(520, 250, 150, 35))
        self.exit_button.setObjectName("exit_button")
        self.day1_value = QtWidgets.QLineEdit(self.centralwidget)
        self.day1_value.setGeometry(QtCore.QRect(10, 40, 150, 25))
        self.day1_value.setObjectName("day1_value")
        self.day2_value = QtWidgets.QLineEdit(self.centralwidget)
        self.day2_value.setGeometry(QtCore.QRect(180, 40, 150, 25))
        self.day2_value.setObjectName("day2_value")
        self.path_group_folder_value = QtWidgets.QLabel(self.centralwidget)
        self.path_group_folder_value.setGeometry(QtCore.QRect(180, 130, 491, 20))
        self.path_group_folder_value.setText("")
        self.path_group_folder_value.setObjectName("path_group_folder_value")
        self.status_label_2 = QtWidgets.QLabel(self.centralwidget)
        self.status_label_2.setGeometry(QtCore.QRect(20, 250, 481, 20))
        self.status_label_2.setText("")
        self.status_label_2.setObjectName("status_label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.actionNew = QtWidgets.QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")
        self.actionCreate_ADF = QtWidgets.QAction(MainWindow)
        self.actionCreate_ADF.setObjectName("actionCreate_ADF")
        self.actionCreate_Test = QtWidgets.QAction(MainWindow)
        self.actionCreate_Test.setObjectName("actionCreate_Test")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Furuno Group Generator"))
        self.label_day1.setText(_translate("MainWindow", "Day 1"))
        self.label_day2.setText(_translate("MainWindow", "Day 2"))
        self.day_backward_button.setText(_translate("MainWindow", "Day backward"))
        self.day_forward_button.setText(_translate("MainWindow", "Day forward"))
        self.browse_group_folder_button.setText(_translate("MainWindow", "Browse "))
        self.path_group_folder_label.setText(_translate("MainWindow", "Path:"))
        self.create_new_group_button.setText(_translate("MainWindow", "Create new group"))
        self.generate_test_files_button.setText(_translate("MainWindow", "Generate test files"))
        self.exit_button.setText(_translate("MainWindow", "Exit"))
        self.actionNew.setText(_translate("MainWindow", "New group ..."))
        self.actionCreate_ADF.setText(_translate("MainWindow", "Create ADF"))
        self.actionCreate_Test.setText(_translate("MainWindow", "Create Test"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))

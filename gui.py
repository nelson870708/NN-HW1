# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(909, 526)
        self.groupBox_setting = QtWidgets.QGroupBox(Form)
        self.groupBox_setting.setGeometry(QtCore.QRect(20, 30, 331, 211))
        self.groupBox_setting.setObjectName("groupBox_setting")
        self.gridLayoutWidget = QtWidgets.QWidget(self.groupBox_setting)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 20, 311, 181))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.doubleSpinBox_learning_rate = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget)
        self.doubleSpinBox_learning_rate.setMaximum(1.0)
        self.doubleSpinBox_learning_rate.setSingleStep(0.01)
        self.doubleSpinBox_learning_rate.setProperty("value", 0.8)
        self.doubleSpinBox_learning_rate.setObjectName("doubleSpinBox_learning_rate")
        self.gridLayout.addWidget(self.doubleSpinBox_learning_rate, 2, 1, 1, 1)
        self.label_stop_condition = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_stop_condition.setObjectName("label_stop_condition")
        self.gridLayout.addWidget(self.label_stop_condition, 3, 0, 1, 1)
        self.label_learning_rate = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_learning_rate.setObjectName("label_learning_rate")
        self.gridLayout.addWidget(self.label_learning_rate, 2, 0, 1, 1)
        self.comboBox_file = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.comboBox_file.setObjectName("comboBox_file")
        self.gridLayout.addWidget(self.comboBox_file, 0, 1, 1, 1)
        self.pushButton_start = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_start.setObjectName("pushButton_start")
        self.gridLayout.addWidget(self.pushButton_start, 4, 0, 1, 1)
        self.label_file = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_file.setObjectName("label_file")
        self.gridLayout.addWidget(self.label_file, 0, 0, 1, 1)
        self.doubleSpinBox_stop_condition = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget)
        self.doubleSpinBox_stop_condition.setMaximum(1.0)
        self.doubleSpinBox_stop_condition.setSingleStep(0.01)
        self.doubleSpinBox_stop_condition.setProperty("value", 0.98)
        self.doubleSpinBox_stop_condition.setObjectName("doubleSpinBox_stop_condition")
        self.gridLayout.addWidget(self.doubleSpinBox_stop_condition, 3, 1, 1, 1)
        self.label_iteration = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_iteration.setObjectName("label_iteration")
        self.gridLayout.addWidget(self.label_iteration, 1, 0, 1, 1)
        self.doubleSpinBox_iteration = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget)
        self.doubleSpinBox_iteration.setDecimals(0)
        self.doubleSpinBox_iteration.setMaximum(999999.0)
        self.doubleSpinBox_iteration.setProperty("value", 100.0)
        self.doubleSpinBox_iteration.setObjectName("doubleSpinBox_iteration")
        self.gridLayout.addWidget(self.doubleSpinBox_iteration, 1, 1, 1, 1)
        self.groupBox_result = QtWidgets.QGroupBox(Form)
        self.groupBox_result.setGeometry(QtCore.QRect(20, 260, 331, 231))
        self.groupBox_result.setObjectName("groupBox_result")
        self.textBrowser_result = QtWidgets.QTextBrowser(self.groupBox_result)
        self.textBrowser_result.setGeometry(QtCore.QRect(10, 20, 311, 201))
        self.textBrowser_result.setObjectName("textBrowser_result")
        self.tabWidget_visualization = QtWidgets.QTabWidget(Form)
        self.tabWidget_visualization.setGeometry(QtCore.QRect(390, 20, 501, 471))
        self.tabWidget_visualization.setObjectName("tabWidget_visualization")
        self.train_graph = QtWidgets.QWidget()
        self.train_graph.setObjectName("train_graph")
        self.tabWidget_visualization.addTab(self.train_graph, "")
        self.test_graph = QtWidgets.QWidget()
        self.test_graph.setObjectName("test_graph")
        self.tabWidget_visualization.addTab(self.test_graph, "")

        self.retranslateUi(Form)
        self.tabWidget_visualization.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.groupBox_setting.setTitle(_translate("Form", "Setting"))
        self.label_stop_condition.setText(_translate("Form", "Stop Condition:"))
        self.label_learning_rate.setText(_translate("Form", "Learning Rate:"))
        self.pushButton_start.setText(_translate("Form", "Start"))
        self.label_file.setText(_translate("Form", "Select File: "))
        self.label_iteration.setText(_translate("Form", "Iteration:"))
        self.groupBox_result.setTitle(_translate("Form", "Results"))
        self.tabWidget_visualization.setTabText(self.tabWidget_visualization.indexOf(self.train_graph), _translate("Form", "Train Graph"))
        self.tabWidget_visualization.setTabText(self.tabWidget_visualization.indexOf(self.test_graph), _translate("Form", "Test Graph"))

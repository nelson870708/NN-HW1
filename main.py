# 將資料讀取到的資料進行前處理
# 傳給algorithm進行感知機演算法
# 將每個資料點的座標畫在Euclidean座標系統上
# 將weight所得出的直線畫在座標系統上
import glob
import os
import sys


# python library
import numpy as np
import matplotlib
from PyQt5.QtWidgets import *
from sklearn.model_selection import train_test_split

# my library
from HW1 import algorithm
from HW1.gui import Ui_Form
from HW1.result_plot import ResultFigure

matplotlib.use("Qt5Agg")  # 宣告使用QT5


def read_file():
    file_elementlist = []
    file_namelist = {}
    files_name = glob.glob(os.path.join(os.getcwd() + '\\dataset', '*.txt'))
    i = 0
    for file_name in files_name:
        file_namelist[os.path.basename(file_name)] = i
        file = open(file_name, 'r')
        elementlist = []
        for line in file:
            elementlist.append(list(map(float, line.split(' '))))
        file_elementlist.append(elementlist)
        i = i + 1
    return file_namelist, file_elementlist


class Main(QDialog, Ui_Form):
    def __init__(self):
        super(Main, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("HW1")
        self.setMinimumSize(0, 0)

        self.file_namelist, self.file_elementlist = read_file()
        self.comboBox_file.addItems(sorted(list(self.file_namelist)))
        self.graph1 = ResultFigure(width=100, height=100, dpi=100)
        self.graph2 = ResultFigure(width=100, height=100, dpi=100)
        self.file_changed()  # 畫第一筆資料之資料點
        # 加入train graph
        vlayout1 = QVBoxLayout(self.train)
        self.tabwidget1 = QTabWidget()
        vlayout1.addWidget(self.tabwidget1)
        self.gridlayout1 = QGridLayout(self.tabwidget1)
        self.gridlayout1.addWidget(self.graph1)
        # 加入test graph
        vlayout2 = QVBoxLayout(self.test_graph)
        self.tabwidget2 = QTabWidget()
        vlayout2.addWidget(self.tabwidget2)
        self.gridlayout2 = QGridLayout(self.tabwidget2)
        self.gridlayout2.addWidget(self.graph2)

        self.learning_rate = self.doubleSpinBox_learning_rate.value()
        self.iteration = self.doubleSpinBox_iteration.value()
        self.early_stop = self.doubleSpinBox_stop_condition.value()

        # 觸發事件才使用
        self.comboBox_file.currentTextChanged.connect(self.file_changed)
        self.doubleSpinBox_learning_rate.valueChanged.connect(self.learning_rate_changed)
        self.doubleSpinBox_iteration.valueChanged.connect(self.iteration_changed)
        self.doubleSpinBox_stop_condition.valueChanged.connect(self.early_stop_changed)
        self.pushButton_start.clicked.connect(self.start_buttom_click)

    def file_changed(self):
        self.textBrowser_result.setText('')
        X = np.asarray(self.file_elementlist[self.file_namelist[self.comboBox_file.currentText()]])[:, :2]
        y = np.asarray(self.file_elementlist[self.file_namelist[self.comboBox_file.currentText()]])[:, 2:]
        if self.comboBox_file.currentText() == 'perceptron1.txt' \
                or self.comboBox_file.currentText() == 'perceptron2.txt':
            self.train_X = X
            self.test_X = X
            self.train_y = y
            self.test_y = y
        else:
            self.train_X, self.test_X, self.train_y, self.test_y = train_test_split(X, y, train_size=2 / 3,
                                                                                    test_size=1 / 3)
        self.graph1.plot_point(self.train_X[:, :1], self.train_X[:, 1:], self.train_y, np.unique(self.train_y))
        self.graph2.plot_point(self.test_X[:, :1], self.test_X[:, 1:], self.test_y, np.unique(self.test_y))

        self.train_num_data = len(self.train_X)
        self.train_x_y_max = np.amax(self.train_X, axis=0)
        self.train_x_y_min = np.amin(self.train_X, axis=0)
        self.train_X = np.concatenate((np.negative(np.ones((self.train_num_data, 1))), self.train_X), axis=1)

        self.test_num_data = len(self.test_X)
        self.test_x_y_max = np.amax(self.test_X, axis=0)
        self.test_x_y_min = np.amin(self.test_X, axis=0)
        self.test_X = np.concatenate((np.negative(np.ones((self.test_num_data, 1))), self.test_X), axis=1)

    def learning_rate_changed(self):
        self.learning_rate = self.doubleSpinBox_learning_rate.value()

    def iteration_changed(self):
        self.iteration = self.doubleSpinBox_iteration.value()

    def early_stop_changed(self):
        self.early_stop = self.doubleSpinBox_stop_condition.value()

    def start_buttom_click(self):

        # perceptron algorithm(training)
        weight, train_accuracy = algorithm.perceptron_train(self.train_X, self.train_y, anskey=np.unique(self.train_y),
                                                            lr=self.learning_rate, it=int(self.iteration),
                                                            es=self.early_stop)

        # perceptron algorithm(testing)
        test_accuracy = algorithm.perceptron_test(self.test_X, self.test_y, anskey=np.unique(self.test_y),
                                                  weight=weight)
        self.textBrowser_result.append('The accuracy of train data is ' + str(train_accuracy) +
                                       '\nThe weight of the cell is ' + str(weight) +
                                       '\nThe accuracy of test data is ' + str(test_accuracy) + '\n')
        self.graph1.plot_line(weight, self.train_x_y_max, self.train_x_y_min)
        self.graph2.plot_line(weight, self.test_x_y_max, self.test_x_y_min)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = Main()
    main.show()
    sys.exit(app.exec_())

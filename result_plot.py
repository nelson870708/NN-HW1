# python library
import numpy as np
from PyQt5.QtWidgets import *
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure


class ResultFigure(FigureCanvas):
    def __init__(self, width=5, height=4, dpi=100):
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        super(ResultFigure, self).__init__(self.fig)  # 此句必不可少，否則不能顯示圖形
        self.axes = self.fig.add_subplot(111)
        FigureCanvas.setSizePolicy(self, QSizePolicy.Expanding, QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)

    def plot_point(self, x, y, label, color):
        self.axes.clear()
        self.axes.grid()
        for i in range(len(x)):
            if label[i] == color[0]:
                self.axes.plot(x[i], y[i], 'ro')
            elif label[i] == color[1]:
                self.axes.plot(x[i], y[i], 'bo')
            else:
                self.axes.plot(x[i], y[i], 'go')
        self.axes.autoscale(enable=False, axis='both', tight=None)  # 讓畫布大小固定
        self.draw()

    def plot_line(self, weight, x_y_max, x_y_min):
        a = weight[1]
        b = weight[2]
        c = -weight[0]  # -θ(theta) at the beginning
        if b != 0:
            x = np.linspace(x_y_min[0] - 2, x_y_max[0] + 2, num=100)
            y = (-a / b) * x + (-c / b)  # from ax + by + c = 0
        elif a != 0:
            y = np.linspace(x_y_min[1] - 2, x_y_max[1] + 2, num=100)
            x = (-b / a) * y + (-c / a)
        else:
            x = 0
            y = 0
            print('Error, no vector.')
        self.axes.plot(x, y)
        self.draw()

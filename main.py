import pyqtgraph as pg
import numpy as np
import bezier
from ingredient import *
import random
from PyQt5 import QtGui, QtCore, QtWidgets
import sys

pg.setConfigOption('background', 'w')
pg.setConfigOption('foreground', 'k')


def plot_ingredients(plot_widget, ingredients, colors=None):
    for i, ingredient in enumerate(ingredients):
        if colors is None:
            pen = pg.mkPen((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
        else:
            pen = pg.mkPen(colors[i])

        coords = bezier.BezierCurve(ingredient).coordinates

        plot = plot_widget.plot(pen=pen)
        plot.setData(coords)


def plot_average_ingredient(plot_widget, ingredients, segments=100, color=None):
    if color is None:
        pen = pg.mkPen((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
    else:
        pen = pg.mkPen(color)

    coords = average_ingredients(ingredients, segments)

    plot = plot_widget.plot(pen=pen)
    plot.setData(coords)


def average_ingredients(ingredients, segments=100):
    curves = [bezier.BezierCurve(ingredient) for ingredient in ingredients]
    return bezier.add_curves(curves, segments)


selected_ingredients = [waterbloom, terraria]


# selected_ingredients = all_ingredients

def update_graph(plot_widget, first=None, second=None, segments=50):
    plot_widget.clear()
    plot_widget.setXRange(-10, 10)
    plot_widget.setYRange(-10, 10)

    plot_widget.addItem(pg.InfiniteLine(angle=90))
    plot_widget.addItem(pg.InfiniteLine(angle=0))
    if first is not None:
        selected_ingredients[0] = all_ingredients[first]
    if second is not None:
        selected_ingredients[1] = all_ingredients[second]

    # plot_ingredients(plot_widget, selected_ingredients)
    plot_average_ingredient(plot_widget, selected_ingredients, segments)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    app = pg.mkQApp()

    window = QtWidgets.QWidget()
    v_box = QtWidgets.QVBoxLayout()

    plot_widget = pg.PlotWidget(None)
    v_box.addWidget(plot_widget)

    mixed_path_segments = 1000

    drop_down_1 = QtWidgets.QComboBox()
    drop_down_1.addItems(all_ingredient_names)
    drop_down_1.currentIndexChanged.connect(lambda x: update_graph(plot_widget, first=x, segments=mixed_path_segments))
    v_box.addWidget(drop_down_1)

    drop_down_2 = QtWidgets.QComboBox()
    drop_down_2.addItems(all_ingredient_names)
    drop_down_2.setCurrentIndex(1)
    drop_down_2.currentIndexChanged.connect(lambda x: update_graph(plot_widget, second=x, segments=mixed_path_segments))
    v_box.addWidget(drop_down_2)
    window.setLayout(v_box)

    update_graph(plot_widget)
    # plot_ingredients(plot_widget, all_ingredients)

    window.show()

    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()

import pyqtgraph as pg
import numpy as np
import bezier
from ingredient import *
import random
from PyQt5 import QtGui, QtCore, QtWidgets
import sys
from gui import IngredientSelectionWidget

pg.setConfigOption('background', 'w')
pg.setConfigOption('foreground', 'k')


def plot_ingredients(plot_widget, ingredients, colors=None, grind_levels=None):
    for i, ingredient in enumerate(ingredients):
        if colors is None:
            color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            pen = pg.mkPen(color)
            pen_dashed = pg.mkPen(color, style=QtCore.Qt.PenStyle.DashLine)
        else:
            pen = pg.mkPen(colors[i])
            pen_dashed = pg.mkPen(colors[i], style=QtCore.Qt.PenStyle.DashLine)

        coords_grinded, coords_unground = ingredient.get_grind_path(grind_levels[i])

        # print("grinded shape", coords_grinded.shape, "unground shape", coords_unground.shape)

        plot = plot_widget.plot(pen=pen)
        plot.setData(coords_grinded)

        plot_dashed = plot_widget.plot(pen=pen_dashed)
        plot_dashed.setData(coords_unground)


def plot_average_ingredient(plot_widget, ingredients, grind_levels=None, segments=100, color=None):
    if color is None:
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    pen = pg.mkPen(color)
    pen_dashed = pg.mkPen(color, style=QtCore.Qt.PenStyle.DashLine)

    grinded_coords, unground_coords = bezier.add_curves(ingredients, grind_levels, segments)

    plot = plot_widget.plot(pen=pen)
    plot.setData(grinded_coords)

    plot_dashed = plot_widget.plot(pen=pen_dashed)
    plot_dashed.setData(unground_coords)


selected_ingredients = all_ingredients[:2]
# selected_ingredients = all_ingredients
gui_parameters = {"first_ingredient": 0, "first_grind": 1,
                  "second_ingredient": 1, "second_grind": 1,
                  "combined_grind": 0}


def update_gui_parameters(**kwargs):
    for k, v in kwargs.items():
        gui_parameters[k] = v


def update_graph(plot_widget, segments=100, **kwargs):
    update_gui_parameters(**kwargs)

    plot_widget.clear()
    # plot_widget.setXRange(-8, 2)
    # plot_widget.setYRange(-8, 2)

    plot_widget.addItem(pg.InfiniteLine(angle=90, pen=pg.mkPen(127, 127, 127)))
    plot_widget.addItem(pg.InfiniteLine(angle=0, pen=pg.mkPen(127, 127, 127)))

    selected_ingredients[0] = all_ingredients[gui_parameters["first_ingredient"]]
    selected_ingredients[1] = all_ingredients[gui_parameters["second_ingredient"]]
    first_grind = gui_parameters["first_grind"]
    second_grind = gui_parameters["second_grind"]
    combined_grind = gui_parameters["combined_grind"]

    plot_ingredients(plot_widget, selected_ingredients, colors=["b", (255, 165, 0)],
                     grind_levels=[first_grind, second_grind])
    plot_average_ingredient(plot_widget, selected_ingredients, grind_levels=[first_grind, second_grind, combined_grind],
                            segments=segments, color=(0, 0, 0))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    app = pg.mkQApp()

    window = QtWidgets.QWidget()
    grid_layout = QtWidgets.QGridLayout()

    plot_widget = pg.PlotWidget(None)
    plot_widget.setXRange(-10, 10)
    plot_widget.setYRange(-10, 10)
    plot_widget.setAspectLocked(True)
    grid_layout.addWidget(plot_widget, 0, 0)

    first_ingredient_widget = IngredientSelectionWidget(0, 1)
    first_ingredient_widget.selected_ingredient_changed.connect(
        lambda x: update_graph(plot_widget, first_ingredient=x))
    first_ingredient_widget.grind_amount_changed.connect(
        lambda x: update_graph(plot_widget, first_grind=x / 100))
    grid_layout.addWidget(first_ingredient_widget, 1, 0)

    second_ingredient_widget = IngredientSelectionWidget(1, 1)
    second_ingredient_widget.selected_ingredient_changed.connect(
        lambda x: update_graph(plot_widget, second_ingredient=x))
    second_ingredient_widget.grind_amount_changed.connect(
        lambda x: update_graph(plot_widget, second_grind=x / 100))
    grid_layout.addWidget(second_ingredient_widget, 2, 0)

    combined_slider = QtWidgets.QSlider(QtCore.Qt.Orientation.Horizontal)
    combined_slider.setMinimum(0)
    combined_slider.setMaximum(100)
    combined_slider.setValue(0)
    combined_slider.valueChanged.connect(
        lambda x: update_graph(plot_widget, combined_grind=x / 100))
    grid_layout.addWidget(combined_slider, 3, 0)

    window.setLayout(grid_layout)

    update_graph(plot_widget)
    # plot_ingredients(plot_widget, all_ingredients)

    window.show()

    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QGuiApplication.instance().exec_()

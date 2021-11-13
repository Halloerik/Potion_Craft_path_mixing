from PyQt5 import QtWidgets, QtCore
from ingredient import all_ingredient_names


class IngredientSelectionWidget(QtWidgets.QWidget):

    grind_amount_changed = QtCore.pyqtSignal(int)
    selected_ingredient_changed = QtCore.pyqtSignal(int)

    def __init__(self, ingredient_index, ingredient_grind_level=1.0):
        super(IngredientSelectionWidget, self).__init__()

        h_box = QtWidgets.QHBoxLayout(self)
        h_box.setContentsMargins(0,0,0,0)
        drop_down = QtWidgets.QComboBox()
        drop_down.addItems(all_ingredient_names)
        drop_down.setCurrentIndex(ingredient_index)

        h_box.addWidget(drop_down)

        horizontal_slider = QtWidgets.QSlider(QtCore.Qt.Orientation.Horizontal)
        horizontal_slider.setMinimum(0)
        horizontal_slider.setMaximum(100)
        horizontal_slider.setSliderPosition(ingredient_grind_level * 100)
        h_box.addWidget(horizontal_slider)

        spin_box = QtWidgets.QSpinBox()
        spin_box.setMinimum(0)
        spin_box.setMaximum(100)
        spin_box.setValue(ingredient_grind_level * 100)
        h_box.addWidget(spin_box)

        spin_box.valueChanged.connect(horizontal_slider.setValue)
        horizontal_slider.valueChanged.connect(spin_box.setValue)

        drop_down.currentIndexChanged.connect(self.selected_ingredient_changed.emit)
        spin_box.valueChanged.connect(self.grind_amount_changed.emit)
        horizontal_slider.valueChanged.connect(self.grind_amount_changed.emit)
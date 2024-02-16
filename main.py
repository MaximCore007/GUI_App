import sys
from PySide6 import QtCore
from PySide6.QtWidgets import QApplication, QMainWindow, QSlider, QBoxLayout, QVBoxLayout, QHBoxLayout, QWidget, QLabel, QPushButton, QSpinBox, QFileDialog

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Slider Example")
        self.setGeometry(100, 100, 400, 200)

        main_layout = QVBoxLayout()
        main_widget = QWidget()
        main_widget.setLayout(main_layout)
        self.setCentralWidget(main_widget)
        
        hue_layout = QHBoxLayout()
        self.hue_slider = MyWindow.__createSlider("Hue", 0, 360, hue_layout)
        main_layout.addLayout(hue_layout)
        
        saturation_layout = QHBoxLayout()
        self.saturation_slider = MyWindow.__createSlider("Saturation", 0, 100, saturation_layout)
        main_layout.addLayout(saturation_layout)

        value_layout = QHBoxLayout()
        self.value_slider = MyWindow.__createSlider("Saturation", 0, 100, value_layout)
        main_layout.addLayout(value_layout)
        
        self.set_color_button = QPushButton("Set Color")
        main_layout.addWidget(self.set_color_button)
        self.set_color_button.clicked.connect(self.set_color)

        
        self.select_file_label = QLabel("Open 'elf' file")
        self.select_file_btn = QPushButton("Browse")
        self.select_file_layout = QVBoxLayout()
        self.select_file_layout.addWidget(self.select_file_label)
        self.select_file_layout.addWidget(self.select_file_btn)
        main_layout.insertLayout(0, self.select_file_layout)

        self.set_color_button.clicked.connect(self.set_color)
        self.select_file_btn.clicked.connect(self.open_file)

    @QtCore.Slot()
    def set_color(self):
        print(f'Color(hue: {self.hue_slider.value()}, saturation: {self.saturation_slider.value()}, value: {self.value_slider.value()})')

    @QtCore.Slot()
    def open_file(self):
        fileName = QFileDialog.getOpenFileName(self, str("Browser"), "~/", str("Image Files (*.txt)"))
        name = ""
        for file in fileName:
            name += file
        self.select_file_label.setText(fileName[0])

    def __createSlider(NameSlider: str, min: int, max: int, layout: QBoxLayout) -> QSlider:
        label = QLabel(NameSlider)
        layout.addWidget(label)

        value = QSpinBox()
        value.setMinimum(min)
        value.setMaximum(max)
        value.setButtonSymbols(QSpinBox.ButtonSymbols.NoButtons)

        slider = QSlider()
        slider.setOrientation(QtCore.Qt.Orientation.Horizontal)  # Horizontal orientation
        slider.setMinimum(min)
        slider.setMaximum(max)
        slider.setTickPosition(QSlider.TicksBelow)
        slider.setTickInterval(10)
        
        slider.valueChanged.connect(value.setValue)
        value.valueChanged.connect(slider.setValue)

        layout.addWidget(slider)
        layout.addWidget(value)

        slider.setValue(0)  # Initial value

        return slider

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())

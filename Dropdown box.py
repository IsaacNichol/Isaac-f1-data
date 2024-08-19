import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QComboBox, QVBoxLayout, QWidget

def create_main_window():
    # Create the main window
    window = QMainWindow()

    # Create a combo box (drop-down)
    comboBox = QComboBox()

    # Add items to the combo box
    comboBox.addItem("Option 1")
    comboBox.addItem("Option 2")
    comboBox.addItem("Option 3")
    comboBox.addItem("Option 4")

    # Define the function to handle combo box selection changes
    def on_combobox_changed(index):
        print(f"Selected index: {index}, Selected item: {comboBox.currentText()}")

    # Connect the combo box selection change event to the function
    comboBox.currentIndexChanged.connect(on_combobox_changed)

    # Set up the layout
    layout = QVBoxLayout()
    layout.addWidget(comboBox)

    # Set up the central widget
    central_widget = QWidget()
    central_widget.setLayout(layout)
    window.setCentralWidget(central_widget)

    # Show the window
    window.show()

    return window

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = create_main_window()
    sys.exit(app.exec_())

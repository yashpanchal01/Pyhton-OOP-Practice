import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout

class App(QWidget):
    def __init__(self):
        super().__init__()

        # Configure the main window
        self.setWindowTitle("My Powerful PyQt6 App")
        self.setGeometry(100, 100, 400, 300) # x, y, width, height

        # --- Layout ---
        # Layouts are used to arrange widgets
        layout = QVBoxLayout()

        # --- Widgets ---

        # Label
        self.label = QLabel("Hello, PyQt6!")
        layout.addWidget(self.label)

        # Button
        self.button = QPushButton("Click Me")
        # Connect the button's 'clicked' signal to a method (slot)
        self.button.clicked.connect(self.on_button_click)
        layout.addWidget(self.button)
        
        # Set the layout for the main window
        self.setLayout(layout)

    # --- Methods (Slots) ---

    def on_button_click(self):
        """
        This function is a 'slot' that responds to the button's 'clicked' signal.
        """
        print("Button was clicked!")
        self.label.setText("Button Clicked!")

# This is the standard entry point for a PyQt application
if __name__ == "__main__":
    app = QApplication(sys.argv) # The core application object
    window = App()
    window.show() # Make the window visible
    sys.exit(app.exec()) # Start the event loop and ensure a clean exit
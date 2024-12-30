import logging
from PySide6.QtWidgets import QApplication
from src.ui.main_window import MainWindow

# Configure logging
logging.basicConfig(
    level=logging.ERROR,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('app.log'),
        logging.StreamHandler()
    ]
)

if __name__ == "__main__":
    app = QApplication([])
    app.setStyle('Fusion')
    
    window = MainWindow()
    window.show()
    
    app.exec()
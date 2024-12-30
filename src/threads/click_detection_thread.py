import time
from PySide6.QtCore import QThread, Signal
from pynput.mouse import Button, Listener as MouseListener
from ..models.app_state import AppState

class ClickDetectionThread(QThread):
    click_detected = Signal()

    def __init__(self, app_state: AppState):
        super().__init__()
        self.app_state = app_state
        self.running = True

    def run(self):
        def on_click(x, y, button, pressed):
            if button == Button.left and not pressed and self.app_state.mouse_state:
                self.click_detected.emit()

        with MouseListener(on_click=on_click) as listener:
            while self.running:
                time.sleep(0.1)
            listener.stop() 
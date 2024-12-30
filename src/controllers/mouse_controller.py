from src.utils.singleton import SingletonMeta
from pynput.mouse import Button, Controller
import threading
from src.utils.logger import logger

class MouseController(metaclass=SingletonMeta):
    def __init__(self):
        self._mouse = Controller()
        self._lock = threading.Lock()
        self._pressed = False

    def press(self):
        with self._lock:
            if not self._pressed:
                self._mouse.press(Button.left)
                self._pressed = True
                logger.debug('Mouse button pressed')

    def release(self):
        with self._lock:
            if self._pressed:
                self._mouse.release(Button.left)
                self._pressed = False
                logger.debug('Mouse button released')

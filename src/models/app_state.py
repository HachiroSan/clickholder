import threading
from dataclasses import dataclass

class AppState:
    """Thread-safe class representing the application state."""
    def __init__(self):
        self._running = True
        self._mouse_state = False
        self._alt_pressed = False
        self._lock = threading.Lock()

    @property
    def running(self) -> bool:
        with self._lock:
            return self._running

    @running.setter
    def running(self, value: bool):
        with self._lock:
            self._running = value

    @property
    def mouse_state(self) -> bool:
        with self._lock:
            return self._mouse_state

    @mouse_state.setter
    def mouse_state(self, value: bool):
        with self._lock:
            self._mouse_state = value

    @property
    def alt_pressed(self) -> bool:
        with self._lock:
            return self._alt_pressed

    @alt_pressed.setter
    def alt_pressed(self, value: bool):
        with self._lock:
            self._alt_pressed = value 
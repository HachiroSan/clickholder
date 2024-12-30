import time
import queue
import logging
from typing import Optional
from PySide6.QtCore import QThread, Signal
from ..controllers.mouse_controller import MouseController
from ..models.app_state import AppState

logger = logging.getLogger(__name__)

class MouseControlThread(QThread):
    state_changed = Signal(bool)
    error_occurred = Signal(str)

    MAX_RETRY_ATTEMPTS = 3
    RETRY_DELAY = 1.0
    PROCESS_DELAY = 0.01

    def __init__(self, app_state: AppState, command_queue: queue.Queue):
        super().__init__()
        self.app_state = app_state
        self.command_queue = command_queue
        self.mouse_controller = MouseController()
        self._last_error_time: Optional[float] = None
        self._error_count = 0

    def run(self):
        while self.app_state.running:
            try:
                self._process_commands()
                self._update_mouse_state()
                time.sleep(self.PROCESS_DELAY)
                
                if self._error_count > 0:
                    self._error_count = 0
                    logger.info("Mouse control recovered from previous errors")
                    
            except Exception as e:
                self._handle_error(e)

    def _handle_error(self, error: Exception):
        current_time = time.time()
        
        if self._last_error_time and (current_time - self._last_error_time) > 60:
            self._error_count = 0
            
        self._error_count += 1
        self._last_error_time = current_time
        
        error_msg = f"Error in mouse control thread: {str(error)}"
        logger.error(error_msg)
        self.error_occurred.emit(error_msg)

        try:
            self.mouse_controller.release()
        except Exception as e:
            logger.error(f"Failed to release mouse button: {e}")

        if self._error_count >= self.MAX_RETRY_ATTEMPTS:
            logger.critical("Too many errors, stopping mouse control")
            self.app_state.mouse_state = False
            self.state_changed.emit(False)
        else:
            time.sleep(self.RETRY_DELAY * self._error_count)

    def _process_commands(self):
        try:
            command = self.command_queue.get_nowait()
            if command == "TOGGLE_MOUSE":
                self.app_state.mouse_state = not self.app_state.mouse_state
                logger.debug(f'Mouse state toggled to: {self.app_state.mouse_state}')
                self.state_changed.emit(self.app_state.mouse_state)
        except queue.Empty:
            pass

    def _update_mouse_state(self):
        if self.app_state.mouse_state:
            self.mouse_controller.press()
        else:
            self.mouse_controller.release() 
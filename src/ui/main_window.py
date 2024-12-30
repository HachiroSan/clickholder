import queue
import logging
from PySide6.QtWidgets import (QMainWindow, QWidget, QVBoxLayout, QLabel, 
                              QSystemTrayIcon, QMenu, QMessageBox)
from PySide6.QtCore import Qt, QEvent, QUrl
from PySide6.QtGui import QIcon, QCursor
from PySide6.QtMultimedia import QSoundEffect
from pynput.keyboard import Key, Listener as KeyboardListener
from pynput.mouse import Button, Listener as MouseListener

from ..models.app_state import AppState
from ..utils.config_manager import ConfigManager
from ..threads.mouse_control_thread import MouseControlThread
from ..threads.click_detection_thread import ClickDetectionThread
from .status_widget import StatusWidget
from .settings_widget import SettingsWidget
from .instructions_widget import InstructionsWidget
from src.utils.resource_path import resource_path
from ..version import __version_full__

logger = logging.getLogger(__name__)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.config_manager = ConfigManager()
        self.app_state = AppState()
        self.command_queue = queue.Queue()
        
        self._init_ui()
        self._init_threads()
        self._init_listeners()

    def _init_ui(self):
        self._setup_window()
        self._setup_ui_components()
        self._setup_tray()
        self._setup_sound()

    def _setup_window(self):
        self.setWindowTitle("Click Holder")
        self.setFixedSize(300, 420)
        self.setWindowIcon(QIcon(resource_path("assets/icon.ico")))
        self._apply_stylesheet()

    def _apply_stylesheet(self):
        self.setStyleSheet("""
            QMainWindow { 
                background-color: #1e1e1e; 
            }
            QWidget { 
                font-family: 'Segoe UI', Arial;
                color: #ffffff;
            }
            QPushButton {
                background-color: #2d2d2d;
                border: 1px solid #3d3d3d;
                border-radius: 8px;
                padding: 8px 12px;
                font-size: 12px;
                color: #ffffff;
                margin: 4px;
                min-height: 20px;
                max-height: 20px;
            }
            QPushButton:hover { 
                background-color: #3d3d3d;
                border: 1px solid #4d4d4d;
            }
            QPushButton:checked { 
                background-color: #007AFF;
                border: none;
            }
            .footer {
                color: #666666;
                font-size: 11px;
                padding: 12px;
            }
        """)

    def _setup_ui_components(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)
        main_layout.setSpacing(8)
        main_layout.setContentsMargins(12, 12, 12, 12)

        # Add status widget
        self.status_widget = StatusWidget()
        main_layout.addWidget(self.status_widget)

        # Add settings widget
        self.settings_widget = SettingsWidget()
        self.settings_widget.key_bind_btn.clicked.connect(self.settings_widget.start_key_binding)
        self.settings_widget.sound_enabled_btn.clicked.connect(self._on_sound_button_clicked)
        main_layout.addWidget(self.settings_widget)

        # Add instructions widget
        self.instructions_widget = InstructionsWidget()
        main_layout.addWidget(self.instructions_widget)
        
        # Add footer
        footer = QLabel(f"Developed by Hachiro | v{__version_full__}")
        footer.setAlignment(Qt.AlignCenter)
        footer.setProperty("class", "footer")
        footer.setStyleSheet("""
            color: #666666;
            font-size: 10px;
            padding: 2px;
            margin: 0px;
            margin-top: 4px;
        """)
        main_layout.addWidget(footer)

    def _setup_sound(self):
        self.beep = QSoundEffect()
        self.beep.setSource(QUrl.fromLocalFile(resource_path("assets/beep.wav")))
        self.beep.setVolume(0.5)

    def _setup_tray(self):
        self.tray_icon = QSystemTrayIcon(self)
        self.tray_icon.setIcon(QIcon(resource_path("assets/icon.ico")))
        self.tray_icon.setToolTip("Click Holder")
        
        self.tray_menu = QMenu()
        
        self.status_action = self.tray_menu.addAction("Status: INACTIVE")
        self.status_action.setEnabled(False)
        self.tray_menu.addSeparator()
        
        self.show_action = self.tray_menu.addAction("Show")
        self.show_action.triggered.connect(self.show_normal)
        
        self.minimize_action = self.tray_menu.addAction("Minimize to Tray")
        self.minimize_action.triggered.connect(self.hide)
        
        self.tray_menu.addSeparator()
        
        self.sound_action = self.tray_menu.addAction("Sound Enabled")
        self.sound_action.setCheckable(True)
        self.sound_action.setChecked(self.config_manager.get_config().get('sound_enabled', True))
        self.sound_action.triggered.connect(self._on_tray_sound_toggle)
        
        self.tray_menu.addSeparator()
        
        self.quit_action = self.tray_menu.addAction("Quit")
        self.quit_action.triggered.connect(self.quit_application)
        
        self.tray_icon.setContextMenu(self.tray_menu)
        self.tray_icon.activated.connect(self._handle_tray_activation)
        self.tray_icon.show()

    def _init_threads(self):
        self.mouse_thread = MouseControlThread(self.app_state, self.command_queue)
        self.mouse_thread.state_changed.connect(self._update_status)
        self.mouse_thread.start()

        self.click_detection_thread = ClickDetectionThread(self.app_state)
        self.click_detection_thread.click_detected.connect(self._handle_single_click)
        self.click_detection_thread.start()

    def _init_listeners(self):
        self.keyboard_listener = KeyboardListener(
            on_press=self._on_key_press,
            on_release=self._on_key_release
        )
        self.mouse_listener = MouseListener(on_click=self._on_mouse_click)
        
        self.keyboard_listener.start()
        self.mouse_listener.start()

    def _handle_tray_activation(self, reason):
        if reason == QSystemTrayIcon.ActivationReason.DoubleClick:
            self.restore_window()
        elif reason == QSystemTrayIcon.ActivationReason.Trigger:
            self.tray_menu.popup(QCursor.pos())

    def restore_window(self):
        self.show()
        self.setWindowState(Qt.WindowActive)
        self.activateWindow()
        self.raise_()

    def show_normal(self):
        if self.isMinimized():
            self.showNormal()
        self.restore_window()

    def _on_sound_button_clicked(self):
        is_enabled = self.settings_widget.sound_enabled_btn.isChecked()
        self.sound_action.setChecked(is_enabled)
        self.config_manager.update_config('sound_enabled', is_enabled)

    def _on_tray_sound_toggle(self):
        is_enabled = self.sound_action.isChecked()
        self.settings_widget.update_sound_state(is_enabled)

    def _on_key_press(self, key):
        if self.settings_widget.is_binding:
            key_str = str(key)
            self.settings_widget.update_key_binding(key_str)
            return

        config = self.config_manager.get_config()
        if str(key) == config.get('trigger_key', 'Key.alt_l'):
            self.app_state.alt_pressed = True

    def _on_key_release(self, key):
        config = self.config_manager.get_config()
        if str(key) == config.get('trigger_key', 'Key.alt_l'):
            self.app_state.alt_pressed = False

    def _on_mouse_click(self, x, y, button, pressed):
        if button == Button.left and not pressed and self.app_state.alt_pressed:
            self.command_queue.put("TOGGLE_MOUSE")

    def _handle_single_click(self):
        if self.app_state.mouse_state:
            self.command_queue.put("TOGGLE_MOUSE")

    def _update_status(self, state):
        self.status_widget.update_status(state)
        self.status_action.setText(f"Status: {'HOLDING' if state else 'LISTENING'}")
        
        if self.config_manager.get_config().get('sound_enabled', True):
            self.beep.play()

    def changeEvent(self, event):
        if event.type() == QEvent.WindowStateChange:
            if self.isMinimized():
                self.hide()
                self.tray_icon.showMessage(
                    "Click Holder",
                    "Application minimized to tray. Double-click tray icon to restore.",
                    QSystemTrayIcon.Information,
                    2000
                )
                event.accept()

    def closeEvent(self, event):
        reply = QMessageBox.question(
            self, 
            'Confirmation',
            'Do you want to quit Click Holder?',
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No
        )

        if reply == QMessageBox.Yes:
            self.quit_application()
        else:
            event.ignore()
            self.hide()
            self.tray_icon.showMessage(
                "Click Holder",
                "Application minimized to tray. Double-click tray icon to restore.",
                QSystemTrayIcon.Information,
                2000
            )

    def quit_application(self):
        self.app_state.running = False
        self.mouse_thread.wait()
        self.keyboard_listener.stop()
        self.mouse_listener.stop()
        self.click_detection_thread.running = False
        self.click_detection_thread.wait() 
from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel
from ..utils.config_manager import ConfigManager

class SettingsWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.config_manager = ConfigManager()
        self.is_binding = False
        self.setFixedHeight(110)
        self._init_ui()

    def _init_ui(self):
        layout = QVBoxLayout(self)
        layout.setSpacing(4)
        layout.setContentsMargins(4, 0, 4, 0)

        settings_header = QLabel("Settings")
        settings_header.setStyleSheet("color: #8e8e93; font-size: 11px; margin-bottom: 2px;")
        layout.addWidget(settings_header)

        buttons_container = QWidget()
        buttons_layout = QVBoxLayout(buttons_container)
        buttons_layout.setSpacing(6)
        buttons_layout.setContentsMargins(0, 0, 0, 0)

        config = self.config_manager.get_config()
        
        self.key_bind_btn = QPushButton(f"🔑 Trigger Key: {self._format_key_name(config.get('trigger_key', 'Key.alt_l'))}")
        self.key_bind_btn.setFixedHeight(32)
        buttons_layout.addWidget(self.key_bind_btn)

        self.sound_enabled_btn = QPushButton(
            "🔊 Sound Enabled" if config.get('sound_enabled', True) else "🔇 Sound Disabled"
        )
        self.sound_enabled_btn.setCheckable(True)
        self.sound_enabled_btn.setChecked(config.get('sound_enabled', True))
        self.sound_enabled_btn.setFixedHeight(32)
        buttons_layout.addWidget(self.sound_enabled_btn)

        buttons_layout.addStretch()
        layout.addWidget(buttons_container)

    def _format_key_name(self, key_str: str) -> str:
        """Convert key string to a friendly display name.""" 
        key_map = {
            "Key.alt_l": "Left Alt",
            "Key.alt_r": "Right Alt",
            "Key.ctrl_l": "Left Ctrl",
            "Key.ctrl_r": "Right Ctrl",
            "Key.shift_l": "Left Shift",
            "Key.shift_r": "Right Shift",
            "Key.enter": "Enter",
            "Key.space": "Space",
            "Key.tab": "Tab",
            "Key.esc": "Escape"
        }
        return key_map.get(key_str, key_str.replace("Key.", "").title())

    def start_key_binding(self):
        if not self.is_binding:
            self.is_binding = True
            self.key_bind_btn.setText("🎯 Press any key...")
            self.key_bind_btn.setStyleSheet("""
                background-color: #007AFF;
                border: none;
                color: white;
            """)

    def update_key_binding(self, key_str: str):
        self.config_manager.update_config('trigger_key', key_str)
        self.key_bind_btn.setText(f"🔑 Trigger Key: {self._format_key_name(key_str)}")
        self.key_bind_btn.setStyleSheet("")
        self.is_binding = False

    def update_sound_state(self, is_enabled: bool):
        self.sound_enabled_btn.setChecked(is_enabled)
        self.sound_enabled_btn.setText("🔊 Sound Enabled" if is_enabled else "🔇 Sound Disabled")
        self.config_manager.update_config('sound_enabled', is_enabled) 
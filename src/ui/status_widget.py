from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel
from PySide6.QtCore import Qt

class StatusWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFixedHeight(90)
        self._init_ui()

    def _init_ui(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 8, 0, 0)
        layout.setSpacing(4)
        
        title = QLabel("Status")
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("color: #8e8e93; font-size: 11px; margin-bottom: 2px;")
        layout.addWidget(title)
        
        self.status_label = QLabel("LISTENING")
        self.status_label.setAlignment(Qt.AlignCenter)
        self.status_label.setMaximumHeight(60)
        self._update_status_style(False)
        layout.addWidget(self.status_label)

    def _update_status_style(self, is_active: bool):
        color = "#34c759" if is_active else "#ff3b30"
        self.status_label.setStyleSheet(f"""
            font-size: 28px;
            font-weight: bold;
            color: {color};
            padding: 12px;
            background-color: #2d2d2d;
            border-radius: 12px;
            margin: 4px;
            qproperty-alignment: AlignCenter;
        """)

    def update_status(self, state: bool):
        status_text = "HOLDING" if state else "LISTENING"
        self.status_label.setText(status_text)
        self._update_status_style(state) 
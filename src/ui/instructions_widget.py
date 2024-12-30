from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel
from PySide6.QtCore import Qt

class InstructionsWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFixedHeight(120)
        self._init_ui()

    def _init_ui(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(4, 0, 4, 0)
        layout.setSpacing(4)

        help_header = QLabel("How to Use")
        help_header.setStyleSheet("color: #8e8e93; font-size: 11px; margin-bottom: 2px;")
        layout.addWidget(help_header)

        instructions = QLabel(
            "1. Hold trigger key + click to start holding\n"
            "2. Click again to stop holding\n"
            "3. Double-click tray icon to show window"
        )
        instructions.setStyleSheet("""
            color: #cccccc;
            font-size: 12px;
            line-height: 1.4;
            padding: 12px;
            background-color: #2d2d2d;
            border-radius: 6px;
        """)
        instructions.setAlignment(Qt.AlignLeft)
        instructions.setWordWrap(True)

        layout.addWidget(instructions) 
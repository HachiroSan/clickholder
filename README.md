# 🖱️ Click Holder

<div align="center">
  <img src="https://raw.githubusercontent.com/HachiroSan/clickholder/master/assets/icon.png" alt="Click Holder Icon" width="128" height="128">
</div>

A sleek utility designed to automate holding left click action in games. Originally made for DayZ but can be used in other games.

<div align="center">

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![PySide6](https://img.shields.io/badge/PySide6-Latest-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

</div>

## ✨ Features

- 🖱️ **Smart Click Holding**: Automatically holds left mouse button
- ⌨️ **Customizable Trigger**: Configure your preferred trigger key (default: Left Alt)
- 🔊 **Audio Feedback**: Clear sound indicators for state changes
- 🔲 **System Tray Integration**: Runs quietly in your system tray
- 🌙 **Modern Dark Theme**: Easy on the eyes during long gaming sessions

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher

### Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/click-holder.git
cd click-holder
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

### Running the Application

Launch the application with:
```bash
python main.py
```

## 🎮 How to Use

1. **Launch**: Start the app - it automatically minimizes to system tray
2. **Activate**: Hold the trigger key (Left Alt by default) and click
3. **Deactivate**: Click again to stop the auto-hold
4. **Configure**: Double-click tray icon to access settings
5. **Customize**: Adjust trigger key and sound preferences

## 🏗️ Project Structure

```
.
├── src/
│   ├── controllers/    # Mouse and keyboard control logic
│   ├── models/        # Data structures and state management
│   ├── utils/         # Helper functions and utilities
│   ├── ui/           # User interface components
│   └── threads/      # Background processing threads
├── assets/
│   ├── sounds/       # Audio feedback files
│   └── icons/        # Application icons
├── main.py           # Application entry point
└── requirements.txt  # Project dependencies
```

## ⚙️ Configuration Options

| Setting | Description | Default |
|---------|-------------|---------|
| Trigger Key | Key that activates click holding | Left Alt |
| Sound Feedback | Toggle audio notifications | Enabled |
| Start Minimized | Launch directly to tray | Enabled |

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## ⚠️ Disclaimer

This tool is designed for convenience in games. Please use responsibly and in accordance with game terms of service.

## 🐛 Known Issues

- May require running as administrator for some games

## 📫 Support

If you encounter any issues or have suggestions:
- Open an issue on GitHub

---
<div align="center">
Made with ❤️ for the DayZ community
</div> 
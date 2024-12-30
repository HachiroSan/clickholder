# 🖱️ Click Holder

<div align="center">
  <img src="https://raw.githubusercontent.com/HachiroSan/clickholder/master/assets/icon.png" alt="Click Holder Icon" width="128" height="128">
</div>

A simple and sleek utility designed to automate holding left click action in games. Originally made for DayZ but can be used in other games.

## 🌟 Why Click Holder?

- **User-Friendly**: Simple interface with system tray integration
- **Customizable**: Configure your own trigger key and sound preferences
- **Open Source**: Transparent, community-driven development

<div align="center">

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![PySide6](https://img.shields.io/badge/PySide6-Latest-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)
![Version](https://img.shields.io/badge/version-0.1.0--beta-orange)

</div>

## ✨ Features

- 🖱️ **Smart Click Holding**: Automatically holds left mouse button when trigger key is held
- ⌨️ **Customizable Trigger**: Configure your preferred trigger key (default: Left Alt)
- 🔊 **Audio Feedback**: Clear sound indicators for state changes
- 🔲 **System Tray Integration**: Runs quietly in your system tray
- 🌙 **Modern Dark Theme**: Easy on the eyes during long gaming sessions

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher

### Installation

#### For Users
There are two ways to install Click Holder:

1. **Installer Version**
   - Download `ClickHolder_Setup.exe` from [Releases](https://github.com/yourusername/click-holder/releases)
   - Run the installer and follow the instructions
   - The application will be installed with start menu shortcuts

2. **Portable Version**
   - Download `ClickHolder_[version].exe` from [Releases](https://github.com/yourusername/click-holder/releases)
   - No installation needed - just run the executable
   - Can be moved to any location or USB drive

> ⚠️ **Antivirus Notice**
> 
> Some antivirus software may flag this application as suspicious because:
> - It monitors keyboard and mouse inputs
> - It's a PyInstaller-packaged executable
> 
> This is a false positive. The application is completely safe and open source.
> You can:
> - View the source code on GitHub
> - Build from source yourself
> - Add the application to your antivirus exclusions

#### For Developers
1. Clone the repository:
```bash
git clone https://github.com/yourusername/click-holder.git
cd click-holder
```

2. Install dependencies:
```bash
# For basic usage and development
pip install -r requirements.txt

# For development tools (linting, testing, etc.)
pip install -r requirements/dev.txt

# For documentation
pip install -r requirements/docs.txt
```

3. Run the application:
```bash
python run.py
```

4. Build executable (optional):
```bash
# Build both portable executable and installer
python scripts/build.py
```

Or build individually:
```bash
# Build portable executable only
pyinstaller --onefile --windowed --icon=assets/icon.ico --add-data "assets;assets" run.py --name ClickHolder
```

# Build installer only (requires Inno Setup)
"C:\Program Files (x86)\Inno Setup 6\ISCC.exe" installer.iss
```
The outputs will be:
- Portable: `dist/ClickHolder.exe`
- Installer: `Output/ClickHolder_Setup_0.1.0-beta.exe`

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

> 📦 **Release Process**
> 
> When creating a new release:
> 1. Build the portable executable using PyInstaller
> 2. Create the installer using Inno Setup
> 3. Test both versions thoroughly
> 4. Create a new GitHub release
> 5. Upload both `ClickHolder.exe` and `ClickHolder_Setup.exe`
> 
> Note: Never commit build artifacts (`dist/`, `Output/`) to the repository

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
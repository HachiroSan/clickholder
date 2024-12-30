# 🖱️ Click Holder

<div align="center">
  <img src="https://raw.githubusercontent.com/HachiroSan/clickholder/master/assets/icon.png" alt="Click Holder Icon" width="128" height="128">
</div>

A simple utility designed to automate holding left click action in games. Originally made for DayZ but can be used in other games.

<div align="center">

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![PySide6](https://img.shields.io/badge/PySide6-Latest-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)
![Version](https://img.shields.io/badge/version-0.1.0--beta-orange)

</div>

## ✨ Features

- 🖱️ **Auto Click Holding**: Automatically holds left mouse button when trigger key is held
- ⌨️ **Customizable Trigger**: Configure your preferred trigger key (default: Left Alt)
- 🔊 **Audio Feedback**: Clear sound indicators for state changes
- 🔲 **System Tray Integration**: Runs quietly in your system tray

## 🎮 How to Use

1. **Launch**: Start the app - it automatically minimizes to system tray
2. **Activate**: Hold the trigger key (Left Alt by default) and left click
3. **Deactivate**: Left click again to stop the auto-hold
4. **Configure**: Double-click tray icon to access settings
5. **Customize**: Adjust trigger key and sound preferences


## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher

### Installation

There are two ways to use Click Holder:

1. **Installer Version**
   - Download `ClickHolder_Setup.exe` from [Releases](https://github.com/yourusername/click-holder/releases)
   - Run the installer and follow the instructions
   - The application will be installed with start menu shortcuts

2. **Portable Version**
   - Download `ClickHolder_[version].exe` from [Releases](https://github.com/yourusername/click-holder/releases)
   - No installation needed - just run the executable

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

> 🔧 **For Developers**
> 
> If you want to contribute or build from source, see [DEVELOPMENT.md](DEVELOPMENT.md)

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
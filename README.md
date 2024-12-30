# Click Holder

A simple utility to help with repetitive mouse actions in DayZ.

## Features

- Hold left mouse button automatically
- Configurable trigger key (default: Left Alt)
- Sound feedback on state changes
- System tray integration
- Modern dark UI theme

## Installation

1. Make sure you have Python 3.8+ installed
2. Clone this repository
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the application:
   ```bash
   python main.py
   ```

2. The application will start and minimize to system tray
3. Hold the trigger key (default: Left Alt) and click to start holding the mouse button
4. Click again to stop holding
5. Double-click the tray icon to show the main window
6. Use the settings to:
   - Change the trigger key
   - Enable/disable sound feedback

## Project Structure

```
src/
├── controllers/     # Mouse and keyboard control
├── models/         # Data models
├── utils/          # Utility classes
├── ui/            # UI components
└── threads/       # Background threads
assets/           # Sound and icon files
```

## License

MIT License 
# Development Guide

## 🛠️ Setup Development Environment

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

## 🏗️ Building

### Build both portable and installer:
```bash
python scripts/build.py
```

### Build portable executable only:
```bash
pyinstaller --onefile --windowed --icon=assets/icon.ico --add-data "assets;assets" run.py --name ClickHolder
```

## 🧪 Testing

1. Run tests:
```bash
pytest
```

2. Run linting:
```bash
pylint src/
```

## 📝 Code Style

- Follow PEP 8 guidelines
- Use meaningful variable and function names
- Add comments for complex logic
- Update documentation when needed

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📚 Project Structure

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
├── tests/            # Test files
└── requirements/     # Dependency files
```

For more details about contributing, see [CONTRIBUTING.md](CONTRIBUTING.md). 
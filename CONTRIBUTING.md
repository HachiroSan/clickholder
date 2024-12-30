# Contributing to Click Holder

First off, thank you for considering contributing to Click Holder! It's people like you that make Click Holder such a great tool.

## Development Process

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## Build Process

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Install Inno Setup 6 (for building installer)

3. Build both portable and installer:
```bash
python scripts/build.py
```

## Code Style

- Follow PEP 8 guidelines
- Use meaningful variable and function names
- Add comments for complex logic
- Update documentation when needed

## Testing

- Test your changes thoroughly
- Ensure both portable and installer versions work
- Test on different Windows versions if possible

## Pull Request Process

1. Update the README.md with details of changes if needed
2. Update the version numbers in src/version.py if needed
3. The PR will be merged once you have the sign-off of a maintainer

### Our Pledge
We pledge to make participation in our project a harassment-free experience for everyone.

### Our Standards

Examples of behavior that contributes to creating a positive environment include:
- Using welcoming and inclusive language
- Being respectful of differing viewpoints
- Gracefully accepting constructive criticism
- Focusing on what is best for the community

### Our Responsibilities

Project maintainers are responsible for clarifying the standards of acceptable behavior and are expected to take appropriate and fair corrective action in response to any instances of unacceptable behavior. 
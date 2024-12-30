import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {
    "packages": ["PySide6", "logging"],
    "excludes": ["tkinter", "unittest"],
    "include_files": [
        ("assets/", "assets/"),  # Include assets directory
    ],
    "include_msvcr": True,
}

base = None
if sys.platform == "win32":
    base = "Win32GUI"  # Use this to hide console window

setup(
    name="Click Holder",
    version="1.0.0",
    description="Auto Click Holder for Games",
    options={"build_exe": build_exe_options},
    executables=[
        Executable(
            "run.py",
            base=base,
            icon="assets/icon.ico",
            target_name="ClickHolder.exe"
        )
    ]
) 
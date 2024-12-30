import os
import shutil
import subprocess
from pathlib import Path
import sys

# Add src to path so we can import version
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src.version import __version__, __version_full__

def clean_build_dirs():
    """Clean up build directories"""
    print("🧹 Cleaning build directories...")
    dirs_to_clean = ['build', 'dist', 'Output']
    for dir_name in dirs_to_clean:
        if os.path.exists(dir_name):
            shutil.rmtree(dir_name)
            print(f"   Cleaned {dir_name}/")

def update_inno_version():
    """Update version in Inno Setup script"""
    print("\n📝 Updating version information...")
    with open('installer.iss', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Update version definitions
    content = content.replace(
        '#define MyAppVersion "0.1.0"',
        f'#define MyAppVersion "{__version__}"'
    )
    content = content.replace(
        '#define MyAppVersionFull "0.1.0-beta"',
        f'#define MyAppVersionFull "{__version_full__}"'
    )
    
    with open('installer.iss', 'w', encoding='utf-8') as f:
        f.write(content)

def build_portable():
    """Build portable executable using PyInstaller"""
    print("\n🚀 Building portable executable...")
    try:
        subprocess.run([
            'pyinstaller',
            '--clean',
            '--onefile',
            '--windowed',
            '--icon=assets/icon.ico',
            '--add-data', 'assets;assets',
            '--name', 'ClickHolder',
            'run.py'
        ], check=True)
        print("✅ Portable executable built successfully")
        return True
    except subprocess.CalledProcessError as e:
        print("❌ Failed to build portable executable")
        print(f"Error: {e}")
        return False

def build_installer():
    """Build installer using Inno Setup"""
    print("\n📦 Building installer...")
    try:
        # Path to Inno Setup Compiler
        iscc_path = r"C:\Program Files (x86)\Inno Setup 6\ISCC.exe"
        
        if not os.path.exists(iscc_path):
            print("❌ Inno Setup Compiler not found!")
            print("Please install Inno Setup 6 or update the path in build.py")
            return False
        
        subprocess.run([
            iscc_path,
            "installer.iss"
        ], check=True)
        print("✅ Installer built successfully")
        return True
    except subprocess.CalledProcessError as e:
        print("❌ Failed to build installer")
        print(f"Error: {e}")
        return False

def main():
    print(f"🔨 Starting build process for version {__version_full__}...")
    
    # Clean build directories
    clean_build_dirs()
    
    # Update version in Inno Setup script
    update_inno_version()
    
    # Build portable executable
    if not build_portable():
        return
    
    # Rename the portable executable to include version
    if os.path.exists('dist/ClickHolder.exe'):
        versioned_name = f'dist/ClickHolder_{__version_full__}.exe'
        if os.path.exists(versioned_name):
            os.remove(versioned_name)
        shutil.copy2('dist/ClickHolder.exe', versioned_name)
    
    # Build installer
    if not build_installer():
        return
    
    print("\n✨ Build completed successfully!")
    print("\nOutputs:")
    print(f"  📁 Portable: dist/ClickHolder.exe")
    print(f"  📁 Portable (versioned): dist/ClickHolder_{__version_full__}.exe")
    print(f"  📁 Installer: Output/ClickHolder_Setup_{__version_full__}.exe")

if __name__ == "__main__":
    main() 
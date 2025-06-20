#!/usr/bin/env python3
"""
Setup script for Social FIT Data Intelligence POC

This script helps set up the environment and dependencies for the data intelligence platform.
"""

import os
import sys
import subprocess
import shutil
from pathlib import Path

def check_python_version():
    """Check if Python version is compatible."""
    if sys.version_info < (3, 8):
        print("❌ Python 3.8 or higher is required")
        print(f"Current version: {sys.version}")
        return False
    print(f"✅ Python version: {sys.version}")
    return True

def install_dependencies():
    """Install required dependencies."""
    print("\n📦 Installing dependencies...")
    
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✅ Dependencies installed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Error installing dependencies: {e}")
        return False

def create_directories():
    """Create necessary directories."""
    print("\n📁 Creating directories...")
    
    directories = ["logs", "data", "reports"]
    
    for directory in directories:
        Path(directory).mkdir(exist_ok=True)
        print(f"✅ Created directory: {directory}")

def setup_environment():
    """Set up environment variables file."""
    print("\n⚙️  Setting up environment...")
    
    env_file = Path(".env")
    env_example = Path("env_example.txt")
    
    if env_file.exists():
        print("✅ .env file already exists")
        return True
    
    if env_example.exists():
        shutil.copy(env_example, env_file)
        print("✅ Created .env file from template")
        print("📝 Please edit .env file with your Supabase credentials")
        return True
    else:
        print("❌ env_example.txt not found")
        return False

def verify_data_files():
    """Verify that data files exist."""
    print("\n📊 Verifying data files...")
    
    data_files = [
        "data/social_fit_students.csv",
        "data/social_fit_instagram_en.csv"
    ]
    
    missing_files = []
    for file_path in data_files:
        if Path(file_path).exists():
            print(f"✅ Found: {file_path}")
        else:
            print(f"❌ Missing: {file_path}")
            missing_files.append(file_path)
    
    if missing_files:
        print(f"\n⚠️  Missing data files: {len(missing_files)}")
        print("Please ensure all data files are present in the data/ directory")
        return False
    
    return True

def run_tests():
    """Run the test suite."""
    print("\n🧪 Running tests...")
    
    try:
        subprocess.check_call([sys.executable, "test_etl.py"])
        return True
    except subprocess.CalledProcessError:
        print("❌ Tests failed")
        return False

def main():
    """Main setup function."""
    print("=" * 60)
    print("🚀 SOCIAL FIT DATA INTELLIGENCE POC SETUP")
    print("=" * 60)
    
    # Check Python version
    if not check_python_version():
        sys.exit(1)
    
    # Create directories
    create_directories()
    
    # Install dependencies
    if not install_dependencies():
        print("❌ Setup failed at dependency installation")
        sys.exit(1)
    
    # Setup environment
    if not setup_environment():
        print("❌ Setup failed at environment setup")
        sys.exit(1)
    
    # Verify data files
    if not verify_data_files():
        print("❌ Setup failed at data verification")
        sys.exit(1)
    
    # Run tests
    if not run_tests():
        print("❌ Setup failed at testing")
        sys.exit(1)
    
    print("\n" + "=" * 60)
    print("✅ SETUP COMPLETED SUCCESSFULLY!")
    print("=" * 60)
    print("\n📋 Next steps:")
    print("1. Edit .env file with your Supabase credentials")
    print("2. Run: python main.py")
    print("3. View dashboard: python dashboard.py")
    print("\n📚 For more information, see README.md")

if __name__ == "__main__":
    main() 
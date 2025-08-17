#!/bin/bash

# Advanced DDoS Testing Tool - Installation Script
# This script installs all dependencies and sets up the environment

echo "🚀 Installing Advanced DDoS Testing Tool..."

# Check if Python 3 is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3.7+ first."
    exit 1
fi

# Check Python version
python_version=$(python3 -c 'import sys; print(".".join(map(str, sys.version_info[:2])))')
required_version="3.7"

if [ "$(printf '%s\n' "$required_version" "$python_version" | sort -V | head -n1)" != "$required_version" ]; then
    echo "❌ Python 3.7+ is required. Current version: $python_version"
    exit 1
fi

echo "✅ Python version: $python_version"

# Install pip if not available
if ! command -v pip3 &> /dev/null; then
    echo "📦 Installing pip..."
    sudo apt-get update
    sudo apt-get install -y python3-pip
fi

# Upgrade pip
echo "⬆️  Upgrading pip..."
python3 -m pip install --upgrade pip

# Install dependencies
echo "📦 Installing dependencies..."
pip3 install -r requirements.txt

# Make the script executable
chmod +x ddos.py

# Create necessary directories
mkdir -p logs
mkdir -p reports

echo "✅ Installation completed successfully!"
echo ""
echo "🎯 Usage:"
echo "   python3 ddos.py"
echo ""
echo "📚 Documentation: README.md"
echo "⚙️  Configuration: config.json"
echo ""
echo "⚠️  Remember: Use only for authorized testing!"
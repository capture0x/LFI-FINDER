#!/bin/bash
set -e

CHROMEDRIVER_URL="https://edgedl.me.gvt1.com/edgedl/chrome/chrome-for-testing/128.0.6613.113/linux64/chromedriver-linux64.zip"
CHROMEDRIVER_ZIP="chromedriver-linux64.zip"
CHROMEDRIVER_DIR="chromedriver-linux64"

if command -v google-chrome &> /dev/null; then
    echo "Detected Google Chrome, downloading compatible chromedriver..."
    curl -sL "$CHROMEDRIVER_URL" -o "$CHROMEDRIVER_ZIP"
    unzip -o "$CHROMEDRIVER_ZIP"
    sudo mv "$CHROMEDRIVER_DIR/chromedriver" /usr/bin/chromedriver
    sudo chown root:root /usr/bin/chromedriver
    sudo chmod +x /usr/bin/chromedriver
    rm -f "$CHROMEDRIVER_ZIP"
    rm -rf "$CHROMEDRIVER_DIR"
    echo "Chromedriver installed successfully."
else
    echo "Google Chrome not found. Please install Chrome first."
    exit 1
fi

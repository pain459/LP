#!/bin/bash

# Variables
APPIMAGE_URL="https://inkscape.org/release/inkscape-1.1.2/AppImage/inkscape-1.1.2-x86_64.AppImage"  # Replace with the actual URL
APPIMAGE_NAME="inkscape.AppImage"
INSTALL_DIR="$HOME/.local/bin"
DESKTOP_FILE="$HOME/.local/share/applications/org.inkscape.Inkscape.desktop"
EXTRACT_DIR="squashfs-root"

# Function to check if a command exists
command_exists () {
    command -v "$1" >/dev/null 2>&1
}

# Check for required tools
if ! command_exists wget || ! command_exists chmod || ! command_exists mkdir || ! command_exists mv || ! command_exists cp; then
    echo "Error: Required tools (wget, chmod, mkdir, mv, cp) are not installed."
    exit 1
fi

# Step 1: Download the AppImage
echo "Downloading Inkscape AppImage..."
wget -O "$APPIMAGE_NAME" "$APPIMAGE_URL"

# Step 2: Make the AppImage executable
echo "Making the AppImage executable..."
chmod +x "$APPIMAGE_NAME"

# Step 3: Move it to the appropriate path
echo "Moving the AppImage to $INSTALL_DIR..."
mkdir -p "$INSTALL_DIR"
mv "$APPIMAGE_NAME" "$INSTALL_DIR/"

# Step 4: Extract the AppImage
echo "Extracting the AppImage..."
"$INSTALL_DIR/$APPIMAGE_NAME" --appimage-extract

# Step 5: Copy the desktop launcher
echo "Copying the desktop launcher..."
mkdir -p "$(dirname "$DESKTOP_FILE")"
cp "$EXTRACT_DIR/usr/share/applications/org.inkscape.Inkscape.desktop" "$DESKTOP_FILE"

# Step 6: Edit the desktop launcher
echo "Editing the desktop launcher..."
sed -i "s|Exec=.*|Exec=$INSTALL_DIR/$APPIMAGE_NAME %F|" "$DESKTOP_FILE"

# Step 7: Give the .desktop file executable permissions
echo "Setting executable permissions for the desktop file..."
chmod +x "$DESKTOP_FILE"

# Step 8: Remove the extracted directory
echo "Cleaning up..."
rm -rf "$EXTRACT_DIR"

# Completion message
echo "Inkscape installation completed! You can find it in your application menu."

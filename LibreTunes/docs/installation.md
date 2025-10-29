# Installation Guide

> **Quick Install**: See the [main README](../README.md) for the fastest way to get started.

## System Requirements

- **Python**: 3.10 or newer
- **GTK**: 4.0 or newer  
- **GStreamer**: 1.0 or newer
- **Operating System**: Linux

## Step-by-Step Installation

### 1. Clone the Repository
```bash
git clone https://github.com/FredXYZ-cmd/LibreTunes.git
cd LibreTunes
```
### 2. Install Dependencies
**Ubuntu/Debian**
```
sudo apt update
sudo apt install python3-gi python3-gi-cairo gir1.2-gtk-4.0 gir1.2-adw-1 python3-pip
```
**Fedora**
```
sudo dnf install python3-gobject gtk4 libadwaita python3-pip
```
**Arch Linux**
```
sudo pacman -S python-gobject gtk4 libadwaita python-pip
```
### 3. Install Python Dependencies
```
pip install -r requirements.txt
```
### 4. Run LibreTunes
```
python -m libretunes

```

### Troubleshooting

### Common Issues

"Gl.Repository Error": Gtk not found

Ensure GTK4 development packages are installed

**On Ubuntu:** 
```
sudo apt install libgtk-4-dev
```
**On Fedora:**
```
sudo dnf install libgtk-4-dev
```
**on Arch:**
```
sudo pacman -S libgtk-4-dev
```
"No module named 'gi"
Install PyGObject:

**Ubuntu**: 
```
sudo apt install python3-gi
```
**Fedora**: 
```
sudo dnf install python3-gi
```
**Arch**:
```
sudo pacman -S python3-gi
```
"Audio not working"

Install GStreamer plugins

**Ubuntu**: 
```
sudo apt install gstreamer1.0-plugins-good
```
**Fedora**: 
```
sudo dnf install gstreamer1.0-plugins-good
```
**Arch**: 
```
sudo pacman -S gstreamer1.0-plugins-good

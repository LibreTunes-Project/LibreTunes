# LibreTunes 🎵🌱 (IN DEVELOPMENT)

<div align="center">

*A modern, open-source music player for Linux*

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![Python](https://img.shields.io/badge/Python-3.10+-yellow.svg)](https://python.org)
[![GTK](https://img.shields.io/badge/GTK-4.0-green.svg)](https://gtk.org)
[![Platform: Linux](https://img.shields.io/badge/Platform-Linux-lightgrey.svg)](https://kernel.org)

<br>

**LibreTunes is a privacy-focused, modern music player built for the Linux desktop**

</div>

## ✨ Features

- 🎶 **Local Music Library** - Play your existing music collection
- 🎨 **Modern GTK4 Interface** - Beautiful Libadwaita design
- 🔍 **Smart Organization** - Automatic metadata and album art
- 🎛️ **High-Quality Audio** - Support for MP3, FLAC, OGG, OPUS, and more
- 🔒 **Privacy First** - Your music, your data, no tracking
- 🚀 **Lightweight** - Fast and resource-efficient

## 📸 Screenshots

*Screenshots coming soon!*

## 🚀 Getting Started

### Prerequisites
- Python 3.10 or newer
- GTK 4.0
- GStreamer

### Installation & Running

```bash
# Clone the repository
git clone https://github.com/FredXYZ-cmd/LibreTunes.git
cd LibreTunes

# Run directly (no installation needed!)
PYTHONPATH=src python src/libretunes/main.py
```

**System Dependencies**

Arch Linux:

```bash
sudo pacman -S python-gobject gtk4 libadwaita gstreamer gst-plugins-good gst-plugins-bad gst-plugins-ugly
```
Ubuntu/Debian:

```bash
sudo apt install python3-gi python3-gi-cairo gir1.2-gtk-4.0 gir1.2-adw-1 gir1.2-gst-plugins-base-1.0 gstreamer1.0-plugins-good gstreamer1.0-plugins-bad gstreamer1.0-plugins-ugly
```

Fedora:

```bash
sudo dnf install python3-gobject gtk4 libadwaita gstreamer1-devel gstreamer1-plugins-base gstreamer1-plugins-good gstreamer1-plugins-bad-free
```

**Alternative Methods**

```bash

pip install -e .  # If your system allows pip installations
libretunes

```




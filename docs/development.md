# Development Guide

Welcome to the LibreTunes development guide! This document will help you set up your development environment and contribute to the project.

## 🚀 Quick Start

### Prerequisites
- **Python** 3.10 or newer
- **GTK 4.0** development libraries
- **GStreamer** 1.0 or newer
- **Git** for version control

### One-Time Setup
```bash
# Clone and setup
git clone https://github.com/FredXYZ-cmd/LibreTunes.git
cd LibreTunes

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate  # Windows

# Install development dependencies
pip install -r requirements.txt
pip install -e .

# Run the application
python -m libretunes

```


## 🏗️ Project Architecture

```text
src/libretunes/
├── main.py                 # Application entry point
├── application.py          # Main application class
├── player/
│   ├── __init__.py
│   ├── audio_engine.py    # GStreamer playback engine
│   └── playlist.py        # Playlist management
├── library/
│   ├── __init__.py
│   ├── manager.py         # Music library management
│   ├── scanner.py         # File system scanning
│   └── metadata.py        # Audio metadata extraction
├── ui/
│   ├── __init__.py
│   ├── main_window.py     # Main application window
│   ├── components/        # Reusable UI components
│   │   ├── sidebar.py
│   │   ├── player_controls.py
│   │   └── library_view.py
│   └── widgets/           # Custom GTK widgets
├── utils/
│   ├── __init__.py
│   ├── file_utils.py      # File operations
│   └── logging.py         # Logging configuration
└── config/
    ├── __init__.py
    └── settings.py        # Application settings

```

## 🔧 Development Environent

**Dependencies by Distribution**

**🐧Ubuntu/Debian:**

```bash

sudo apt update
sudo apt install \
    python3-gi \
    python3-gi-cairo \
    gir1.2-gtk-4.0 \
    gir1.2-adw-1 \
    gir1.2-gst-plugins-base-1.0 \
    gstreamer1.0-plugins-good \
    gstreamer1.0-plugins-bad \
    gstreamer1.0-plugins-ugly \
    python3-pip

```

**🎩Fedora:**

```bash

sudo dnf install \
    python3-gobject \
    gtk4 \
    libadwaita \
    gstreamer1-devel \
    gstreamer1-plugins-base \
    gstreamer1-plugins-good \
    gstreamer1-plugins-bad-free \
    python3-pip

```

**⚡Arch Linux:**

```bash

sudo pacman -S \
    python-gobject \
    gtk4 \
    libadwaita \
    gstreamer \
    gst-plugins-good \
    gst-plugins-bad \
    gst-plugins-ugly \
    python-pip

```

**Development Dependencies**

```bash

# Install additional development tools
pip install black flake8 pytest pytest-gtk

```

## 🧪 Testing

**Running Tests**

```bash

# Run all tests
pytest

# Run tests with coverage
pytest --cov=src/libretunes

# Run specific test file
pytest tests/test_player.py

# Run tests in watch mode (requires pytest-watch)
ptw

```

**Test Structure**

```text
tests/
├── unit/
│   ├── test_player.py
│   ├── test_library.py
│   └── test_metadata.py
├── integration/
│   └── test_application.py
└── fixtures/
    └── test_audio_files/

```

**Writing Tests**

```python

def test_audio_playback():
    """Test basic audio playback functionality."""
    player = AudioEngine()
    player.load("test_audio.mp3")
    player.play()
    assert player.is_playing == True
    player.stop()

```

## 🛠️Development Workflow

**1. Code Style**

We use automated code formatting and linting

```bash

# Format code
black src/

# Check code style
flake8 src/

# Type checking (when implemented)
mypy src/

```

**2. Git Workflow**

```bash

# Create feature branch
git checkout -b feat/new-feature

# Make changes and test
git add .
git commit -m "feat: add new feature"

# Keep branch updated
git fetch origin
git rebase origin/main

# Push and create PR
git push origin feat/new-feature

```

**3. Debugging**

GTK Debugging

```bash

# Enable GTK debug output
G_MESSAGES_DEBUG=all python -m libretunes

# Inspect GTK widgets
GTK_DEBUG=interactive python -m libretunes

```

GStreamer Debugging

```bash

# Enable GStreamer debug output
GST_DEBUG=3 python -m libretunes

# Specific GStreamer element debugging
GST_DEBUG=playbin:5 python -m libretunes

```

## 🎯 Core Components

**Audio Engine (GStreamer)**

```python

class AudioEngine:
    def __init__(self):
        self.playbin = Gst.ElementFactory.make("playbin", "player")
        self.setup_audio_sink()
    
    def play(self, uri: str):
        self.playbin.set_property("uri", uri)
        self.playbin.set_state(Gst.State.PLAYING)

```

**Library Management**

```python

class LibraryManager:
    def scan_directory(self, path: str):
        """Scan directory for audio files and extract metadata."""
        for file_path in self.find_audio_files(path):
            metadata = self.extract_metadata(file_path)
            self.add_to_library(metadata)

```

**UI Components**

```python

class MainWindow(Adw.ApplicationWindow):
    def __init__(self):
        super().__init__()
        self.setup_ui()
        self.connect_signals()
    
    def setup_ui(self):
        self.header = Gtk.HeaderBar()
        self.sidebar = Sidebar()
        self.content = LibraryView()

```

## 📦 Building and Distribution

**Local Build**

```bash
# Build package
python setup.py sdist bdist_wheel

# Install locally
pip install dist/libretunes-*.whl
```

**Flatpak (In the future)**

```bash

# Build Flatpak
flatpak-builder build-dir org.libretunes.LibreTunes.json

# Install Flatpak
flatpak install build-dir/org.libretunes.LibreTunes.flatpak
```

## 🐛 Common Issues and Solutions

**"GI.RepositoryError:
Gtk not found:"**

•Install GTK 4.0 development packages

•Ensure *gobject-introspection* is installed

**No Module named "gi"**

•Install *python3-gi* package

•Check Python virtual environment

**Audio Playback issues**

•Install GStreamer plugins
```text
gst-plugins-good
gst-plugins-bad
gst-plugins-ugly
```

•Check audio file permissions and formats

**UI not rendering properly**

•Ensure *libadwaita* is installed

•Check GTK theme compatibility

## 🤝 Contributing

**Before Submitting**

•Run *black* and *flake8*

•Test your changes thoroughly

•Update documentation if needed

•Add tests for new features

**Code Review Checklist**

•Code follows project style guide 

•Tests are included and passing

•Documentation is updated

•No breaking changes introduced

## 📚 Additional Resources
•[GTK 4 Documentation](https://docs.gtk.org/gtk4/)

•[GStreamer Documentation](https://gstreamer.freedesktop.org/documentation/?gi-language=c)

•[Python GI Documentation](https://pygobject.gnome.org/)

•[LibreTunes Contributing Guide](../CONTRIBUTING.md)


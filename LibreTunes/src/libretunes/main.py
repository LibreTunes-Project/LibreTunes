#!/usr/bin/env python3
"""
LibreTunes - Main entry point
"""

import sys
import gi

# Configure GTK and GStreamer
gi.require_version("Gtk", "4.0")
gi.require_version("Adw", "1")
gi.require_version("Gst", "1.0")

from gi.repository import Gtk, Gio, Adw, Gst
from libretunes.application import LibreTunesApplication


def main():
    """Main function - entry point of the application."""
    # Initialize GStreamer
    Gst.init(sys.argv)
    
    # Create and run the application
    app = LibreTunesApplication()
    
    # Run the application
    return app.run(sys.argv)


if __name__ == "__main__":
    sys.exit(main())

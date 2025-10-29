"""
Main application class for LibreTunes
"""

from gi.repository import Gtk, Gio, Adw, Gst
from libretunes.ui.main_window import LibreTunesWindow


class LibreTunesApplication(Adw.Application):
    """Main application class."""
    
    def __init__(self):
        super().__init__(
            application_id="org.libretunes.LibreTunes",
            flags=Gio.ApplicationFlags.FLAGS_NONE
        )
        
    def do_activate(self):
        """Called when the application is activated."""
        # Create the main window
        win = LibreTunesWindow(application=self)
        win.present()

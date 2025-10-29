"""
Main application window
"""

from gi.repository import Gtk, Adw, Gio, Gst


class LibreTunesWindow(Adw.ApplicationWindow):
    """Main application window."""
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        # Configure the window
        self.set_title("LibreTunes")
        self.set_default_size(800, 600)
        
        # Create the main layout
        self.setup_ui()
        
    def setup_ui(self):
        """Setup the user interface."""
        # Main box
        main_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.set_content(main_box)
        
        # Header bar
        header = Gtk.HeaderBar()
        main_box.append(header)
        
        # Title
        title = Gtk.Label()
        title.set_label("🎵 LibreTunes")
        title.add_css_class("title")
        header.set_title_widget(title)
        
        # Play button
        play_button = Gtk.Button()
        play_button.set_icon_name("media-playback-start-symbolic")
        play_button.connect("clicked", self.on_play_clicked)
        header.pack_start(play_button)
        
        # Status label
        self.status_label = Gtk.Label()
        self.status_label.set_label("Ready to play music!")
        self.status_label.set_margin_top(20)
        self.status_label.set_margin_bottom(20)
        main_box.append(self.status_label)
        
        # Setup audio player
        self.setup_audio_player()
        
    def setup_audio_player(self):
        """Setup the GStreamer audio player."""
        self.player = Gst.ElementFactory.make("playbin", "player")
        
    def on_play_clicked(self, button):
        """Called when play button is clicked."""
        # For now, play a test sound or local file
        self.status_label.set_label("🎶 Playing music...")
        
        # You can replace this with a path to your test audio file
        test_file = "/usr/share/sounds/ubuntu/stereo/message.ogg"  # Ubuntu sound
        
        try:
            self.player.set_property("uri", f"file://{test_file}")
            self.player.set_state(Gst.State.PLAYING)
        except Exception as e:
            self.status_label.set_label(f"❌ Error: {str(e)}")

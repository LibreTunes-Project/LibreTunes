"""
Audio playback engine using GStreamer
"""

from gi.repository import Gst


class AudioEngine:
    """Main audio playback engine."""
    
    def __init__(self):
        self.player = None
        self.setup_player()
        
    def setup_player(self):
        """Setup the GStreamer player."""
        self.player = Gst.ElementFactory.make("playbin", "player")
        
    def play_file(self, file_path):
        """Play an audio file."""
        if self.player:
            uri = f"file://{file_path}"
            self.player.set_property("uri", uri)
            self.player.set_state(Gst.State.PLAYING)
            return True
        return False
        
    def stop(self):
        """Stop playback."""
        if self.player:
            self.player.set_state(Gst.State.NULL)
            
    def pause(self):
        """Pause playback."""
        if self.player:
            self.player.set_state(Gst.State.PAUSED)
            
    def resume(self):
        """Resume playback."""
        if self.player:
            self.player.set_state(Gst.State.PLAYING)

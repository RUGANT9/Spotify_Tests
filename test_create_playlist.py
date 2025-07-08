from pywinauto.application import Application
from pywinauto.keyboard import send_keys
import pytest, time

SPOTIFY_PATH = r"C:\Users\<YOUR_USER>\AppData\Local\Microsoft\WindowsApps\Spotify.exe"


def connect_spotify():
    try:
        return Application(backend="uia").connect(title_re="Spotify.*", timeout=10)
    except Exception:
        return Application(backend="uia").start(SPOTIFY_PATH)


@pytest.fixture(scope="function")
def spotify_app():
    app = connect_spotify()
    time.sleep(4)
    win = app.window(title_re="Spotify.*")
    win.set_focus()
    yield win


def test_create_new_playlist(spotify_app):
    """
    Open the 'Create Playlist' option in the sidebar to make a new playlist.
    """
    send_keys("{TAB 15}{ENTER}")   # Navigate to sidebar's 'Create Playlist' button
    time.sleep(3)
    send_keys("{ESC}")             # Close modal (optional)


def test_rename_new_playlist(spotify_app):
    """
    After creating a playlist, rename it using the context menu.
    """
    send_keys("{TAB 15}{ENTER}")   # Create playlist again
    time.sleep(3)
    send_keys("+{F10}")            # Shift+F10 = context menu
    time.sleep(1)
    send_keys("{DOWN 2}{ENTER}")   # Select 'Rename'
    time.sleep(1)
    send_keys("My New Playlist{ENTER}")  # New name
    time.sleep(1)


def test_add_track_to_playlist(spotify_app):
    """
    Search for a track and add it to the newly created playlist.
    """
    send_keys("^l")                 # Focus search
    send_keys("Coldplay Paradise{ENTER}")
    time.sleep(4)
    send_keys("{TAB 5}")            # Navigate to first song
    send_keys("+{F10}")             # Open context menu
    time.sleep(1)
    send_keys("{DOWN 3}{ENTER}")    # Add to Playlist
    time.sleep(1)
    send_keys("{DOWN}{ENTER}")      # Select first playlist in the list
    time.sleep(2)

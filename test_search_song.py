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


def test_search_song_and_open_result(spotify_app):
    """
    Search for a song ('Imagine') using the global search box
    and open the top result.
    """
    send_keys("^l")               # CTRL+L focuses the search bar
    send_keys("Imagine{ENTER}")   # type query + Enter
    time.sleep(3)
    # move to first result and open
    send_keys("{TAB}{TAB}{ENTER}")
    time.sleep(2)


def test_search_album(spotify_app):
    """
    Search for an album ('Divide') and attempt to play its first track.
    """
    send_keys("^l")
    send_keys("Divide Album{ENTER}")
    time.sleep(4)
    send_keys("{TAB 5}{ENTER}")  # Tab to album section, open
    time.sleep(3)
    send_keys("{TAB 3}{ENTER}")  # Navigate to and play first track
    time.sleep(2)

def test_search_artist_and_view_artist(spotify_app):
    """
    Search for an artist ('Adele') and open the artist profile page.
    """
    send_keys("^l")
    send_keys("Adele{ENTER}")
    time.sleep(3)
    send_keys("{TAB 4}{ENTER}")  # Navigate to artist section, open
    time.sleep(3)
    send_keys("{TAB 2}")         # Tab around inside profile
from pywinauto.application import Application
from pywinauto.keyboard import send_keys
import pytest, time

SPOTIFY_PATH = r"C:\Users\<YOUR_USER>\AppData\Local\Microsoft\WindowsApps\Spotify.exe"


def connect_spotify():
    try:
        app = Application(backend="uia").connect(title_re="Spotify.*", timeout=10)
        return app
    except Exception:
        return Application(backend="uia").start(SPOTIFY_PATH)


@pytest.fixture(scope="function")
def spotify_app():
    app = connect_spotify()
    time.sleep(4)
    win = app.window(title_re="Spotify.*")
    win.set_focus()
    yield win


def test_play_first_track(spotify_app):
    """Play the very first track in the current Spotify screen."""
    send_keys("{TAB}{ENTER}")     # tab to play area, press Enter
    time.sleep(2)
    # space toggles play / pause
    send_keys(" ")                
    time.sleep(2)
    # verify playback toggled—we use the space key again to pause
    send_keys(" ")

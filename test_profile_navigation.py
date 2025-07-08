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


def test_open_user_profile(spotify_app):
    """Navigate to the user profile via keyboard shortcuts."""
    # Alt+F opens the file-style menu, arrow up to profile icon, Enter
    send_keys("%f{UP}{ENTER}")
    time.sleep(3)
    # Verify by sending TAB a few times then ESC to close
    send_keys("{TAB}{TAB}{ESC}")

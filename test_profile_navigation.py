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

def test_navigate_to_profile_settings(spotify_app):
    """Open profile and navigate to Account Settings using keyboard."""
    send_keys("%f{UP}{ENTER}")           # Open user menu
    time.sleep(2)
    send_keys("{TAB 2}{ENTER}")          # Navigate to Account settings or similar
    time.sleep(3)
    send_keys("{ESC}")                   # Close settings screen

def test_log_out_flow_from_profile(spotify_app):
    """Navigate through the profile menu and trigger logout flow (without confirming)."""
    send_keys("%f{UP}{ENTER}")           # Open profile dropdown
    time.sleep(2)
    send_keys("{TAB 5}")                 # Tab to Logout or equivalent
    send_keys("{ENTER}")                 # Trigger logout (you can cancel in real test)
    time.sleep(1)
    send_keys("{ESC}")                   # Cancel logout or close dialog
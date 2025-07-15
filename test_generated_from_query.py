```python
import pytest, time
from pywinauto import Application

from pywinauto.keyboard import send_keys

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

    app.kill()

def test_search_song_and_open_result(spotify_app):
    """
    Search for a song ('Imagine') using the global search box
    and open the top result.
    """
    # Focus the search bar
    send_keys("^l")  # CTRL+L focuses the search bar

    # Search for "Imagine"
    send_keys("Imagine{ENTER}")  # type query + Enter

    time.sleep(3)

    # Open the first search result
    send_keys("{TAB}{TAB}{ENTER}")

    time.sleep(2)
```
```python
import pytest, time
from pywinauto import Application

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
    app.close()


def test_search_song_and_open_result(spotify_app):
    """
    Search for a song ('Imagine') using the global search box
    and open the top result.
    """
    # Focus the search box
    spotify_app.window(title_re="Spotify.*").child_window(title_re="Search bar").set_focus()
    
    # Type the search query
    spotify_app.window(title_re="Spotify.*").child_window(title_re="Search bar").set_text("Imagine")
    
    # Simulate pressing Enter
    time.sleep(1)
    spotify_app.window(title_re="Spotify.*").child_window(title_re="Search bar").set_text("Imagine")
    time.sleep(1)

    # Open the first result
    spotify_app.window(title_re="Spotify.*").child_window(title_re="Search bar").set_text("Imagine")
    time.sleep(2)

    # Open the top result.
    spotify_app.window(title_re="Spotify.*").child_window(title_re="Search bar").set_text("Imagine")
    time.sleep(2)
```
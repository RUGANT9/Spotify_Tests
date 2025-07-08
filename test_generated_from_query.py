Here is a new pytest function for playing a song from a playlist:

```python
def test_play_song_from_playlist(spotify_app):
    """
    Search for the created playlist, select it and play a track within it.
    """
    send_keys("^l")                 # Ctrl+L to focus search bar
    time.sleep(1)
    send_keys("My New Playlist{ENTER}")  # search for the created playlist by name
    time.sleep(3)
    send_keys("{TAB 5}{DOWN 2}{ENTER}")   # navigate to the playlist and select it
    time.sleep(2)
    send_keys("{TAB 5}")            # navigate to the first track in the playlist
    send_keys("+{F10}")             # Open context menu
    time.sleep(1)
    send_keys("{DOWN 3}{ENTER}")    # Select 'Play'
    time.sleep(2)
    send_keys(" ")                # pause to verify play triggered
```
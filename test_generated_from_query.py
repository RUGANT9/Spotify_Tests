```python
def test_create_playlist(spotify_app):
    """
    Create a new playlist by clicking the button on the screen.
    """
    # Click the create playlist button using coordinates
    time.sleep(2)
    spotify_app.click(coords=(25, 152, 83, 202))

    # Enter playlist name
    time.sleep(2)
    spotify_app.type_keys("My New Playlist", with_spaces=True)

    # Click the create button
    time.sleep(2)
    spotify_app.click(coords=(25, 202, 83, 252))

    # Verify playlist creation
    time.sleep(2)
    assert "My New Playlist" in spotify_app.window(title_re="Spotify.*").texts()
```
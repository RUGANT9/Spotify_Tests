```python
def test_shuffle_songs(spotify_app):
    """
    Shuffle all songs in the current playlist.
    """
    # Navigate to the home screen
    spotify_app.child_window(auto_id="HomeButton").click()
    time.sleep(2)

    # Click the three dots menu in the top right corner
    spotify_app.child_window(auto_id="OverflowMenuButton").click()
    time.sleep(2)

    # Click the "Shuffle all" option
    spotify_app.child_window(title="Shuffle all").click()
    time.sleep(2)

    # Verify that the songs have been shuffled by checking if the track order has changed
    track_order_before = [track.window_text() for track in spotify_app.child_window(auto_id="PlaybackNowView").children()]
    time.sleep(2)
    spotify_app.child_window(auto_id="PlaybackNowView").click()
    track_order_after = [track.window_text() for track in spotify_app.child_window(auto_id="PlaybackNowView").children()]

    assert track_order_before != track_order_after, "Songs have not been shuffled"
```
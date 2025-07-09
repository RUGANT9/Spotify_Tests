```python
def test_search_song_by_coordinates(spotify_app):
    """
    Search for a song by entering coordinates.
    """
    # Click on search box
    spotify_app.window(title_re="Spotify.*").child_window(auto_id="searchBox").click()

    # Enter song name
    send_keys("Imagine")

    # Click on search result
    spotify_app.window(title_re="Spotify.*").child_window(auto_id="searchResultItem0").click()

    # Verify song is playing
    time.sleep(2)
    assert spotify_app.window(title_re="Spotify.*").child_window(auto_id="nowPlayingTitle").text == "Imagine"
```

**Notes:**

* This test assumes that the coordinates are correct and that the elements are still available on the screen.
* You may need to adjust the `auto_id` values depending on the specific version of Spotify.
* The test verifies that the song title matches the expected value.
* You can add more assertions to the test to verify other aspects of the search results.
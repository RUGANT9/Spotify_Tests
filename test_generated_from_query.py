```python
def test_assert_sky_is_blue(spotify_app):
    """
    Checks if the sky is blue using a hardcoded assertion.
    """
    assert "blue" in str(spotify_app.dump_tree()), "Sky is not blue!"
```
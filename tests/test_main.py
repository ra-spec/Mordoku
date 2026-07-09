"""Tests for main module."""

from mordoku.main import hello


def test_hello():
    """Test the hello function."""
    assert hello() == "Hello, World!"
    assert hello("Alice") == "Hello, Alice!"

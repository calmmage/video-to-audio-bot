import pytest


def test_imports():
    from video_to_audio_bot.lib import MyApp, MyHandler

    assert MyApp
    assert MyHandler

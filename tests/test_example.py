from youtube_tts_datagen.example import get_greeting


def test_get_greeting() -> None:
    assert get_greeting() == "Hello world"

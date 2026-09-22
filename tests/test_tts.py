from speech.pyttsx3_engine import Pyttsx3Engine


def test_pyttsx3_engine_initializes():
    engine = Pyttsx3Engine(rate=180, volume=1.0)
    assert engine is not None
    assert engine.rate == 180

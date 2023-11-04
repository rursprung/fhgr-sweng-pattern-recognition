import pyttsx3


class TtsOffline:
    """
    TTS implementation which uses the library `pyttsx3` which works fully offline
    """

    def __init__(self):
        self._engine = pyttsx3.init()

    def speak(self, text: str) -> None:
        self._engine.say(text)
        self._engine.runAndWait()

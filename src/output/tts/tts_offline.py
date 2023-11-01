import pyttsx3


class TtsOffline:
    def __init__(self):
        # initialize Text-to-speech engine
        self._engine = pyttsx3.init()

    def speak(self, text):
        self._engine.say(text)
        self._engine.runAndWait()

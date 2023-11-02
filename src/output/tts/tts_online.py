from io import BytesIO

import gtts
import pygame


class TtsOnline:
    """
    TTS implementation which uses the library `gTTS` which requires an internet connection.
    """

    def __init__(self):
        pygame.init()
        pygame.mixer.init()

    """
    Run gTTS on the text and write the result as an MP3 to a byte buffer.
    """
    def _text_to_mp3(self, text: str) -> BytesIO:
        mp3 = BytesIO()
        tts = gtts.gTTS(text, lang='en')
        tts.write_to_fp(mp3)
        return mp3

    def speak(self, text: str) -> None:
        sound = self._text_to_mp3(text)
        sound.seek(0)
        pygame.mixer.music.load(sound, "mp3")
        pygame.mixer.music.play()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                break

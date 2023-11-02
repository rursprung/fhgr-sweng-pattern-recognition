import gtts
from io import BytesIO
import pygame


class TtsOnline:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()

    def _text_to_mp3(self, text):
        mp3 = BytesIO()
        tts = gtts.gTTS(text, lang='en')
        tts.write_to_fp(mp3)
        return mp3

    def speak(self, text):
        sound = self._text_to_mp3(text)
        sound.seek(0)
        pygame.mixer.music.load(sound, "mp3")
        pygame.mixer.music.play()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                break

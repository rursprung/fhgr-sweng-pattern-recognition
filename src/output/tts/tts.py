from image_proc.image_proc import Pattern
from output.tts.tts_offline import TtsOffline
from output.tts.tts_online import TtsOnline


class TtsPatterns:
    def __init__(self, online=True):
        if online:
            self.tts = TtsOnline()
        else:
            self.tts = TtsOffline()

    def patterns_to_speech(self, pattern_list: list[Pattern]):
        for pattern in pattern_list:
            self.tts.speak(f'the pattern is a {pattern.name} and has the color {pattern.color}')

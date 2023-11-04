from image_proc.image_proc import Pattern
from output.tts.tts_offline import TtsOffline
from output.tts.tts_online import TtsOnline


class TtsPatterns:
    def __init__(self, online=True):
        if online:
            self._tts = TtsOnline()
        else:
            self._tts = TtsOffline()

    def patterns_to_speech(self, pattern_list: list[Pattern]) -> None:
        """
        Goes through the list of patterns and uses text to speech to say which patterns have been found.
        """
        for pattern in pattern_list:
            self._tts.speak(f'the pattern is a {pattern.name} and has the color {pattern.color}')

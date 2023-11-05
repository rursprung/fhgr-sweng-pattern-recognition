import tomllib
from enum import Enum


TtsConfig = Enum('TtsConfig', ['DISABLED', 'ONLINE', 'OFFLINE'])


class Config:
    def __init__(self):
        with open("config/config.toml", "rb") as f:
            self._config_data = tomllib.load(f)

    def tts(self) -> TtsConfig:
        """
        returns the configuration parameter for the TTS function.
        """
        return TtsConfig[self._config_data['tts'].upper()]

    def logfile_path(self) -> str:
        """
        returns the path for the logfile.
        """
        return self._config_data['logfile_path']

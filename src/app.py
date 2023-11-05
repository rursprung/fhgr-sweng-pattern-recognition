from abc import ABC, abstractmethod
from typing import Optional

import cv2

from config import Config
from image_proc.image_proc import ImageProcessor
from output.pattern_logger.console_logger import ConsolePatternLogger
from output.pattern_logger.csv_logger import CsvPatternLogger
from output.tts.tts import TtsPatterns
from output.visualizer.visualizer import Visualizer
from pattern_processor.pattern_filter import PatternFilter


class App(ABC):
    """
    Generic implementation of an app which scans an image for patterns.
    Specific implementations of this class need to implement the `get_next_frame` method
    to provide
    """
    def __init__(self, delay=0):
        self._config = Config()
        self._image_processor = ImageProcessor()
        self._pattern_filter = PatternFilter()
        self._loggers = [
            ConsolePatternLogger(),
            CsvPatternLogger(self._config.logfile_path()),
        ]
        self._visualizer = Visualizer("Press 'q' to quit")
        self._tts_patterns = TtsPatterns(self._config.tts())
        self._delay = delay

    def handle_frame(self, frame: cv2.Mat) -> None:
        pattern_list = self._image_processor.process(frame)

        filtered_patterns = self._pattern_filter.set_and_filter_patterns(pattern_list)

        for logger in self._loggers:
            logger.log(filtered_patterns)

        self._visualizer.visualize(frame, pattern_list)
        self._tts_patterns.patterns_to_speech(filtered_patterns)

    def run(self) -> None:
        try:
            while True:
                frame = self.get_next_frame()

                if frame is None:
                    break

                self.handle_frame(frame)

                if cv2.waitKey(self._delay) & 0xFF == ord("q"):
                    break
                if cv2.getWindowProperty(self._visualizer.name, cv2.WND_PROP_VISIBLE) < 1:
                    break

        except KeyboardInterrupt:
            pass
        finally:
            cv2.destroyAllWindows()

    @abstractmethod
    def get_next_frame(self) -> Optional[cv2.Mat]:
        """
        Return the next frame to be processed or None to stop processing
        """
        pass

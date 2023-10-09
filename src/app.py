from abc import ABC, abstractmethod
from typing import Optional

import cv2

from image_proc.image_proc import ImageProcessor
from output.pattern_logger.console_logger import ConsolePatternLogger
from output.pattern_logger.csv_logger import CsvPatternLogger
from output.tts.tts import TtsPatterns
from output.visualizer.visualizer import Visualizer
from pattern_processor.pattern_filter import PatternFilter


class App(ABC):
    def __init__(self, delay=0):
        self.image_processor = ImageProcessor()
        self.pattern_filter = PatternFilter()
        self.loggers = [
            ConsolePatternLogger(),
            CsvPatternLogger(),
        ]
        self.visualizer = Visualizer("MyVis")
        self.tts_patterns = TtsPatterns()
        self._delay = delay

    def handle_frame(self, frame: cv2.Mat):
        pattern_list = self.image_processor.process(frame)

        filtered_patterns = self.pattern_filter.set_and_filter_patterns(pattern_list)

        for logger in self.loggers:
            logger.log(filtered_patterns)

        self.visualizer.visualize(frame, pattern_list)
        self.tts_patterns.patterns_to_speech(filtered_patterns)

    def run(self):
        try:
            while True:
                frame = self.get_next_frame()

                if frame is None:
                    break

                self.handle_frame(frame)

                if cv2.waitKey(self._delay) & 0xFF == ord("q"):
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

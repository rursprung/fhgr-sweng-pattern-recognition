from abc import ABC, abstractmethod
from typing import Optional

from image_proc.image_proc import ImageProcessor
from pattern_logger.console_logger import ConsolePatternLogger
from pattern_logger.csv_logger import CsvPatternLogger
from pattern_processor.pattern_filter import PatternFilter
from visualizer.visualizer import Visualizer
import cv2


class App(ABC):
    def __init__(self):
        self.image_processor = ImageProcessor()
        self.pattern_filter = PatternFilter()
        self.loggers = [
            ConsolePatternLogger(),
            CsvPatternLogger(),
        ]
        self.visualizer = Visualizer("MyVis")

    def handle_frame(self, frame: cv2.Mat):
        pattern_list = self.image_processor.process(frame)

        filtered_patterns = self.pattern_filter.set_and_filter_patterns(pattern_list)

        for logger in self.loggers:
            logger.log(filtered_patterns)

        self.visualizer.visualize(frame, pattern_list)

    def run(self):
        try:
            while True:
                frame = self.get_next_frame()

                if frame is None:
                    break

                self.handle_frame(frame)

                if cv2.waitKey() & 0xFF == ord("q"):
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

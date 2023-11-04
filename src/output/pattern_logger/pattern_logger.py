from abc import ABC, abstractmethod

from image_proc.image_proc import Pattern


class PatternLogger(ABC):
    @abstractmethod
    def log(self, pattern_list: list[Pattern]) -> None:
        """
        Abstract method to log the patterns.

        Args:
            pattern_list (list): A list of Pattern objects to be visualized.

        Returns:
            None
        """
        pass

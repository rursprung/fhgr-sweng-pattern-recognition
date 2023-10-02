from abc import ABC, abstractmethod


class PatternLogger(ABC):
    @abstractmethod
    def log(self, pattern_list):
        """
        Abstract method to log the patterns.

        Args:
            pattern_list (list): A list of Pattern objects to be visualized.

        Returns:
            None
        """
        pass

from pattern_logger.pattern_logger import PatternLogger


class ConsolePatternLogger(PatternLogger):
    def log(self, pattern_list):
        """
        Logs the patterns to the console.

        Args:
            pattern_list (list): A list of Pattern objects to be visualized.

        Returns:
            None
        """
        for pattern in pattern_list:
            print(f"Pattern name: {pattern.name}, Color: {pattern.color}")

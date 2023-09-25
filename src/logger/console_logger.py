class ConsoleLogger:
    def log(self, pattern_list):
        """
        Logs the patterns to the console
        """
        for pattern in pattern_list:
            print(f"Pattern name: {pattern.name}, Color: {pattern.color}")

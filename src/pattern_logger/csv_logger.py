from pattern_logger.pattern_logger import PatternLogger
import csv


class CsvPatternLogger(PatternLogger):

    def __init__(self):
        self._file = open('logfile.csv', 'w', encoding='UTF8', newline='')

        self._writer = csv.writer(self._file)

        # write the header
        self._writer.writerow(['pattern name', 'pattern color'])

    def __del__(self):
        self._file.close()

    def log(self, pattern_list):
        """
        Logs the patterns to the CSV file.

        Args:
            pattern_list (list): A list of Pattern objects to be visualized.

        Returns:
            None
        """

        for pattern in pattern_list:
            self._writer.writerow([pattern.name, pattern.color])

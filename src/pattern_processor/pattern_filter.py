from image_proc.image_proc import Pattern


class PatternFilter:
    """
    Filter which only returns previously unseen patterns.
    """

    def __init__(self):
        self._previous_patterns = []

    def set_and_filter_patterns(self, patterns: list[Pattern]) -> list[Pattern]:
        """
        :param patterns: the patterns found in the current processing step
        :return: list of patterns which have not been found in the previous step
        """
        filtered_patterns = []
        for pattern in patterns:
            if pattern not in self._previous_patterns:
                filtered_patterns.append(pattern)

        self._previous_patterns = patterns.copy()
        return filtered_patterns

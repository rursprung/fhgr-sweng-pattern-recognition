import cv2
import numpy as np

from image_proc.image_proc import Pattern


class Visualizer:
    def __init__(self, name: str):
        """
        Initialize a Visualizer object.

        Args:
            name (str): The name of the visualization window.

        """
        self._name = name

    @property
    def name(self) -> str:
        return self._name

    def visualize(self, frame: np.ndarray, pattern_list: list[Pattern]) -> None:
        """
        Visualizes patterns on a given frame.

        Args:
            frame (numpy.ndarray): The input image frame.
            pattern_list (list): A list of Pattern objects to be visualized.

        Returns:
            None
        """
        for pattern in pattern_list:
            x, y, w, h = cv2.boundingRect(pattern.contour)
            cv2.drawContours(frame, [pattern.contour], -1, (0, 255, 0), 2)
            cv2.putText(
                frame,
                pattern.color + " " + pattern.name,
                (x, y),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.5,
                (120, 120, 255),
                2,
            )
        cv2.imshow(self._name, frame)

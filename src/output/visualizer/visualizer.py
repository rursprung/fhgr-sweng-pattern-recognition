import cv2


class Visualizer:
    def __init__(self, name):
        """
        Initialize a Visualizer object.

        Args:
            name (str): The name of the visualization window.

        """
        self.name = name

    def visualize(self, frame, pattern_list):
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
        cv2.imshow(self.name, frame)

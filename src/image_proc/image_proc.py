import cv2
import numpy as np
from abc import ABC, abstractmethod


class Pattern:
    def __init__(self, name, contour):
        """
        Initialize a Pattern object.

        Args:
            name (str): The name of the pattern.
            contour (numpy.ndarray): The contour representing the pattern.

        """
        self.name = name
        self.contour = contour
        self.color = None


from abc import ABC, abstractmethod


class Detector(ABC):
    @abstractmethod
    def detect(self, patterns, frame):
        """
        Abstract method to detect patterns in a given image frame.

        Args:
            patterns (list): A list to store detected Pattern objects.
            frame (numpy.ndarray): The input image frame.

        Returns:
            list: A list of detected Pattern objects.

        """
        pass


class ImageProcessor:
    def __init__(self):
        """
        Initialize an ImageProcessor object.

        This class is responsible for processing image frames using a list of detectors.

        """
        self._detectors = [
            PatternDetector(),  # PatternDetector must come first, else no patterns for color detector
            ColorDetector(),
        ]
        self._pattern_color_list = []

    def process(self, frame):
        """
        Process an image frame using a list of detectors.

        Args:
            frame (numpy.ndarray): The input image frame.

        Returns:
            list: A list of patterns and colors detected in the frame.

        """
        for detector in self._detectors:
            self._pattern_color_list = detector.detect(self._pattern_color_list, frame)
        return self._pattern_color_list


class ColorDetector(Detector):
    def __init__(self):
        pass

    def detect(self, patterns, frame):
        """
        Detect the color of patterns in a given image frame.

        Args:
            patterns (list): A list of Pattern objects.
            frame (numpy.ndarray): The input image frame.

        Returns:
            list: A list of Pattern objects with updated color attributes.
        """
        for pattern in patterns:
            mask = np.zeros_like(frame)
            cv2.drawContours(
                mask, [pattern.contour], -1, (255, 255, 255), thickness=cv2.FILLED
            )
            masked_image = cv2.bitwise_and(frame, mask)
            # Convert the masked image to HSV color space
            hsv_image = cv2.cvtColor(masked_image, cv2.COLOR_BGR2HSV)

            # Get the hue channel from the HSV image
            hue_channel = hsv_image[:, :, 0]

            # Calculate the mean hue of non-zero values
            non_zero_hues = hue_channel[hue_channel != 0]
            median_hue = np.median(non_zero_hues)

            pattern.color = self._hue_to_color(median_hue)
        return patterns

    def _hue_to_color(self, hue):
        """
        Convert a hue value to a color name.

        Args:
            hue (float): The hue value to be converted.

        Returns:
            str: The color name corresponding to the hue value.
        """
        color = ""
        if hue < 10:
            color = "RED"
        elif hue < 22:
            color = "ORANGE"
        elif hue < 33:
            color = "YELLOW"
        elif hue < 78:
            color = "GREEN"
        elif hue < 131:
            color = "BLUE"
        elif hue < 150:
            color = "VIOLET"
        else:
            color = "RED"
        return color


class PatternDetector(Detector):
    def __init__(self):
        pass

    def detect(self, patterns, frame):
        """
        Detect patterns (shapes) in a given image frame.

        Args:
            patterns (list): A list to store detected Pattern objects.
            frame (numpy.ndarray): The input image frame.

        Returns:
            list: A list of Pattern objects representing the detected patterns.
        """
        img = frame.copy()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # Perform dilation
        blurred = cv2.GaussianBlur(gray, (5, 5), 0)
        edges = cv2.Canny(blurred, 40, 180)
        # Perform dilation
        kernel = np.ones((5, 5), np.uint8)
        dilated_image = cv2.dilate(edges, kernel, iterations=2)
        # detect contours
        contours, _ = cv2.findContours(
            dilated_image.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
        )

        approx = None
        patterns.clear()
        for contour in contours:
            epsilon = 0.04 * cv2.arcLength(contour, True)
            approx = cv2.approxPolyDP(contour, epsilon, True)

            num_sides = len(approx)
            x, y, w, h = cv2.boundingRect(approx)

            if num_sides == 3:
                pattern = "Triangle"
            elif num_sides == 4:
                aspect_ratio = w / float(h)
                if 0.95 <= aspect_ratio <= 1.05:
                    pattern = "Square"
                else:
                    pattern = "Rectangle"
            else:
                pattern = "Circle"

            if num_sides >= 3:
                patterns.append(Pattern(pattern, approx))
        return patterns

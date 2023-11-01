from typing import Optional

import cv2

from app import App


class WebcamApp(App):
    """
    Reads images from the webcam, runs the pattern recognition on them and displays the images with the result.
    """

    def __init__(self):
        self._vid = cv2.VideoCapture(0)
        super().__init__(delay=1)

    def get_next_frame(self) -> Optional[cv2.Mat]:
        has_frame, frame = self._vid.read()
        if not has_frame:
            return None

        return frame


def main():
    app = WebcamApp()
    app.run()


if __name__ == "__main__":
    main()

from typing import Optional

import cv2

from app import App


class StoredImageApp(App):
    """
    Reads images from the disk, runs the pattern recognition on them and displays the images with the result.
    """

    def __init__(self):
        self._current_image = 0
        self._num_images = 5  # quick-win

        super().__init__()

    def get_next_frame(self) -> Optional[cv2.Mat]:
        if self._current_image >= self._num_images:
            return None

        i = self._current_image
        self._current_image += 1

        print(f"processing image {i}")
        return cv2.imread(f"assets/test_image{i:02}.jpg", cv2.IMREAD_COLOR)


def main():
    app = StoredImageApp()
    app.run()


if __name__ == "__main__":
    main()

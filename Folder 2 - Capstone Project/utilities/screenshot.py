import os


class ScreenshotUtility:

    @staticmethod
    def capture(driver, test_name):
        screenshot_dir = os.path.join(
            os.path.dirname(os.path.dirname(__file__)),
            "screenshots"
        )

        os.makedirs(screenshot_dir, exist_ok=True)

        file_path = os.path.join(
            screenshot_dir,
            f"{test_name}.png"
        )

        driver.save_screenshot(file_path)

        return file_path
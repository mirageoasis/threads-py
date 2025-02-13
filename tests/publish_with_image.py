import unittest
from threadspy import ThreadsAPI


class TestPublishWithImage(unittest.TestCase):
    def setUp(self):
        self.threads_api = ThreadsAPI(verbose=True, username="username", password="password")

    def test_publish_with_local_image(self):
        check_sum = self.threads_api.publish_with_image(
            "Hello World!", image_path=".github/logo.jpg"
        )
        self.assertEqual(check_sum, True)

    def test_publish_with_image_url(self):
        check_sum = self.threads_api.publish_with_image(
            "Hello World!",
            image_path="https://github.com/junhoyeo/threads-py/blob/main/.github/logo.jpg?raw=true",
        )
        self.assertEqual(check_sum, True)


if __name__ == "__main__":
    unittest.main()

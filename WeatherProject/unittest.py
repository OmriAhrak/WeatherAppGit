import unittest
import requests

class TestApp(unittest.TestCase):

    def RuningOrNot(self):
        url = requests.head("http://10.1.0.152/")
        self.assertEqual(url.status_code, 200)


if __name__ == '__main__':
    unittest.main()

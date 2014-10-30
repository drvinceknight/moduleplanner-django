"""
Functional tests using selenium.
"""
from selenium import webdriver
import unittest

class IndexPage(unittest.TestCase):

    def setUp(self):
        self.firefox = webdriver.Firefox()
        self.chrome = webdriver.Chrome()

    def tearDown(self):
        self.firefox.quit()
        self.chrome.quit()

    def test_title_in_firefox(self):
        """
        Test the title in firefox
        """
        self.firefox.get('http://localhost:8000')
        self.assertIn('Module Planner', self.firefox.title)

    def test_title_in_chrome(self):
        """
        Test the title in Chrome
        """
        self.chrome.get('http://localhost:8000')
        self.assertIn('Module Planner', self.chrome.title)

if __name__ == '__main__':
    unittest.main()

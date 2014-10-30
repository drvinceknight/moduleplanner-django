"""
Functional tests using selenium.
"""
from selenium import webdriver

# Firefox tests for the index page

browser = webdriver.Firefox()
browser.get('http://localhost:8000')

assert 'Module Planner' in browser.title
browser.quit()

# Chrome tests for the index page
# To use this you need to have ChromeDriver (https://code.google.com/p/selenium/wiki/ChromeDriver)

browser = webdriver.Chrome()
browser.get('http://localhost:8000')

assert 'Module Planner' in browser.title
browser.quit()

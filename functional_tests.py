"""
Functional tests using selenium
"""
from selenium import webdriver

browser = webdriver.Firefox()
browser.get('http://localhost:8000')

assert 'Module Planner' in browser.title

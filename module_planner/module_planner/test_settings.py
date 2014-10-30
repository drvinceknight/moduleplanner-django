"""
Custom setting to run tests
"""
from module_planner.settings import *

# Test runner with no database creation
TEST_RUNNER = 'mysite.scripts.testrunner.NoDbTestRunner'

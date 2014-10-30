"""
Custom setting to run tests
"""
from module_planner.settings import *

# Test runner with no database creation
TEST_RUNNER = 'module_planner.testrunner.NoDbTestRunner'

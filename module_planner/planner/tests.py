from module_planner.testrunner import NoDbTestRunner

class SmokeTest(NoDbTestRunner):
    def test_bad_maths(self):
        self.assertEqual(1+1,3)

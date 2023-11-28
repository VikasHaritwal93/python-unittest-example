import unittest
import sys

class TestExample(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(1 + 1, 2, "1 + 1 should equal 2")

if __name__ == '__main__':
    # Create a TestSuite and add the test case
    suite = unittest.TestSuite()
    suite.addTest(TestExample('test_addition'))

    # Create a TestResult object to capture the test results
    result = unittest.TestResult()

    # Run the tests
    suite.run(result)

    # Output the results to a file
    with open('test_report.xml', 'w') as f:
        runner = unittest.TextTestRunner(stream=f, verbosity=2)
        runner.run(suite)

    # Print the results to the console
    print("\n=== Test Results ===")
    print(f"Errors: {len(result.errors)}")
    print(f"Failures: {len(result.failures)}")
    print(f"Tests Run: {result.testsRun}")
    print("Test Report written to 'test_report.xml'")
    
    # Exit with the appropriate status code
    sys.exit(len(result.errors) + len(result.failures))

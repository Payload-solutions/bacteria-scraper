from unittest import (
    TestLoader,
    TestSuite
)

from pyunitreport import HTMLTestRunner
from assertions import HomePageTests

assertions_tests = TestLoader().loadTestsFromTestCase(HomePageTests)
smoke_test = TestSuite([assertions_tests])

kwargs = {
    "output": 'smoke-report'
}
runner = HTMLTestRunner(**kwargs)
runner.run(smoke_test)

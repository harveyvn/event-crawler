import unittest

import test_models
import test_spiders

from test_crawler import TestCrawler
from test_connection import TestConnection
from test_reader import TestReader
from test_writer import TestWriter

if __name__ == "__main__":
    runner = unittest.TextTestRunner(verbosity=2)
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    suite = test_models.load_tests(suite, loader)
    suite = test_spiders.load_tests(suite, loader)
    suite.addTests(loader.loadTestsFromTestCase(TestCrawler))
    suite.addTests(loader.loadTestsFromTestCase(TestConnection))
    suite.addTests(loader.loadTestsFromTestCase(TestReader))
    suite.addTests(loader.loadTestsFromTestCase(TestWriter))
    runner.run(suite)

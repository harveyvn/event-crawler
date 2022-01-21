import unittest

import test_models
import test_spiders
import test_controllers

from test_connection import TestConnection

if __name__ == "__main__":
    runner = unittest.TextTestRunner(verbosity=2)
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    suite = test_models.load_tests(suite, loader)
    suite = test_spiders.load_tests(suite, loader)
    suite = test_controllers.load_tests(suite, loader)
    suite.addTests(loader.loadTestsFromTestCase(TestConnection))
    runner.run(suite)

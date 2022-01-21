import unittest
import test_models

if __name__ == "__main__":
    print("Running unittest...")
    runner = unittest.TextTestRunner(verbosity=2)
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    suite = test_models.load_tests(suite, loader)
    runner.run(suite)

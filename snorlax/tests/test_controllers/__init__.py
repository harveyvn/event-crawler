from .test_writer import TestWriter
from .test_reader import TestReader
from .test_crawler import TestCrawler


def load_tests(suite, loader):
    suite.addTests(loader.loadTestsFromTestCase(TestCrawler))
    suite.addTests(loader.loadTestsFromTestCase(TestWriter))
    suite.addTests(loader.loadTestsFromTestCase(TestReader))
    return suite
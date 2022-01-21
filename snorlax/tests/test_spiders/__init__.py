from .test_event_spider import TestEventSpider
from .test_program_spider import TestProgramSpider


def load_tests(suite, loader):
    suite.addTests(loader.loadTestsFromTestCase(TestEventSpider))
    suite.addTests(loader.loadTestsFromTestCase(TestProgramSpider))
    return suite

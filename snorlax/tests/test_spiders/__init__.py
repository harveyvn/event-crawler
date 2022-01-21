from .test_event_spider import TestEventSpider


def load_tests(suite, loader):
    suite.addTests(loader.loadTestsFromTestCase(TestEventSpider))
    return suite

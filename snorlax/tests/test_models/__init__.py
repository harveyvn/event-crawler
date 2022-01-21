from .test_artitst import TestArtist


def load_tests(suite, loader):
    suite.addTests(loader.loadTestsFromTestCase(TestArtist))
    return suite

from .test_artitst import TestArtist
from .test_event import TestEvent
from .test_cover import TestCover
from .test_location import TestLocation
from .test_song import TestSong


def load_tests(suite, loader):
    suite.addTests(loader.loadTestsFromTestCase(TestArtist))
    suite.addTests(loader.loadTestsFromTestCase(TestEvent))
    suite.addTests(loader.loadTestsFromTestCase(TestCover))
    suite.addTests(loader.loadTestsFromTestCase(TestLocation))
    suite.addTests(loader.loadTestsFromTestCase(TestSong))
    return suite

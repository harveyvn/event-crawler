from .test_artitst import TestArtist
from .test_event import TestEvent
from .test_cover import TestCover
from .test_location import TestLocation
from .test_song import TestSong
from .test_event_artist import TestEventArtist
from .test_event_cover import TestEventCover
from .test_event_location import TestEventLocation
from .test_event_song import TestEventSong


def load_tests(suite, loader):
    suite.addTests(loader.loadTestsFromTestCase(TestArtist))
    suite.addTests(loader.loadTestsFromTestCase(TestEvent))
    suite.addTests(loader.loadTestsFromTestCase(TestCover))
    suite.addTests(loader.loadTestsFromTestCase(TestLocation))
    suite.addTests(loader.loadTestsFromTestCase(TestSong))
    suite.addTests(loader.loadTestsFromTestCase(TestEventArtist))
    suite.addTests(loader.loadTestsFromTestCase(TestEventCover))
    suite.addTests(loader.loadTestsFromTestCase(TestEventLocation))
    suite.addTests(loader.loadTestsFromTestCase(TestEventSong))
    return suite

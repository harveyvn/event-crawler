import unittest
from snorlax.modules.models import Cover
from snorlax.modules.constant import CONST


class TestCover(unittest.TestCase):
    def test_create_cover(self):
        a = Cover("Pokemon")
        b = Cover("")

        self.assertEqual(a.url, "Pokemon")
        self.assertEqual(a.status, CONST.PASSED)
        self.assertEqual(b.url, "")
        self.assertEqual(b.status, CONST.FAILED)

    def test_check_found_match_query(self):
        a = Cover("google.com")
        self.assertEqual(a.found(), ('SELECT * FROM covers where url = %s', ('google.com',)))

    def test_check_save_match_query(self):
        a = Cover("google.com")
        self.assertEqual(a.save(), ('INSERT INTO covers(url) VALUES(%s) RETURNING id;', ('google.com',)))


if __name__ == '__main__':
    unittest.main()

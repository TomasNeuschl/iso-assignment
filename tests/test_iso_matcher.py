from app.iso_matcher.iso_matcher import ISOMatcher
from tests.base_test import BaseTest


class TestISOMatcher(BaseTest):
    def test_valid_iso_code(self):
        result = ["Slowakei", "Slovaška", "Szlovákia"]
        matcher = ISOMatcher()
        success, matches = matcher.match_country('svk', result)

        self.assertEqual(success, True)
        self.assertEqual(matches, result)

    def test_invalid_iso_code(self):
        matcher = ISOMatcher()
        success, matches = matcher.match_country('abcd', ['Slovaška', 'Slovakien', 'Szlovákia'])
        self.assertEqual(success, False)
        self.assertEqual(matches, [])

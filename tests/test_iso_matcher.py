from app.iso_matcher.iso_matcher import ISOMatcher
from tests.base_test import BaseTest


class TestISOMatcher(BaseTest):
    def test_valid_iso_code(self):
        result = ["Slowakei", "Slovaška", "Szlovákia"]
        matcher = ISOMatcher('svk', result)
        matcher.match_country()

        self.assertEqual(matcher.success, True)
        self.assertEqual(matcher.matches, result)

    def test_invalid_iso_code(self):
        matcher = ISOMatcher('abcd', ['Slovaška', 'Slovakien', 'Szlovákia'])
        matcher.match_country()
        self.assertEqual(matcher.success, False)
        self.assertEqual(matcher.matches, [])

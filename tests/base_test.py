from unittest import TestCase
from unittest.mock import patch


class BaseTest(TestCase):
    def setUp(self):
        super().setUp()

        salutation_patch = patch(
            'app.iso_matcher.iso_matcher.ISOMatcher._load_countries').start()
        salutation_patch.return_value = [
            {"id": 703, "alpha2": "sk", "alpha3": "svk", "ar": "سلوفاكيا", "bg": "Словакия", "cs": "Slovensko",
             "da": "Slovakiet", "de": "Slowakei", "el": "Σλοβακία", "en": "Slovakia", "eo": "Slovakio",
             "es": "Eslovaquia", "et": "Slovakkia", "eu": "Eslovakia", "fi": "Slovakia", "fr": "Slovaquie",
             "hr": "Slovačka", "hu": "Szlovákia", "hy": "Սլովակիա", "it": "Slovacchia", "ja": "スロバキア",
             "ko": "슬로바키아", "lt": "Slovakija", "nl": "Slowakije", "no": "Slovakia", "pl": "Słowacja",
             "pt": "Eslováquia", "ro": "Slovacia", "ru": "Словакия", "sk": "Slovensko", "sl": "Slovaška",
             "sr": "Slovačka", "sv": "Slovakien", "th": "สโลวาเกีย", "uk": "Словаччина", "zh": "斯洛伐克",
             "zh-tw": "斯洛伐克"},
            {"id": 705, "alpha2": "si", "alpha3": "svn", "ar": "سلوفينيا", "bg": "Словения", "cs": "Slovinsko",
             "da": "Slovenien", "de": "Slowenien", "el": "Σλοβενία", "en": "Slovenia", "eo": "Slovenio",
             "es": "Eslovenia", "et": "Sloveenia", "eu": "Eslovenia", "fi": "Slovenia", "fr": "Slovénie",
             "hr": "Slovenija", "hu": "Szlovénia", "hy": "Սլովենիա", "it": "Slovenia", "ja": "スロベニア",
             "ko": "슬로베니아", "lt": "Slovėnija", "nl": "Slovenië", "no": "Slovenia", "pl": "Słowenia", "pt": "Eslovênia",
             "ro": "Slovenia", "ru": "Словения", "sk": "Slovinsko", "sl": "Slovenija", "sr": "Slovenija",
             "sv": "Slovenien", "th": "สโลวีเนีย", "uk": "Словенія", "zh": "斯洛文尼亚", "zh-tw": "斯洛維尼亞"},
        ]
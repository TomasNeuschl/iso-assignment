import json


class ISOMatcher:
    countries_table = None

    def __init__(self):
        self.countries_table = self._load_countries()

    @staticmethod
    def _load_countries():
        file_path = './data/data.json'

        # Open and read the JSON file
        with open(file_path, 'r') as json_file:
            data = json.load(json_file)
        return data

    def match_country(self, iso_code, countries):
        matches = []
        for country in self.countries_table:
            if country['alpha3'] == iso_code:
                for translation in countries:
                    if translation in country.values():
                        matches.append(translation)
                return True, matches
        return False, matches

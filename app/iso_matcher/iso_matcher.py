import json


class ISOMatcher:
    countries_table = None

    def __init__(self, iso_code, countries):
        self.countries_table = self._load_countries()
        self.iso_code = iso_code
        self.countries = countries
        self.success = None
        self.matches = []

    @staticmethod
    def _load_countries():
        file_path = './data/data.json'

        # Open and read the JSON file
        with open(file_path, 'r') as json_file:
            data = json.load(json_file)
        return data

    def match_country(self):
        self.success = False
        for country in self.countries_table:
            if country['alpha3'] == self.iso_code:
                for translation in self.countries:
                    if translation in country.values():
                        self.matches.append(translation)
                self.success = True
                return self

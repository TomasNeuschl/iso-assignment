from fastapi.testclient import TestClient

from app.main import app
from tests.base_test import BaseTest


class TestMain(BaseTest):
    client = TestClient(app)

    def test_valid_data(self):
        data = {
            "iso": "svk",
            "countries": [
                "iran",
                "Slowakei",
                "Vatikan",
                "Slovaška",
                "Szlovákia",
                "Belgrade",
                "España",
                "Nizozemsko"
            ]
        }

        response = self.client.post("/match_country", json=data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {
            "iso": "svk",
            "match_count": 3,
            "matches": ["Slowakei", "Slovaška", "Szlovákia"]
        })

    def test_invalid_iso(self):
        data = {
            "iso": "svkx",
            "countries": [
                "iran",
            ]
        }

        response = self.client.post("/match_country", json=data)

        self.assertEqual(response.status_code, 422)

    def test_invalid_keys(self):
        data = {
            "123": "svk",
            "countries": [
                "iran",
            ]
        }

        response = self.client.post("/match_country", json=data)

        self.assertEqual(response.status_code, 422)

    def test_empty_data(self):
        data = {}

        response = self.client.post("/match_country", json=data)

        self.assertEqual(response.status_code, 422)

    def test_non_existing_iso(self):
        data = {
            "iso": "abc",
            "countries": [
            ]
        }

        response = self.client.post("/match_country", json=data)

        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.text, '{"detail":"ISO code does not exist"}')

    def test_iso_not_found_in_countries(self):
        data = {
            "iso": "svk",
            "countries": [
                "iran",
            ]
        }

        response = self.client.post("/match_country", json=data)

        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.text, '{"detail":"ISO code not found in the list of countries"}')

import unittest
from unittest import mock
from main import get_stat_value, convert_json_to_pokemon, get_random_pokemon


def mocked_requests_get(*args, **kwargs):
    class MockResponse:
        def __init__(self, json_data, status_code):
            self.json_data = json_data
            self.status_code = status_code

        def json(self):
            return self.json_data

    if args[0] == "https://pokeapi.co/api/v2/stat/":
        return MockResponse(
            {
                "results": [
                    {"name": "hp"},
                    {"name": "attack"},
                    {"name": "defense"},
                    {"name": "special-attack"},
                    {"name": "special-defense"},
                    {"name": "speed"},
                    {"name": "accuracy"},
                    {"name": "evasion"},
                ],
            },
            200,
        )
    elif args[0] == "https://pokeapi.co/api/v2/pokemon/1":
        return MockResponse(
            {
                "name": "bulbasaur",
                "stats": [
                    {"base_stat": 45, "stat": {"name": "hp"}},
                    {"base_stat": 49, "stat": {"name": "attack"}},
                    {"base_stat": 49, "stat": {"name": "defense"}},
                    {"base_stat": 65, "stat": {"name": "special-attack"}},
                    {"base_stat": 65, "stat": {"name": "special-defense"}},
                    {"base_stat": 45, "stat": {"name": "speed"}},
                ],
            },
            200,
        )


def choise_one(*args, **kwargs):
    return 1


class TestIntegration(unittest.TestCase):
    @mock.patch("requests.get", side_effect=mocked_requests_get)
    def test_getting_all_stat_names(self, mock_request):
        stat_names = get_stat_value()
        self.assertEqual(
            stat_names,
            [
                "hp",
                "attack",
                "defense",
                "special-attack",
                "special-defense",
                "speed",
                "accuracy",
                "evasion",
            ],
        )

    @mock.patch("requests.get", side_effect=mocked_requests_get)
    @mock.patch("random.randint", side_effect=choise_one)
    def test_convert_json_to_pokemon(self, mocked_request_get, mocked_choise_one):
        pokemon = convert_json_to_pokemon(get_random_pokemon())
        self.assertEqual(pokemon.name, "bulbasaur")


if __name__ == "__main__":
    unittest.TestCase

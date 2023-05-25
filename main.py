from typing import Dict, List
import random
import requests
from pokemon import Pokemon, Statistics


POKEMON_ENDPOINT = "https://pokeapi.co/api/v2/pokemon/"


def get_random_pokemon() -> Dict[str, str]:
    pokemon_id = random.randint(1, 1010)
    pokemon = requests.get(f"{POKEMON_ENDPOINT}{pokemon_id}")
    return pokemon.json()


def convert_json_to_pokemon(api_responce: Dict[str, str]) -> Pokemon:
    name = api_responce["name"]
    responce_stats = api_responce["stats"]
    stats = []
    for responce_stat in responce_stats:
        stats.append(
            Statistics(responce_stat["base_stat"], responce_stat["stat"]["name"])
        )
    pokemon = Pokemon(name, stats)
    return pokemon


POKEMON_ENDPOINT_TWO = "https://pokeapi.co/api/v2/stat/"


def get_stat_value() -> List[str]:
    pokemon_stat = []
    responce_stat = requests.get(f"{POKEMON_ENDPOINT_TWO}")
    converted_file = responce_stat.json()
    for stat_name in converted_file["results"]:
        pokemon_stat.append(stat_name["name"])
    return pokemon_stat


def chose_winner(pokemon1: Pokemon, pokemon2: Pokemon) -> Pokemon:
    all_possible_stats = get_stat_value()
    p1_score = 0
    p2_score = 0
    for statistic in all_possible_stats:
        p1_stat_points = pokemon1.get_statistic_base_stat(statistic)
        p2_stat_points = pokemon2.get_statistic_base_stat(statistic)
        if p1_stat_points > p2_stat_points:
            p1_score += 1
        elif p2_stat_points > p1_stat_points:
            p2_score += 1

    if p1_score > p2_score:
        return pokemon1
    elif p2_score > p1_score:
        pokemon2
    else:
        return None


if __name__ == "__main__":
    poke1 = convert_json_to_pokemon(get_random_pokemon())
    poke2 = convert_json_to_pokemon(get_random_pokemon())

    winner = chose_winner(poke1, poke2)

    print(f"First pokemon {poke1.name}")
    print(f"Secound pokemon {poke2.name}")
    if winner:
        print(f" And the winner is {winner.name}")
    else:
        print(" Ivyko drama!")

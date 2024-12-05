import requests


BREEDS_URL = "https://api.thecatapi.com/v1/breeds"


def is_breed_valid(breed_name: str) -> bool:
    response = requests.get(BREEDS_URL)
    all_breeds = [breed["name"] for breed in response.json()]
    return breed_name in all_breeds

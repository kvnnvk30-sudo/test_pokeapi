import requests

class PokeClient:
    def __init__(self):
        self.base_url = "https://pokeapi.co/api/v2"



    def get_pokemon(self, name: str):
        url=f"{self.base_url}/pokemon/{name}"
        return requests.get(url)

    def get_pokemon_list(self, limit: int):
        url=f"{self.base_url}/pokemon?limit={limit}"
        return requests.get(url)

    def get_berry(self, name: str):
        url=f"{self.base_url}/berry/{name}"
        return requests.get(url)
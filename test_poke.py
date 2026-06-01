from pokeapi import PokeClient
import pytest


@pytest.fixture
def poke_client():
    return PokeClient()


@pytest.fixture
def pikachu_response(poke_client):
    return poke_client.get_pokemon("pikachu")


@pytest.fixture
def poke_data(pikachu_response):
    return pikachu_response.json()


def test_get_pokemon(pikachu_response, poke_data):
    assert pikachu_response.status_code == 200
    assert poke_data["name"]=="pikachu"
    assert "abilities" in poke_data
    assert "height" in poke_data
    assert "weight" in poke_data


def test_abilities_is_list(pikachu_response,poke_data ):
    assert isinstance(poke_data['abilities'],list)
    assert len(poke_data['abilities'])>0
    for item in poke_data['abilities']:
        assert 'ability' in item


def test_get_pokemon_list(poke_client):
    response = poke_client.get_pokemon_list(10)
    assert response.status_code == 200
    data = response.json()
    assert 'results' in data
    assert len(data['results'])==10
    for pokemon in data['results']:
        assert 'name' in pokemon
        assert 'url' in pokemon


def test_get_berry(poke_client):
    response = poke_client.get_berry("cheri")
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "cheri"
    assert 'growth_time' in data
    assert isinstance(data['growth_time'], int)


def test_not_found(poke_client):
    response = poke_client.get_pokemon("fakemonster123")
    assert response.status_code == 404
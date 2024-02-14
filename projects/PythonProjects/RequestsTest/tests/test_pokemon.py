import requests
import pytest

token = '0914aeb73237ab03ffd912259909f366'
host = 'https://api.pokemonbattle.me:9104'

def test_status_code(): 
    response = requests.get(f'{host}/trainers', params = {
        'trainer_id' : 151
    })
    assert response.status_code == 200
    assert response.json()['trainer_name'] == 'Vovan4eg'


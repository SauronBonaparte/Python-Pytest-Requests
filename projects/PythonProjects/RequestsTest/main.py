import requests

token = '0914aeb73237ab03ffd912259909f366' #мой токен из котика
host = 'https://api.pokemonbattle.me:9104' #хост для покемонов

response_add_pokemon = requests.post(f'{host}/pokemons', json = { # создание покемона 
    "name": "Мурлыкер",
    "photo": "https://dolnikov.ru/pokemons/albums/004.png"
}, headers = {'Content-Type' : 'application/json',
              'trainer_token' : token})

print (response_add_pokemon.text)

response_rename_pokemon = requests.patch(f'{host}/pokemons', json = { # изменить имя покемона
    "pokemon_id": "540",
    "name": "Мумурка",
    "photo": "https://dolnikov.ru/pokemons/albums/005.png"
}, headers = {'Content-Type' : 'application/json',
              'trainer_token' : token})

print (response_rename_pokemon.text)

response_add_pokeball = requests.post(f'{host}/trainers/add_pokeball', json = { # добавить покемона в покебол
    "pokemon_id": "540"
}, headers = {'Content-Type' : 'application/json',
              'trainer_token' : token})

print (response_add_pokeball.text)
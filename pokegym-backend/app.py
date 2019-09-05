import requests
from flask import Flask
from flask_restful import Resource, Api
from flask_cors import CORS
from persistqueue import Queue
import threading
import time
import sys

app = Flask(__name__)
api = Api(app)
CORS(app)
pokemon_queue = Queue("./pokemon_queue")


def byName(pokemon):
    return pokemon['name']
print(pokemon_queue.qsize())

def thread_function():
    print("Pokemon queue fill in progress")
    fill_queue_file()

def fill_queue_file():
    pokemon_request = requests.get("https://pokeapi.co/api/v2/pokemon/?limit=1000")
    pokemon_list = sorted(pokemon_request.json()['results'], key=byName)
    for pokemon in pokemon_list:
        pokemon_queue.put(pokemon)
    pokemon_queue.task_done()
    print('Pokemon queue insertion of 964 pokemons, queue size:', pokemon_queue.qsize())

if pokemon_queue.qsize() < 100:
    fill_queue_file()

class GetPokemonEntries(Resource):
    def get(self):
        pokemon_list = []
        if pokemon_queue.qsize() < 100:
            pokemon_fill_thread = threading.Thread(target=thread_function)
            pokemon_fill_thread.start()
        for i in range(0, 18):
            pokemon = pokemon_queue.get()
            pokemon_name = pokemon['name']
            pokemon_id = pokemon['url'][slice(34,100)][slice(-1)]
            pokemon_list.append({ 'id': pokemon_id, 'name': pokemon_name, 'qsize': pokemon_queue.qsize() })
        pokemon_queue.task_done()
        print('sending', len(pokemon_list), 'pokemons to gym')
        print(pokemon_queue.qsize(), 'on queue')
        return pokemon_list

api.add_resource(GetPokemonEntries, '/pokegym/entries')

if __name__ == '__main__':
    app.run(debug=True)
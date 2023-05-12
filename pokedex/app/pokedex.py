from flask import Flask, jsonify, render_template
from redis import Redis
import requests

app = Flask(__name__)
redis = Redis(host='redis', port=6379)


@app.route('/pokemon/<name>')
def get_pokemon(name):
    redis.incr('hits')
    counter = str(redis.get('hits').decode('utf-8'))

    url = f"https://pokeapi.co/api/v2/pokemon/{name}"
    response = requests.get(url)
    pokemon = response.json()

    return render_template('pokemon.html', pokemon=pokemon, counter=counter)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)

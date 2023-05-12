from ..app import pokedex
from bs4 import BeautifulSoup
import unittest


class appTest(unittest.TestCase):
    def setUp(self):
        self.app = pokedex.app.test_client()

    def test_response_ok(self):
        response = self.app.get('/pokemon/pikachu')
        self.assertEqual(response.status_code, 200)

    def test_pikachu_right_information(self):
        response = self.app.get('/pokemon/pikachu')

        soup = BeautifulSoup(response.text, 'html.parser')
        self.assertEqual(soup.find(id='name').text, 'pikachu')
        self.assertEqual(soup.find(id="types").find('li').text, 'electric')

    def test_counter(self):
        response = self.app.get('/pokemon/pikachu')

        soup = BeautifulSoup(response.text, 'html.parser')
        # The counter is the penultimate word of the text
        self.assertGreater(int(soup.find(id='counter').text.split(' ')[-2]), 0)

    def test_pokemon_not_found(self):
        response = self.app.get('/pokemon/donotexist')
        self.assertEqual(response.status_code, 404)

    def close(self):
        self.app.close()

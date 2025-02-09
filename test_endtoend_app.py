# test_endtoend_app.py
import unittest
import requests
from bs4 import BeautifulSoup

class TestAppE2E(unittest.TestCase):
    def setUp(self):
        self.base_url = 'http://my-app:5000'

    def test_add_and_delete_item(self):
        # Send a POST request to add a new item
        response = requests.post(self.base_url + '/add', data={'item': 'New E2E Item'})

        self.assertEqual(response.status_code, 200)

        # Parse the response HTML using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find the new item in the HTML
        item = soup.find(lambda tag: tag.name == 'li' and 'New E2E Item' in tag.text)

        self.assertIsNotNone(item)

        # Extract the item index from the delete link URL
        index = item.find_next('a', text='Delete')['href'].split('/')[-1]

        # Send a GET request to delete the item
        response = requests.get(self.base_url + '/delete/' + index)

        self.assertEqual(response.status_code, 200)

        # Parse the response HTML using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Assert that the item is no longer in the HTML
        item = soup.find(lambda tag: tag.name == 'li' and 'New E2E Item' in tag.text)
        self.assertIsNone(item)

if __name__ == '__main__':
    unittest.main()
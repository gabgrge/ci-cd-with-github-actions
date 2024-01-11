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
        print(f"Add item response status code: {response.status_code}")
        print(f"Add item response text: {response.text}")

        self.assertEqual(response.status_code, 200)

        # Parse the response HTML using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')
        print(f"HTML response after adding item: {soup.prettify()}")

        # Find the new item in the HTML
        item = soup.find('li', string=lambda text: text and 'New E2E Item' in text)

        self.assertIsNotNone(item)

        # Extract the item index from the delete link URL
        index = item.find_next('a', text='Delete')['href'].split('/')[-1]

        # Send a GET request to delete the item
        response = requests.get(self.base_url + '/delete/' + index)
        print(f"Delete item response status code: {response.status_code}")
        print(f"Delete item response text: {response.text}")

        self.assertEqual(response.status_code, 200)

        # Parse the response HTML using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')
        print(f"HTML response after deleting item: {soup.prettify()}")

        # Assert that the item is no longer in the HTML
        item = soup.find('li', string=lambda text: text and 'New E2E Item' in text)
        self.assertIsNone(item)

if __name__ == '__main__':
    unittest.main()
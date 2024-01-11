# test_endtoend_app.py
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class TestAppE2E(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://my-app:5000')

    def test_add_and_delete_item(self):
        input_field = self.driver.find_element(By.NAME, 'item')
        input_field.send_keys('New E2E Item')
        input_field.send_keys(Keys.RETURN)
        self.assertIn('New E2E Item', self.driver.page_source)

        delete_link = self.driver.find_element(By.LINK_TEXT, 'Delete')
        delete_link.click()
        self.assertNotIn('New E2E Item', self.driver.page_source)

    def tearDown(self):
        self.driver.close()
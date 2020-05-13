from Locators.locators import Locators
from random import randint

class ProductsPage():

    def __init__(self, driver):

        self.driver = driver

        self.all_items_css_selector = Locators.all_items_css_selector

    def click_on_a_random_product(self):
        all_items = self.driver.find_elements_by_css_selector(self.all_items_css_selector)
        item = all_items[randint(0, len(all_items) - 1)]
        print(item.text)
        item.click()
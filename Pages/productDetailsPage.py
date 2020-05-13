from Locators.locators import Locators

class ProductDetailsPage():

    def __init__(self, driver):

        self.driver = driver

        self.add_to_cart_button_id = Locators.add_to_cart_button_id

    def click_add_to_cart(self):
        self.driver.find_element_by_id(self.add_to_cart_button_id).click()
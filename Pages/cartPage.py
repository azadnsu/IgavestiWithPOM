from Locators.locators import Locators

class CartPage():

    def __init__(self, driver):

        self.driver = driver

        self.remove_cart_class_name = Locators.remove_cart_class_name
        self.checkout_button_name   = Locators.checkout_button_name

    def click_remove_cart(self):
        self.driver.find_element_by_class_name(self.remove_cart_class_name).click()

    def click_checkout_button(self):
        self.driver.find_element_by_name(self.checkout_button_name).click()
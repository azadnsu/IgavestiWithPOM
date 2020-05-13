from Locators.locators import Locators

class OrderConfirmationPage():

    def __init__(self, driver):
        self.driver = driver
        self.order_number_class_name = Locators.order_number_class_name
        self.continue_shopping_link_text = Locators.continue_shopping_link_text

    def print_order_number(self):
        print(self.driver.find_element_by_class_name('os-order-number'))

    def click_continue_shopping(self):
        self.driver.find_element_by_link_text("Continue shopping").click()

from Locators.locators import Locators

class ShippingPage():

    def __init__(self, driver):
        self.driver = driver
        self.continue_to_payment_xpath = Locators.continue_to_payment_xpath

    def click_continue_to_payment_button(self):
        self.driver.find_element_by_xpath(self.continue_to_payment_xpath).click()


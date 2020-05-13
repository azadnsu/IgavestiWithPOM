from Locators.locators import Locators

class PaymentPage():

    def __init__(self,driver):
        self.driver = driver

        self.cash_on_delivery_radio_button_xpath = Locators.cash_on_delivery_radio_button_xpath
        self.complete_order_button_id = Locators.complete_order_button_id

    def select_cash_on_delivery(self):
        self.driver.find_element_by_xpath(self.cash_on_delivery_radio_button_xpath).click()

    def click_complete_order_button(self):
        self.driver.find_element_by_id(self.complete_order_button_id).click()


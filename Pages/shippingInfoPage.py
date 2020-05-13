from Locators.locators import Locators
from selenium.webdriver.common.keys import Keys
import random

class ShippingInfoPage():

    def __init__(self, driver):
        self.driver = driver

        self.checkout_email_or_phone_xpath           = Locators.checkout_email_or_phone_xpath
        self.checkout_shipping_address_last_name_id  = Locators.checkout_shipping_address_last_name_id
        self.checkout_shipping_address_address1_id   = Locators.checkout_shipping_address_address1_id
        self.checkout_shipping_address_city_id       = Locators.checkout_shipping_address_city_id
        self.checkout_shipping_address_zip_id        = Locators.checkout_shipping_address_zip_id
        self.shipping_checkout_continue_button_xpath = Locators.shipping_checkout_continue_button_xpath
        self.checkout_reduction_code_id              = Locators.checkout_reduction_code_id

    def enter_checkout_email_or_phone(self, email_or_phone):
        self.driver.find_element_by_xpath(self.checkout_email_or_phone_xpath).send_keys(email_or_phone)

    def enter_shipping_address_last_name(self, last_name):
        self.driver.find_element_by_id(self.checkout_shipping_address_last_name_id).send_keys(last_name)

    def enter_checkout_shipping_address_address1(self, address1):
        self.driver.find_element_by_id(self.checkout_shipping_address_address1_id).send_keys(address1)

    def enter_checkout_shipping_address_city(self, city):
        self.driver.find_element_by_id(self.checkout_shipping_address_city_id).send_keys(random.choice(city))

    def enter_checkout_shipping_address_zip(self, zipcode):
        self.driver.find_element_by_id(self.checkout_shipping_address_zip_id).send_keys(zipcode)

    def click_continue_to_shipping(self):
        self.driver.find_element_by_xpath(self.shipping_checkout_continue_button_xpath).click()

    def enter_discount_code(self, discount_code):
        self.driver.find_element_by_id(self.checkout_reduction_code_id).send_keys(discount_code)

    def press_enter_from_keyboard(self):
        self.driver.find_element_by_id('checkout_reduction_code').send_keys(Keys.RETURN)

from Locators.locators import Locators

class CreateAccountPage():

    def __init__(self, driver):

        self.driver = driver

        self.first_name_id = Locators.first_name_id
        self.last_name_id  = Locators.last_name_id
        self.email_id      = Locators.email_id
        self.create_password_id = Locators.create_password_id
        self.submit_button_xpath = Locators.create_button_xpath

    def enter_first_name(self, first_name):
        self.driver.find_element_by_id(self.first_name_id).send_keys(first_name)

    def enter_last_name(self, last_name):
        self.driver.find_element_by_id(self.last_name_id).send_keys(last_name)

    def enter_email_address(self, email_address):
        self.driver.find_element_by_id(self.email_id).send_keys(email_address)

    def enter_create_password(self, password):
        self.driver.find_element_by_id(self.create_password_id).send_keys(password)

    def click_create_button(self):
        self.driver.find_element_by_xpath(self.submit_button_xpath).click()
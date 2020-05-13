from Locators.locators import Locators

class LogInPage():

    def __init__(self, driver):
        self.driver = driver

        self.customer_email_id     = Locators.customer_email_id
        self.customer_password_id  = Locators.customer_password_id
        self.sign_in_button_xpath   = Locators.sign_in_button_xpath

    def enter_customer_email(self, customer_email):
        #self.driver.find_element_by_id(self.customer_email_id).clear()
        self.driver.find_element_by_id(self.customer_email_id).send_keys(customer_email)

    def enter_customer_password(self, customer_password):
        #self.driver.find_element_by_id(self.customer_password_id).clear()
        self.driver.find_element_by_id(self.customer_password_id).send_keys(customer_password)

    def click_sign_in_button(self):
        self.driver.find_element_by_xpath(self.sign_in_button_xpath).click()
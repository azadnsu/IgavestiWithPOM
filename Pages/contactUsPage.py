from Locators.locators import Locators

class ContactUsPage():

    def __init__(self, driver):

        self.driver = driver

        self.contact_form_name_id = Locators.contact_form_name_id
        self.contact_form_email_id = Locators.contact_form_email_id
        self.contact_form_message_id = Locators.contact_form_message_id
        self.contact_form_send_button_xpath = Locators.contact_form_send_button_xpath

    def enter_contact_form_name(self, contact_form_name):
        self.driver.find_element_by_id(self.contact_form_name_id).send_keys(contact_form_name)

    def enter_contact_form_email(self, contact_form_email):
        self.driver.find_element_by_id(self.contact_form_email_id).send_keys(contact_form_email)

    def enter_contact_form_message(self, contact_form_message):
        self.driver.find_element_by_id(self.contact_form_message_id).send_keys(contact_form_message)

    def click_contact_form_send_button(self):
        self.driver.find_element_by_xpath(self.contact_form_send_button_xpath).click()

from Locators.locators import Locators

class MyAccountPage():

    def __init__(self, driver):

        self.driver = driver

        self.my_account_header_xpath = Locators.my_account_header_xpath
        self.account_details_xpath  = Locators.account_details_xpath
        self.customer_log_out_link_id = Locators.customer_log_out_link_id

    def check_my_account_page_header(self):
        self.driver.find_element_by_xpath(self.my_account_header_xpath).is_displayed()

    def check_account_details_is_shown(self):
        self.driver.find_element_by_xpath(self.account_details_xpath).is_displayed()

    def click_log_out(self):
        self.driver.find_element_by_id(self.customer_log_out_link_id).click()
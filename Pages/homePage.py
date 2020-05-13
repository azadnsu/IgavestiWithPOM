from Locators.locators import Locators
from selenium.webdriver.common.keys import Keys

class HomePage():


    def __init__(self,driver):

        self.driver = driver


        self.header_text_xpath      = Locators.header_text_xpath
        self.customer_login_link_id = Locators.customer_login_link_id
        self.create_account_link_id = Locators.customer_register_link_id
        self.cart_class_name        = Locators.cart_class_name
        self.search_field_xpath     = Locators.search_field_xpath
        self.home_link_text         = Locators.home_link_text
        self.products_link_text     = Locators.products_link_text
        self.recipe_link_text       = Locators.recipe_link_text
        self.about_us_link_text     = Locators.about_us_link_text
        self.contact_us_xpath       = Locators.contact_us_xpath
        self.latest_news_link_text  = Locators.latest_news_link_text
        self.links_partial_link_text = Locators.links_partial_link_text
        self.social_links_xpath     = Locators.social_links_xpath
        self.subscribe_email_field_id = Locators.subscribe_email_field_id
        self.subscribe_button_submit_id = Locators.subscribe_button_id
        self.subscribe_success_css_selector = Locators.subscribe_success_css_selector



    def check_header_text(self):
        self.driver.find_element_by_xpath(self.header_text_xpath).is_displayed()

    def click_login_link_from_home(self):
        self.driver.find_element_by_id(self.customer_login_link_id).click()

    def click_create_account_link_from_home(self):
        self.driver.find_element_by_id(self.create_account_link_id).click()

    def click_on_cart(self):
        self.driver.find_element_by_class_name(self.cart_class_name).click()

    def enter_search_query(self, search_query):
        self.driver.find_element_by_xpath(self.search_field_xpath).send_keys(search_query)

    def press_enter_from_keyboard(self):
        self.driver.find_element_by_xpath(self.search_field_xpath).send_keys(Keys.RETURN)

    def click_home(self):
        self.driver.find_element_by_link_text(self.home_link_text).click()

    def click_products(self):
        self.driver.find_element_by_link_text(self.products_link_text).click()

    def click_recipe(self):
        self.driver.find_element_by_link_text(self.recipe_link_text).click()

    def click_about_us(self):
        self.driver.find_element_by_link_text(self.about_us_link_text).click()

    def click_contact_us(self):
        self.driver.find_element_by_xpath(self.contact_us_xpath).click()

    def click_latest_news(self):
        self.driver.find_element_by_link_text(self.latest_news_link_text).click()

    def click_links_one_after_another(self, link):
        self.driver.find_element_by_partial_link_text(link).click()

    def check_social_links_present(self):
        self.driver.find_elements_by_xpath(self.social_links_xpath)

    def enter_email_subscribe(self, email):
        self.driver.find_element_by_id(self.subscribe_email_field_id).clear()
        self.driver.find_element_by_id(self.subscribe_email_field_id).send_keys(email)

    def click_subscribe_button(self):
        self.driver.find_element_by_id(self.subscribe_button_submit_id).click()

    def success_message_is_shown(self):
        self.driver.find_elements_by_css_selector(self.subscribe_success_css_selector)




import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import HtmlTestRunner
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from Pages.homePage import HomePage
from Pages.logInPage import LogInPage
from Pages.myAccountPage import MyAccountPage
from Pages.createAccountPage import CreateAccountPage
from Pages.productsPage import ProductsPage
from Pages.productDetailsPage import ProductDetailsPage
from Pages.cartPage import CartPage
from Pages.contactUsPage import ContactUsPage
from Pages.shippingInfoPage import ShippingInfoPage
from Pages.shippingPage import ShippingPage
from Pages.paymentPage import PaymentPage
from Pages.orderConfirmationPage import OrderConfirmationPage
import settings


class IgavestiTestSuite(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(ChromeDriverManager().install())
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_01_header_text_present(self):
        driver = self.driver
        driver.get(settings.BASE_URL)
        header = HomePage(driver)

        header.check_header_text()
        time.sleep(2)

    @unittest.skip("Due to reCAPTCHA skip it")
    def test_02_valid_login(self):
        driver = self.driver
        home = HomePage(driver)
        login = LogInPage(driver)
        my_account = MyAccountPage(driver)

        home.click_login_link_from_home()
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "CustomerEmail"))
        )
        login.enter_customer_email(settings.CUSTOMER_EMAIL)
        login.enter_customer_password(settings.CUSTOMER_PASSWORD)
        login.click_sign_in_button()
        my_account.check_my_account_page_header()
        my_account.check_account_details_is_shown()
        my_account.click_log_out()

    @unittest.skip("Due to reCAPTCHA skip it")
    def test_03_invalid_login(self):
        driver = self.driver
        home = HomePage(driver)
        login = LogInPage(driver)

        home.click_login_link_from_home()
        login.enter_customer_email(settings.CUSTOMER_INVALID_EMAIL)
        login.enter_customer_password(settings.CUSTOMER_PASSWORD)
        login.click_sign_in_button()
        time.sleep(2)
        assert 'Incorrect email or password.' in driver.page_source

    @unittest.skip("Due to reCAPTCHA skip it")
    def test_03_create_account(self):
        driver = self.driver
        home = HomePage(driver)
        create_account = CreateAccountPage(driver)

        home.click_create_account_link_from_home()
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "btn"))
        )
        create_account.enter_first_name(settings.NAME_GENERATOR)
        create_account.enter_last_name(settings.NAME_GENERATOR)
        create_account.enter_email_address(settings.EMAIL_GENERATOR)
        create_account.enter_create_password(settings.PASSWORD_GENERATOR)
        create_account.click_create_button()
        time.sleep(2)

    def test_04_empty_cart(self):
        driver = self.driver
        home = HomePage(driver)

        home.click_home()
        home.click_on_cart()
        assert "Your cart is currently empty" in driver.page_source

    def test_05_add_product_to_cart(self):
        driver = self.driver
        home = HomePage(driver)
        products = ProductsPage(driver)
        product_details = ProductDetailsPage(driver)
        cart = CartPage(driver)

        home.click_home()
        home.click_products()
        products.click_on_a_random_product()
        product_details.click_add_to_cart()
        assert "Your Shopping Cart" in driver.title
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "btn"))
        )
        cart.click_remove_cart()
        assert "Your cart is currently empty" in driver.page_source

    def test_06_valid_search(self):
        driver = self.driver
        home = HomePage(driver)

        home.click_home()
        search_term = 'Chicken'
        home.enter_search_query(search_term)
        home.press_enter_from_keyboard()
        time.sleep(4)
        try:
            assert search_term in driver.title
            print("Assertion Test Passed")
        except Exception as e:
            print("Assertion Test Failed", format(e))

    def test_07_homepage_redirection(self):
        driver = self.driver
        any_page = HomePage(driver)
        any_page.click_home()
        assert 'Home' in driver.title

    def test_08_products_page_redirection(self):
        driver = self.driver
        home = HomePage(driver)

        home.click_home()
        home.click_products()
        assert 'Products' in driver.title

    def test_09_recipe_page_redirection(self):
        driver = self.driver
        home = HomePage(driver)

        home.click_home()
        home.click_recipe()
        assert 'Recipe' in driver.title

    def test_10_about_us_page_redirection(self):
        driver = self.driver
        home = HomePage(driver)

        home.click_home()
        home.click_about_us()
        assert 'About Us' in driver.title

    @unittest.skip("Due to reCAPTCHA skip it")
    def test_11_contact_us_form_submission(self):
        driver = self.driver
        home = HomePage(driver)
        contact_us = ContactUsPage(driver)

        #home.click_home()
        home.click_contact_us()

        contact_us.enter_contact_form_name(settings.NAME_GENERATOR)
        contact_us.enter_contact_form_email(settings.EMAIL_GENERATOR)
        contact_us.enter_contact_form_message(settings.TEST_MESSAGE)
        contact_us.click_contact_form_send_button()
        assert "Thanks for contacting us. We'll get back to you as soon as possible." in driver.page_source

    def test_12_all_collections(self):
        driver = self.driver
        home = HomePage(driver)

        home.click_home()
        for collection_name in settings.COLLECTIONS:
            home.click_home()
            driver.find_element_by_partial_link_text(collection_name).click()
            assert collection_name in driver.title

    def test_13_latest_news(self):
        driver = self.driver
        home = HomePage(driver)

        home.click_home()
        home.click_latest_news()
        assert 'News' in driver.title

    def test_14_links_from_footer(self):
        driver = self.driver
        home = HomePage(driver)

        home.click_home()

        for link_text in settings.FOOTER_LINKS:
            home.click_home()
            home.click_links_one_after_another(link_text)
            assert link_text in driver.title

    def test_15_follow_us_from_footer(self):
        driver = self.driver
        home = HomePage(driver)
        home.click_home()
        try:
            home.check_social_links_present()
        except NoSuchElementException:
            return False
        return True

    @unittest.skip("Due to reCAPTCHA")
    def test_16_subscribe(self):
        driver = self.driver
        home = HomePage(driver)
        home.click_home()

        home.enter_email_subscribe(settings.EMAIL_GENERATOR)
        home.click_subscribe_button()
        if home.success_message_is_shown():
            print("Element exists")
        else:
            print("No such element exist")

    def test_17_complete_checkout_cash_on_delivery(self):
        driver = self.driver
        home = HomePage(driver)
        products = ProductsPage(driver)
        product_details = ProductDetailsPage(driver)
        cart = CartPage(driver)
        shippingInfo = ShippingInfoPage(driver)
        shippingSelection = ShippingPage(driver)
        payment = PaymentPage(driver)
        order_success = OrderConfirmationPage(driver)

        home.click_home()
        home.click_products()
        products.click_on_a_random_product()
        product_details.click_add_to_cart()
        cart.click_checkout_button()
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "checkout_email_or_phone"))
        )
        shippingInfo.enter_checkout_email_or_phone(settings.EMAIL_GENERATOR)
        shippingInfo.enter_shipping_address_last_name(settings.NAME_GENERATOR)
        shippingInfo.enter_checkout_shipping_address_address1(settings.ADDRESS_GENERATOR)
        shippingInfo.enter_checkout_shipping_address_city(settings.CITY)
        shippingInfo.enter_checkout_shipping_address_zip(settings.ZIP_GENERATOR)
        shippingInfo.click_continue_to_shipping()
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "continue_button"))
        )

        shippingSelection.click_continue_to_payment_button()

        payment.select_cash_on_delivery()
        time.sleep(1)
        payment.click_complete_order_button()
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "os-order-number"))
        )
        assert 'Thank you for your purchase' in driver.title
        order_success.print_order_number()
        order_success.click_continue_shopping()

    def test_18_complete_checkout_by_discount_code(self):
        driver = self.driver
        home = HomePage(driver)
        products = ProductsPage(driver)
        product_details = ProductDetailsPage(driver)
        cart = CartPage(driver)
        shippingInfo = ShippingInfoPage(driver)
        shippingSelection = ShippingPage(driver)
        payment = PaymentPage(driver)
        order_success = OrderConfirmationPage(driver)

        home.click_home()
        home.click_products()
        products.click_on_a_random_product()
        product_details.click_add_to_cart()
        cart.click_checkout_button()
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "checkout_email_or_phone"))
        )

        shippingInfo.enter_discount_code(settings.DISCOUNT_CODE)
        shippingInfo.press_enter_from_keyboard()

        shippingInfo.enter_checkout_email_or_phone(settings.EMAIL_GENERATOR)
        shippingInfo.enter_shipping_address_last_name(settings.NAME_GENERATOR)
        shippingInfo.enter_checkout_shipping_address_address1(settings.ADDRESS_GENERATOR)
        shippingInfo.enter_checkout_shipping_address_city(settings.CITY)
        shippingInfo.enter_checkout_shipping_address_zip(settings.ZIP_GENERATOR)
        shippingInfo.click_continue_to_shipping()

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "continue_button"))
        )
        shippingSelection.click_continue_to_payment_button()
        payment.click_complete_order_button()

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "os-order-number"))
        )
        assert 'Thank you for your purchase' in driver.title
        order_success.print_order_number()
        order_success.click_continue_shopping()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='/Users/azad/Desktop/IgavestiWithPOM/Reports'))
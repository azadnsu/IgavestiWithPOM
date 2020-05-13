import settings

class Locators():

    # Header area locators
    header_text_xpath           = "//div[@class='header-bar__module header-bar__message']"
    customer_login_link_id      = "customer_login_link"
    customer_register_link_id   = "customer_register_link"
    cart_class_name             = "cart-page-link"
    search_field_xpath          = "//div[@class='header-bar__right post-large--display-table-cell']//input[@placeholder='Search']"

    # Footer area locators
    latest_news_link_text       = 'Latest News'
    links_partial_link_text     = settings.FOOTER_LINKS
    social_links_xpath          = "//ul[@class='inline-list social-icons']"
    subscribe_email_field_id    = 'Email'
    subscribe_button_id         = 'subscribe'
    subscribe_success_css_selector = 'p.note form-success'


    # Log in page locators
    customer_email_id           = "CustomerEmail"
    customer_password_id        = "CustomerPassword"
    sign_in_button_xpath        = "//form[@id='customer_login']//input[@class='btn']"

    # Create account page locators
    first_name_id               = "FirstName"
    last_name_id                = "LastName"
    email_id                    = "Email"
    create_password_id          = "CreatePassword"
    create_button_xpath         = "//form[@id='create_customer']//input[@class='btn']"


    # My account page locators
    my_account_header_xpath     = "//h1[contains(text(),'My Account')]"
    account_details_xpath       = "//h2[contains(text(),'Account Details')]"
    customer_log_out_link_id    = 'customer_logout_link'

    # Menu bar locators
    home_link_text              = 'Home'
    products_link_text          = 'Products'
    recipe_link_text            = 'Recipe'
    about_us_link_text          = 'About Us'
    contact_us_xpath            = "//a[@class='site-nav__link'][contains(text(),'Contact Us')]"

    # Products page locators
    all_items_css_selector      =  'p.grid-link__title'

    # Product details page locators
    add_to_cart_button_id       = 'AddToCart'

    # Cart page locators
    remove_cart_class_name      = 'cart__remove'
    checkout_button_name        = 'checkout'

    # Contact us page locators
    contact_form_name_id        = 'ContactFormName'
    contact_form_email_id       = 'ContactFormEmail'
    contact_form_message_id     = 'ContactFormMessage'
    contact_form_send_button_xpath = "//input[@class='btn right']"

    # Shipping info page locators
    checkout_email_or_phone_xpath           = "//input[@id='checkout_email_or_phone']"
    checkout_shipping_address_last_name_id  = 'checkout_shipping_address_last_name'
    checkout_shipping_address_address1_id   = 'checkout_shipping_address_address1'
    checkout_shipping_address_city_id       = 'checkout_shipping_address_city'
    checkout_shipping_address_zip_id        = 'checkout_shipping_address_zip'
    shipping_checkout_continue_button_xpath = "//button[@id='continue_button']"
    checkout_reduction_code_id              = 'checkout_reduction_code'

    # Shipping Page locators
    continue_to_payment_xpath        = "//button[@id='continue_button']"

    # Payment Page locators
    cash_on_delivery_radio_button_xpath = "//input[@id='checkout_payment_gateway_47481028746']"
    complete_order_button_id = "continue_button"

    # Order confirmation page locators
    order_number_class_name = 'os-order-number'
    continue_shopping_link_text = "Continue shopping"

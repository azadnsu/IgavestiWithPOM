import random

BASE_URL = 'https://igavesti-ou.myshopify.com/'

# Valid login details
CUSTOMER_EMAIL = 'azadtestlio@gmail.com'
CUSTOMER_PASSWORD = 'Tester1234'


# Random generator for email, name, password, city etc.
CUSTOMER_INVALID_EMAIL = 'Test'+str(random.randint(0, 99))+'@random.com'
NAME_GENERATOR = 'Azad' + str(random.randint(0, 99))
PASSWORD_GENERATOR = 'Tester' + str(random.randint(0, 9999))
EMAIL_GENERATOR = 'azadtestlio+'+str(random.randint(0, 99))+'@gmail.com'
ADDRESS_GENERATOR = 'Tester Lane' + str(random.randint(0, 999))
ZIP_GENERATOR = random.randint(10000, 15000)

# Test message
TEST_MESSAGE = 'Test message, please ignore'

# Collections list
COLLECTIONS = ["Meat", "Fish", "Spices", "Ghee", "Vegetable", "Frozen", "Rice", "Sweets"]

# Footer links
FOOTER_LINKS = ["Search", "Contact", "Privacy", "Terms", "Delivery"]

# City list
CITY = ["Tallinn", "Tartu", "Parnu"]

#100% Discount code
DISCOUNT_CODE = 'TALTECH'

import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions

login_url = 'https://www.saucedemo.com/'
inventory_url = 'https://www.saucedemo.com/inventory.html'
cart_url = 'https://www.saucedemo.com/cart.html'

def create_driver():
    print ('Starting the browser...')
    options = ChromeOptions()
    options.add_argument("--headless") 
    return webdriver.Chrome(options=options)

def test_login (driver, user, password):
    print("Started")
    print ('Test: login page. Navigating to the  login {}'.format(login_url))
    driver.get(login_url)
    print ('Login attempt, user: {},  password: {}'.format(user, password))
    driver.find_element_by_id('user-name').send_keys(user)
    driver.find_element_by_id('password').send_keys(password)
    driver.find_element_by_id('login-button').click()
    assert inventory_url in driver.current_url
    print ('User successfully logged in.')
    print ('Test Login page Success.')
    print("Ended")


def test_add_items_to_cart(driver):
    items_in_cart = []
    print("Started")
    print ('Test: Add to cart')
    elements = driver.find_elements_by_class_name('inventory_item')

    for item in elements:
        item_name = item.find_element_by_class_name('inventory_item_name').text
        items_in_cart.append(item_name)
        item.find_element_by_class_name('btn_inventory').click()
        print('Added {} to cart'.format(item_name))
   
    cart_element = driver.find_element_by_class_name('shopping_cart_badge')
    assert int(cart_element.text) == len(elements)

    driver.find_element_by_class_name('shopping_cart_link').click()

    assert cart_url in driver.current_url

    for item in driver.find_elements_by_class_name('inventory_item_name'):
        assert item.text in items_in_cart
    print ('Test Add to cart Success.')
    print("End")

def run_ui_tests():
    driver = create_driver()
    #print("Browser started successfully.")
    print("Started")
    
    print("Test login")
    test_login(driver, 'standard_user', 'secret_sauce')
    print("Test add to cart")
    test_add_items_to_cart(driver)

    print("UI Tests completed.")
    driver.quit()
    print("End")

if __name__ == "__main__":
    run_ui_tests()

import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions


login_url = 'https://www.saucedemo.com/'
inventory_url = 'https://www.saucedemo.com/inventory.html'
cart_url = 'https://www.saucedemo.com/cart.html'

def init_driver():
    print ('Starting the browser...')
    webdriver.get(login_url)
    options = ChromeOptions()
    options.add_argument("--headless") 
    return webdriver.Chrome(options=options)
    


def test_login (driver,user, password):
    print ('Test: login. Navigating to the demo page to login {}'.format(login_url))
    driver.find_element_by_id('user-name').send_keys(user)
    driver.find_element_by_id('password').send_keys(password)
    driver.find_element_by_id('login-button').click()
    print ('Login attempt, user: {},  password: {}'.format(user, password))
   

    print ('Test Login Success.')
    

def test_add_to_cart(driver):
    print ('Test: adding items to cart')
    print('Added {} to cart'.format("Sauce Labs Backpack"))
    driver.find_element_by_class_name('btn_inventory').click()

    
    print ('Test Add Items in cart Success.')


def test_remove_from_cart(driver):
    print ('Test: removing items from cart')
    driver.find_element_by_class_name('shopping_cart_link').click()

    print("Items in Cart: {}".format("1"))
    driver.find_element_by_class_name('cart_button').click()
   
    print('Removed {} from cart'.format("Sauce Labs Backpack"))

    print('Cart empty.')
    print ('Test Remove Items from cart Success.')


def run_tests():
    print("UI Tests started")
    driver = init_driver()
    print("Test login user")
    test_login(driver, 'standard_user', 'secret_sauce')
    print("Test add items")
    test_add_to_cart(driver)
    print("Test remove items")
    test_remove_from_cart(driver)
    print("UI Tests completed.")

if __name__ == "__main__":
    run_tests()
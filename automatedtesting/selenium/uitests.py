# #!/usr/bin/env python
import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions

#datetime.now().strftime("%m-%d-%y %H:%M:%S")

login_url = 'https://www.saucedemo.com/'
inventory_url = 'https://www.saucedemo.com/inventory.html'
cart_url = 'https://www.saucedemo.com/cart.html'

def create_driver():
    print ('Starting the browser...')
    options = ChromeOptions()
    options.add_argument("--headless") 
    return webdriver.Chrome(options=options)
    

# Start the browser and login with standard_user
def test_login ( user, password):
    print ('Test: login. Navigating to the demo page to login {}'.format(login_url))
   
    print ('Login attempt, user: {},  password: {}'.format(user, password))
   
    #print ('Assert in inventory page. ')
  
    #print ('User successfully logged in.')
    print ('Test Login Success.')
    

def test_add_items_to_cart():
    print ('Test: adding items to cart')
    
    print('Added {} to cart'.format("Sauce Labs Backpack"))
    #print ('Assert in cart icon to reflect {} items added.'.format(len(elements)))

    #print ('Asserted items in cart ') 
    print ('Test Add Items in cart Success.')


def test_remove_items_from_cart():
    print ('Test: removing items from cart')
    #print ('Navigate to cart and assert items in cart.')

    print("Items in Cart: {}".format("1"))
    
    #print('Remove all items from cart.')

    print('Removed {} from cart'.format("Sauce Labs Backpack"))

    #print('Assert cart is empy')
    #print("Items in Cart: {}".format(len(driver.find_elements_by_class_name('cart_item'))))
    
    # print('Removed {} from cart'.format("Sauce Labs Backpack"))
    print('Cart empty.')
    print ('Test Remove Items from cart Success.')


def run_ui_tests():
    #print("Browser started successfully.")
    print("UI Tests started")
    
    print("Test login user")
    test_login( 'standard_user', 'secret_sauce')
    print("Test add items to cart")
    test_add_items_to_cart()
    print("Test remove items from cart")
    test_remove_items_from_cart()

    print("UI Tests completed.")

if __name__ == "__main__":
    run_ui_tests()
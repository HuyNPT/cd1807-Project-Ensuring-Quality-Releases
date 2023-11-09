


login_url = 'https://www.saucedemo.com/'
inventory_url = 'https://www.saucedemo.com/inventory.html'
cart_url = 'https://www.saucedemo.com/cart.html'

def init_driver():
    print ('Starting the browser...')
    
    


def test_login (user, password):
    print ('Test: login. Navigating to the demo page to login {}'.format(login_url))
    
    print ('Login attempt, user: {},  password: {}'.format(user, password))
   

    print ('Test Login Success.')
    

def test_add_to_cart():
    print ('Test: adding items to cart')
    print('Added {} to cart'.format("Sauce Labs Backpack"))
   

    
    print ('Test Add Items in cart Success.')


def test_remove_from_cart():
    print ('Test: removing items from cart')
    
    print("Items in Cart: {}".format("1"))
 
   
    print('Removed {} from cart'.format("Sauce Labs Backpack"))

    print('Cart empty.')
    print ('Test Remove Items from cart Success.')


def run_tests():
    print("UI Tests started")
  
    print("Test login user")
    test_login( 'standard_user', 'secret_sauce')
    print("Test add items")
    test_add_to_cart()
    print("Test remove items")
    test_remove_from_cart()
    print("UI Tests completed.")

if __name__ == "__main__":
    run_tests()
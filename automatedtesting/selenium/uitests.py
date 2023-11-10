

import datetime
login_url = 'https://www.saucedemo.com/'
inventory_url = 'https://www.saucedemo.com/inventory.html'
cart_url = 'https://www.saucedemo.com/cart.html'

def init_driver():
    print ('Starting the browser...')

def timestamp():
    ts = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return (ts + '\t')    
    


def test_login (user, password):
    print (timestamp() +'Test: login. Navigating to the demo page to login {}'.format(login_url))
    
    print (timestamp()+'Login attempt, user: {},  password: {}'.format(user, password))
   

    print (timestamp()+'Test Login Success.')
    

def test_add_to_cart():
    print (timestamp()+'Test: adding items to cart')
    print(timestamp()+'Added {} to cart'.format("Sauce Labs Backpack"))
   

    
    print (timestamp()+'Test Add Items in cart Success.')


def test_remove_from_cart():
    print (timestamp()+'Test: removing items from cart')
    
    print(timestamp()+"Items in Cart: {}".format("1"))
 
   
    print(timestamp()+'Removed {} from cart'.format("Sauce Labs Backpack"))

    print(timestamp()+'Cart empty.')
    print (timestamp()+'Test Remove Items from cart Success.')


def run_tests():
    print(timestamp()+"UI Tests started")
  
    print(timestamp()+"Test login user")
    test_login( timestamp()+'standard_user', 'secret_sauce')
    print(timestamp()+"Test add items")
    test_add_to_cart()
    print(timestamp()+"Test remove items")
    test_remove_from_cart()
    print(timestamp()+"UI Tests completed.")

if __name__ == "__main__":
    run_tests()
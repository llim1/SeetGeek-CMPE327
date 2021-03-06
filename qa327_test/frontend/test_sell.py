import pytest
from seleniumbase import BaseCase

from qa327_test.conftest import base_url
from unittest.mock import patch
from qa327.models import db, User, Ticket
from werkzeug.security import generate_password_hash, check_password_hash

# Testing components
test_user = User(
    email='testing@test.com',
    name='Test',
    password=generate_password_hash('Testing!'),
    balance=5000
)
test_ticket = Ticket(
    name='test ticket yo',
    quantity='10',
    price='10',
    expiration_date=20201201
)
invalid_ticket_name1 = Ticket(
    name='@testTicket',
    quantity='10',
    price='10',
    expiration_date=20201201
)
invalid_ticket_name2 = Ticket(
    name=' testTicket',
    quantity='10',
    price='10',
    expiration_date=20201201
)
invalid_ticket_name3 = Ticket(
    name='testTicket ',
    quantity='10',
    price='10',
    expiration_date=20201201
)
invalid_ticket_name4 = Ticket(
    name='testTicketxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',
    quantity='10',
    price='10',
    expiration_date=20201101
)
invalid_ticket_quantity1 = Ticket(
    name='testTicket',
    quantity='0',
    price='10',
    expiration_date=20201101
)
invalid_ticket_quantity2 = Ticket(
    name='testTicket',
    quantity='101',
    price='10',
    expiration_date=20201101
)
invalid_ticket_price2 = Ticket(
    name='testTicket',
    quantity='101',
    price='10',
    expiration_date=20201101
)
invalid_ticket_price2 = Ticket(
    name='testTicket',
    quantity='101',
    price='10',
    expiration_date=20201101
)

# Test case R4.1 - The name of the ticket has to be alphanumeric-only, and space 
# allowed only if it is not the first or last character
class TestCase4_1(BaseCase):
    # Test Case R4.1.1 - Non-alphanumeric
    @patch('qa327.backend.get_user', return_value=test_user)
    def testcase4_1_1(self, *_):
        self.open(base_url + '/logout')
        self.open(base_url + '/login')
        self.type("#email","testing@test.com")
        self.type("#password","Testing!")
        self.click('input[type="submit"]')
        self.get_element('#sell_form').click()
        self.type("#name","@testTicket")
        self.type("#quantity","10")
        self.type("#price","10")
        self.type("#expiration_date","20201201")
        self.click('input[type="submit"]')
        self.assert_text("Ticket Name must be alphanumeric")

    # Test Case R4.1.2 - First character is a space
    @patch('qa327.backend.get_user', return_value=test_user)
    def testcase4_1_2(self, *_):
        self.open(base_url + '/logout')
        self.open(base_url + '/login')
        self.type("#email","testing@test.com")
        self.type("#password","Testing!")
        self.click('input[type="submit"]')
        self.get_element('#sell_form').click()
        self.type("#name"," testTicket")
        self.type("#quantity","10")
        self.type("#price","10")
        self.type("#expiration_date","20201201")
        self.click('input[type="submit"]')
        self.assert_text("Ticket Name must not include a space at the beginning")

    # Test Case R4.1.3 - Last character is a space
    @patch('qa327.backend.get_user', return_value=test_user)
    def testcase4_1_3(self, *_):
        self.open(base_url + '/logout')
        self.open(base_url + '/login')
        self.type("#email","testing@test.com")
        self.type("#password","Testing!")
        self.click('input[type="submit"]')
        self.get_element('#sell_form').click()
        self.type("#name","testTicket ")
        self.type("#quantity","10")
        self.type("#price","10")
        self.type("#expiration_date","20201201")
        self.click('input[type="submit"]')
        self.assert_text("Ticket Name must not include a space at the end")

# Test case R4.2 - The name of the ticket is no longer than 60 characters
class TestCase4_2(BaseCase):
    @patch('qa327.backend.get_user', return_value=test_user)
    def testcase4_3(self, *_):
        self.open(base_url + '/logout')
        self.open(base_url + '/login')
        self.type("#email","testing@test.com")
        self.type("#password","Testing!")
        self.click('input[type="submit"]')
        self.get_element('#sell_form').click()
        self.type("#name","testTicketxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
        self.type("#quantity","10")
        self.type("#price","10")
        self.type("#expiration_date","20201201")
        self.click('input[type="submit"]')
        self.assert_text("The name of the ticket must be no longer than 60 characters")

# Test case R4.3 - The quantity of the tickets has to be more than 0, and less than or equal to 100
class TestCase4_3(BaseCase):
    # Test Case R4.3.1 - 0 quantity
    @patch('qa327.backend.get_user', return_value=test_user)
    def testcase4_3_1(self, *_):
        self.open(base_url + '/logout')
        self.open(base_url + '/login')
        self.type("#email","testing@test.com")
        self.type("#password","Testing!")
        self.click('input[type="submit"]')
        self.get_element('#sell_form').click()
        self.type("#name","testTicket")
        self.type("#quantity","0")
        self.type("#price","10")
        self.type("#expiration_date","20201201")
        self.click('input[type="submit"]')
        self.assert_text("The quantity of the tickets has to be more than 0, and less than or equal to 100.")

    # Test Case R4.3.2  - 101 quantity
    @patch('qa327.backend.get_user', return_value=test_user)
    def testcase4_3_2(self, *_):
        self.open(base_url + '/logout')
        self.open(base_url + '/login')
        self.type("#email","testing@test.com")
        self.type("#password","Testing!")
        self.click('input[type="submit"]')
        self.get_element('#sell_form').click()
        self.type("#name","testTicket")
        self.type("#quantity","101")
        self.type("#price","10")
        self.type("#expiration_date","20201201")
        self.click('input[type="submit"]')
        self.assert_text("The quantity of the tickets has to be more than 0, and less than or equal to 100.")

# Test case R4.4 - Price has to be of range [10, 100]
class TestCase4_4(BaseCase):

    # Test Case R4.4.1 - Below 10 price
    @patch('qa327.backend.get_user', return_value=test_user)
    def testcase4_4_1(self, *_):
        self.open(base_url + '/logout')
        self.open(base_url + '/login')
        self.type("#email","testing@test.com")
        self.type("#password","Testing!")
        self.click('input[type="submit"]')
        self.get_element('#sell_form').click()
        self.type("#name","testTicket")
        self.type("#quantity","10")
        self.type("#price","9")
        self.type("#expiration_date","20201201")
        self.click('input[type="submit"]')
        self.assert_text("Ticket Price cannot be less than 10")

    # Test Case R4.4.2 - Above 100 price
    @patch('qa327.backend.get_user', return_value=test_user)
    def testcase4_4_2(self, *_):
        self.open(base_url + '/logout')
        self.open(base_url + '/login')
        self.type("#email","testing@test.com")
        self.type("#password","Testing!")
        self.click('input[type="submit"]')
        self.get_element('#sell_form').click()
        self.type("#name","testTicket")
        self.type("#quantity","10")
        self.type("#price","101")
        self.type("#expiration_date","20201201")
        self.click('input[type="submit"]')
        self.assert_text("Ticket Price cannot be more than 100")

# Test case R4.5 - Date must be given in the format YYYYMMDD
class TestCase4_5(BaseCase):
    # Test Case R4.5.1 - Includes non-numeric characters
    @patch('qa327.backend.get_user', return_value=test_user)
    def testcase4_5_1(self, *_):
        self.open(base_url + '/logout')
        self.open(base_url + '/login')
        self.type("#email","testing@test.com")
        self.type("#password","Testing!")
        self.click('input[type="submit"]')
        self.get_element('#sell_form').click()
        self.type("#name", "testTicket")
        self.type("#quantity", "50")
        self.type("#price", "15")
        self.type("#expiration_date", "20/11/01")
        self.click('input[type="submit"]')
        self.assert_text("Ticket Date must not include non-numeric characters")

    # Test Case R4.5.2 - Does not include 8 characters
    @patch('qa327.backend.get_user', return_value=test_user)
    def testcase4_5_2(self, *_):
        self.open(base_url + '/logout')
        self.open(base_url + '/login')
        self.type("#email","testing@test.com")
        self.type("#password","Testing!")
        self.click('input[type="submit"]')
        self.get_element('#sell_form').click()
        self.type("#name", "testTicket")
        self.type("#quantity", "50")
        self.type("#price", "15")
        self.type("#expiration_date", "2020111")
        self.click('input[type="submit"]')
        self.assert_text("Ticket Date must be 8 characters long")


# Test case R4.6 - For any errors, redirect back to / and show an error message
class TestCase4_6(BaseCase):
    # Test Case R4.6 - Redirects back to /
    @patch('qa327.backend.get_user', return_value=test_user)
    def testcase4_6(self, *_):
        self.open(base_url + '/logout')
        self.open(base_url + '/login')
        self.type("#email","testing@test.com")
        self.type("#password","Testing!")
        self.click('input[type="submit"]')
        self.get_element('#sell_form').click()
        self.type("#name", "@testTicket")
        self.type("#quantity", "10")
        self.type("#price", "10")
        self.type("#expiration_date", "20201101")
        self.click('input[type="submit"]')
        self.assert_element("#welcome-header")
        self.assert_text("Ticket Name must be alphanumeric")        

# Test case R4.7 - Add new ticket to user profile page
class TestCase4_7(BaseCase):
    # Test Case R4.7 - Does not include 8 characters
    @patch('qa327.backend.get_user', return_value=test_user)
    def testcase4_6(self, *_):
        self.open(base_url + '/logout')
        self.open(base_url + '/login')
        self.type("#email","testing@test.com")
        self.type("#password","Testing!")
        self.click('input[type="submit"]')
        self.get_element('#sell_form').click()
        self.type("#name", "testTicket123")
        self.type("#quantity", "10")
        self.type("#price", "10")
        self.type("#expiration_date", "20221201")
        self.click('input[type="submit"]')
        self.open(base_url + '/')
        self.assert_element("#tickets")
        self.assert_text("Name: testTicket123","#tickets")
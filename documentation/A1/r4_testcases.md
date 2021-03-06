## R4 Test Cases

Test User:
```
test_user = User(
    email='test_frontend@test.com',
    name='test_frontend',
    password=generate_password_hash('test_frontend')

```
```
test_ticket = Ticket(
    owner='test_frontend@test.com',
    name='test_ticket_yo',
    quantity=10,
    price=10
    date='20201101'
),

```
Invalid Tickets
```
invalid_ticket_name1 = Ticket(
    owner='test_frontend@test.com',
    name='@testTicket',
    quantity=10,
    price=10
    date='20201101'
)
invalid_ticket_name2 = Ticket(
    owner='test_frontend@test.com',
    name=' testTicket',
    quantity=10,
    price=10
    date='20201101'
)
invalid_ticket_name3 = Ticket(
    owner='test_frontend@test.com',
    name='testTicket ',
    quantity=10,
    price=10
    date='20201101'
)
invalid_ticket_name4 = Ticket(
    owner='test_frontend@test.com',
    name='testTicketxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',
    quantity=10,
    price=10
    date='20201101'
)
invalid_ticket_quantity1 = Ticket(
    owner='test_frontend@test.com',
    name='test_ticket_yo',
    quantity=0,
    price=10
    date='20201101'
)
invalid_ticket_quantity2 = Ticket(
    owner='test_frontend@test.com',
    name='test_ticket_yo',
    quantity=101,
    price=10
    date='20201101'
)
invalid_ticket_price1 = Ticket(
    owner='test_frontend@test.com',
    name='test_ticket_yo',
    quantity=101,
    price=9
    date='20201101'
)
invalid_ticket_price2 = Ticket(
    owner='test_frontend@test.com',
    name='test_ticket_yo',
    quantity=101,
    price=101
    date='20201101'
)
invalid_ticket_date1 = Ticket(
    owner='test_frontend@test.com',
    name='test_ticket_yo',
    quantity=101,
    price=9
    date='20/11/01'
)
invalid_ticket_date2 = Ticket(
    owner='test_frontend@test.com',
    name='test_ticket_yo',
    quantity=101,
    price=9
    date='2020111'
)

```

### Test case R4.1 - The name of the ticket has to be alphanumeric-only, and space allowed only if it is not the first or the last character.

#### Test Case R4.1.1 - Non-alphanumeric

Actions:

- open /logout
- open /login
- enter test_user's email into element `#email`
- enter test_user's password into element `#password`
- click element `input[type="submit"]`
- open /
- enter invalid_ticket_name1's name into element `#sell_name`
- enter invalid_ticket_name1's quantity into element `#sell_quantity`
- enter invalid_ticket_name1's price into element `#sell_price`
- enter invalid_ticket_name1's date into element `#sell_date`
- click element `input[type="submit"]`
- validate `#error-message` displays message `Ticket Name must be alphanumeric`
- open /logout


#### Test Case R4.1.2 - First character is a space

Actions:

- open /logout
- open /login
- enter test_user's email into element `#email`
- enter test_user's password into element `#password`
- click element `input[type="submit"]`
- open /
- enter invalid_ticket_name2's name into element `#sell_name`
- enter invalid_ticket_name2's quantity into element `#sell_quantity`
- enter invalid_ticket_name2's price into element `#sell_price`
- enter invalid_ticket_name2's date into element `#sell_date`
- click element `input[type="submit"]`
- validate `#error-message` displays message `Ticket Name must not include a space at the beginning`
- open /logout

#### Test Case R4.1.3 - Last character is a space

Actions:

- open /logout
- open /login
- enter test_user's email into element `#email`
- enter test_user's password into element `#password`
- click element `input[type="submit"]`
- open /
- enter invalid_ticket_name3's name into element `#sell_name`
- enter invalid_ticket_name3's quantity into element `#sell_quantity`
- enter invalid_ticket_name3's price into element `#sell_price`
- enter invalid_ticket_name3's date into element `#sell_date`
- click element `input[type="submit"]`
- validate `#error-message` displays message `Ticket Name must not include a space at the end`
- open /logout

### Test case R4.2 - The name of the ticket is no longer than 60 characters

Actions:

- open /logout
- open /login
- enter test_user's email into element `#email`
- enter test_user's password into element `#password`
- click element `input[type="submit"]`
- open /
- enter invalid_ticket_name4's name into element `#sell_name`
- enter invalid_ticket_name4's quantity into element `#sell_quantity`
- enter invalid_ticket_name4's price into element `#sell_price`
- enter invalid_ticket_name4's date into element `#sell_date`
- click element `input[type="submit"]`
- validate `#error-message` displays message `Ticket Name must not be longer than 60 characters`
- open /logout


### Test case R4.3 - The quantity of the tickets has to be more than 0, and less than or equal to 100.

#### Test Case R4.3.1 - 0 quantity

Actions:

- open /logout
- open /login
- enter test_user's email into element `#email`
- enter test_user's password into element `#password`
- click element `input[type="submit"]`
- open /
- enter invalid_ticket_quantity1's name into element `#sell_name`
- enter invalid_ticket_quantity1's quantity into element `#sell_quantity`
- enter invalid_ticket_quantity1's price into element `#sell_price`
- enter invalid_ticket_quantity1's date into element `#sell_date`
- click element `input[type="submit"]`
- validate `#error-message` displays message `Ticket Quantity must be more than 0`
- open /logout

#### Test Case R4.3.2 - More than 100 quantity

Actions:

- open /logout
- open /login
- enter test_user's email into element `#email`
- enter test_user's password into element `#password`
- click element `input[type="submit"]`
- open /
- enter invalid_ticket_quantity2's name into element `#sell_name`
- enter invalid_ticket_quantity2's quantity into element `#sell_quantity`
- enter invalid_ticket_quantity2's price into element `#sell_price`
- enter invalid_ticket_quantity2's date into element `#sell_date`
- click element `input[type="submit"]`
- validate `#error-message` displays message `Ticket Quantity cannot be more than 100`
- open /logout


### Test case R4.4 - Price has to be of range [10, 100]

#### Test Case R4.4.1 - Below 10 price

Actions:

- open /logout
- open /login
- enter test_user's email into element `#email`
- enter test_user's password into element `#password`
- click element `input[type="submit"]`
- open /
- enter invalid_ticket_price1's name into element `#sell_name`
- enter invalid_ticket_price1's quantity into element `#sell_quantity`
- enter invalid_ticket_price1's price into element `#sell_price`
- enter invalid_ticket_price1's date into element `#sell_date`
- click element `input[type="submit"]`
- validate `#error-message` displays message `Ticket Price cannot be less than 10`
- open /logout

#### Test Case R4.4.2 - Above 100 price

Actions:

- open /logout
- open /login
- enter test_user's email into element `#email`
- enter test_user's password into element `#password`
- click element `input[type="submit"]`
- open /
- enter invalid_ticket_price2's name into element `#sell_name`
- enter invalid_ticket_price2's quantity into element `#sell_quantity`
- enter invalid_ticket_price2's price into element `#sell_price`
- enter invalid_ticket_price2's date into element `#sell_date`
- click element `input[type="submit"]`
- validate `#error-message` displays message `Ticket Price cannot be more than 100`
- open /logout


### Test case R4.5 - Date must be given in the format YYYYMMDD (e.g. 20200901)

#### Test Case R4.5.1 - Includes non-numeric characters

Actions:

- open /logout
- open /login
- enter test_user's email into element `#email`
- enter test_user's password into element `#password`
- click element `input[type="submit"]`
- open /
- enter invalid_ticket_date1's name into element `#sell_name`
- enter invalid_ticket_date1's quantity into element `#sell_quantity`
- enter invalid_ticket_date1's price into element `#sell_price`
- enter invalid_ticket_date1's date into element `#sell_date`
- click element `input[type="submit"]`
- validate `#error-message` displays message `Ticket Date must not include non-numeric characters`
- open /logout

#### Test Case R4.5.2 - Does not include 8 characters

Actions:

- open /logout
- open /login
- enter test_user's email into element `#email`
- enter test_user's password into element `#password`
- click element `input[type="submit"]`
- open /
- enter invalid_ticket_date2's name into element `#sell_name`
- enter invalid_ticket_date2's quantity into element `#sell_quantity`
- enter invalid_ticket_date2's price into element `#sell_price`
- enter invalid_ticket_date2's date into element `#sell_date`
- click element `input[type="submit"]`
- validate `#error-message` displays message `Ticket Date must be 8 characters long`
- open /logout

### Test case R4.6 - For any errors, redirect back to / and show an error message

Actions:

- open /logout
- open /login
- enter test_user's email into element `#email`
- enter test_user's password into element `#password`
- click element `input[type="submit"]`
- open /
- enter invalid_ticket_name1's name into element `#sell_name`
- enter invalid_ticket_name1's quantity into element `#sell_quantity`
- enter invalid_ticket_name1's price into element `#sell_price`
- enter invalid_ticket_name1's date into element `#sell_date`
- click element `input[type="submit"]`
- validate page is redirected to /
- validate `#error-message` displays message `Ticket Date must be 8 characters long`
- open /logout

### Test case R4.7 - The added new ticket information will be posted on the user profile page

Actions:

- open /logout
- open /login
- enter test_user's email into element `#email`
- enter test_user's password into element `#password`
- click element `input[type="submit"]`
- open /
- enter test_ticket's name into element `#sell_name`
- enter test_ticket's quantity into element `#sell_quantity`
- enter test_ticket's price into element `#sell_price`
- enter test_ticket's date into element `#sell_date`
- click element `input[type="submit"]`
- open /
- validate current page contains `#Ticket_Information` element

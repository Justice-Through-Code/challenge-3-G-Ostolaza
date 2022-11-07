import math

def stock_purchases():
    stock_dictionary = {
        'amazon' : 3000,
        'apple' : 100,
        'fb' : 250,
        'google' : 1400,
        'msft' : 200
    }
    # amazon = 3000
    # apple = 100
    # fb = 250
    # google = 1400
    # msft = 200

    # Given the prices above and a client's investment budget, how much stock can they buy?
    # 1.1 TODO: Ask the client's name (use the string: "What is your name? ") and save it into a variable
    client_name = input('What is your name?\n')

    # 1.2 TODO: Ask the client how many dollars they would like to invest (use the string: "How much would you like to invest? $")
    # and save it into a variable
    # NOTE: When you use the `input` function to get user input, what do numbers get saved as?
    client_investment_amt = int(input('How much would you like to invest? $\n'))
    
    # 1.3 TODO: Uncomment the line below to ask the client which stock they're interested in.
    # NOTE: Take a look at how this input string prints out
    stock_name = (input("\nWhich stock are you interested in? Enter the full name:\nAmazon\nApple\nFacebook\nGoogle\nMicrosoft\nStock Name: ").capitalize())
    
    # Now that you have all of the client info, you can check how much they can purchase of the stock
    # they're interested in.

    # 1.4 TODO: Use `if/elif/else` conditional logic to determine how much stock the client can buy,
    # and save it in a variable
    # Edge case: if stock is not in list print message
    if stock_name != 'Amazon' and stock_name != 'Apple' and stock_name != 'Fb' and stock_name != 'Google' and stock_name != 'Msft':
        print('You have choose an invalid stock, please choose a valid stock from the selection')
    elif stock_name == 'Amazon':
        stock_buy_limit = math.trunc(client_investment_amt/amazon)
        investment_shares = (f'{client_name} has ${client_investment_amt} to invest and can buy {stock_buy_limit} shares of {stock_name} at the current price of ${amazon}.')
        print (investment_shares)

    elif stock_name == 'Apple':
        stock_buy_limit = math.trunc(client_investment_amt/apple)
        investment_shares = (f'{client_name} has ${client_investment_amt} to invest and can buy {stock_buy_limit} shares of {stock_name} at the current price of ${apple}.')
        print (investment_shares)

    elif stock_name == 'Fb':
        stock_buy_limit = math.trunc(client_investment_amt/fb)
        investment_shares = (f'{client_name} has ${client_investment_amt} to invest and can buy {stock_buy_limit} shares of {stock_name} at the current price of ${fb}.')
        print (investment_shares)

    elif stock_name == 'Google':
        stock_buy_limit = math.trunc(client_investment_amt/google)
        investment_shares = (f'{client_name} has ${client_investment_amt} to invest and can buy {stock_buy_limit} shares of {stock_name} at the current price of ${google}.')
        print (investment_shares)

    elif stock_name == 'Msft':
        stock_buy_limit = math.trunc(client_investment_amt/msft)
        investment_shares = (f'{client_name} has ${client_investment_amt} to invest and can buy {stock_buy_limit} shares of {stock_name} at the current price of ${msft}.')
        print (investment_shares)

    # 1.5 TODO: Once you've calculated the number of stocks that can be purchased,
    # Use an f-string to print the result for the client, ala:
    # Alex has $5000 to invest and can buy 50 shares of Apple at the current price of $100.
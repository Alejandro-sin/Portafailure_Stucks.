
'''
Reference:

Construct a simple Portfolio class that has a collection of Stocks and a "Profit" method that receives 2 dates and returns the profit of the Portfolio between those dates. Assume each Stock has a "Price" method that receives a date and returns its price.

Bonus Track: make the Profit method return the "annualized return" of the portfolio between the given dates.
'''
import time


class Portafolio:
    # Collection of Stocks
    stocks = []


    def __init__(self):
        pass

    
    #Profit Method
    def profit(initial_date, final_date):
        
        # Each Stock has a price.
        profit = None
        annualized_return = None
        return profit, annualized_return


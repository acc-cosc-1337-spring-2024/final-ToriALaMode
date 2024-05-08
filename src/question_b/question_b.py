# Publicly traded stock reports.
# A report of stock purchase history for each stock (details below).

# Data:
# Stock list
# =Symbol
# AAPL
# CAT
# EK
# GOOG
# MSFT
# =Company Name
# Apple Inc
# Caterpillar
# Eastman Kodak
# Google
# Microsoft

# Implementation:

# 1-Create a class Stock with private variables symbol and company_name. (Create a constructor that accepts symbol and company_name)
# 2-Create a stock class function/method that returns symbol
# 3-Create a stock class function/method that returns company_name
# 4-Create a function stock_purchase_history.
#    a-Create 5 variables/instances of Stock with the values from the Stock List table above (AAP, CAT etc)
#    b-Add the 5 stock variables to a dictionary
#    c-Loop through the dictionary to display the list as displayed above in the table

# Tests:
# No Test cases.

# write functions here, don't add input('') statements here!
class Stock:
    def __init__(self, symbol, company_name): # Create a class Stock with private variables symbol and company_name. (Create a constructor that accepts symbol and company_name)
        self.__symbol = symbol
        self.__company_name = company_name

    def get_symbol(self): # Create a stock class function/method that returns symbol
        return self.__symbol

    def get_company_name(self): # Create a stock class function/method that returns company_name
        return self.__company_name

def stock_purchase_history(): # Create a function stock_purchase_history
    stock_list = {
        "AAPL": Stock("AAPL", "Apple Inc"), # Create 5 variables/instances of Stock with the values from the Stock List table above (AAP, CAT etc)
        "CAT": Stock("CAT", "Caterpillar"),
        "EK": Stock("EK", "Eastman Kodak"),
        "GOOG": Stock("GOOG", "Google"),
        "MSFT": Stock("MSFT", "Microsoft") # Add the 5 stock variables to a dictionary
    }

    for symbol, stock in stock_list.items(): #Loop through the dictionary to display the list as displayed above in the table
        print("Symbol:", stock.get_symbol())
        print("Company Name:", stock.get_company_name())
        print()

if __name__ == "__main__":
    stock_purchase_history()
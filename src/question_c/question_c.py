# Use classes for this question.
# Publicly traded stock reports.
# Example
# Stock  Report
# Company  Symbol    
# Microsoft  MSFT      

# Implementation:
# Create a Stock class with one constructor with symbol and company_name parameters, private attributes(variables) symbol and company_name, and public functions get_symbol 
# and get_company_name.
# write functions here, don't add input('') statements here!

class Stock:
    def __init__(self, symbol, company_name):
        self.__symbol = symbol
        self.__company_name = company_name

    def get_symbol(self):
        return self.__symbol

    def get_company_name(self):
        return self.__company_name


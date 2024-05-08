# Design a program that asks the user to enter a series of 5 numbers.
# The program should store the numbers in a list then display the following data:
# The lowest number in the list
# The highest number in the list
# The total of the numbers in the list
# The average of the numbers in the list
#write functions here, don't add input('') statements here!
def test_config():
    return True
def get_numbers():
    numbers = []
    for _ in range(5):
        num = float(input("Enter a number: "))
        numbers.append(num)
    return numbers
    
def get_lowest(numbers): # The lowest number in the list
    return min(numbers)
    
def get_highest(numbers): # The highest number in the list
    return max(numbers)

def get_total(numbers): # The total of the numbers in the list
    return sum(numbers)

def get_average(numbers): # The average of the numbers in the list
    return sum(numbers) / len(numbers)
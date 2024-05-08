# Main:

# 1. The program continues until the user opts out.
# 2. Create the following menu:
#      1-Display stock purchase history
#      2-Exit

#      Option 1 calls the stock_purchase_history function.
#      Option 3 exits the program
#add import
from question_b import stock_purchase_history

def display_menu():
    print("Menu:")
    print("1. Display stock purchase history")
    print("2. Exit")

def main():
    while True:
        display_menu()
        option = input("Enter your choice: ")
        if option == "1": # Option 1 calls the stock_purchase_history function.
            stock_purchase_history()
        elif option == "2": # Option 3 exits the program (assuming this is typo? made it option 2)
            print("Exiting the program.")
            break
        else:
            print("Invalid option. Please try again.") #The program continues until the user opts out.

if __name__ == "__main__":
    main()
# Main:
# 1- Create a loop that will continue until the user opts out.
# 2- Call the create_multiplication table, save the return values to a local variable
# 3- Call the display_mulitiplication table function, use the local variable as its function argument
#     The list will display
# 4-Don't forget to ask the user if they want to continue or quit the program 
# # write functions here, don't add input('') statements here!
#add import
from question_d import create_multiplication_table
from question_d import display_multiplication_table


def main():
    while True:
        multiplication_table = create_multiplication_table()
        display_multiplication_table(multiplication_table)
        
        choice = input("Do you want to continue? (yes/no): ").lower()
        if choice != 'yes':
            print("Closing out of the table.")
            break

if __name__ == "__main__":
    main()
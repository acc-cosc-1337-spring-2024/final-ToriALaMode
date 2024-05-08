# Problem
# Create a multiplication table using lists
# 1 2 3 4   5   6    7   8   9 10
# 2 4 6 8 10 12 14 16 18 20
# 3 6 9 12 15 18 21 24 27 30
# 4 8 12 16 20 24 28 32 36 40
# 5 10 15 20 25 30 35 40 45 50

# Implementation:
# 1-Create a create_mulitiplication_table function that returns a list.
#    a-Create an empty list
#    b-Use nested looping to create the above table with lists
#        Use multiplication to derive the values for each list element
#    c-return the list

# 2-Create a display_multiplication_table that displays a table and accepts a list parameter
#    1-Loop through the list
#    2-Display the table as displayed above

# Tests:
# no tests
def create_multiplication_table():
    table = []
    for i in range(1, 6):
        row = []
        for j in range(1, 11):
            row.append(i * j)
        table.append(row)
    return table

def display_multiplication_table(table):
    for row in table:
        print(" ".join(map(str, row)))

if __name__ == "__main__":
    multiplication_table = create_multiplication_table()
    display_multiplication_table(multiplication_table)
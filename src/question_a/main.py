#add import
from question_a import get_average, get_highest, get_lowest, get_numbers, get_total
def main():
    numbers = get_numbers()
    print("Lowest number:", get_lowest(numbers))
    print("Highest number:", get_highest(numbers))
    print("Total:", get_total(numbers))
    print("Average:", get_average(numbers))

if __name__ == "__main__":
    main()
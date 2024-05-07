#add import
from src.qustion_a import get_numbers
from src.qustion_a import get_highest
from src.qustion_a import get_total
from src.qustion_a import get_average

def main():
    numbers = get_numbers()
    print("Lowest number:", get_lowest(numbers))
    print("Highest number:", get_highest(numbers))
    print("Total:", get_total(numbers))
    print("Average:", get_average(numbers))

if __name__ == "__main__":
    main()

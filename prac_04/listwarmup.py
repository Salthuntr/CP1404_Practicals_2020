def main():
    numbers = [3,1,4,1,5,9,2]
    print(numbers[0])
    print(numbers[-1])
    print(numbers[3])
    print(numbers[:-1])
    print(numbers[3:4])
    print(5 in numbers)
    print(7 in numbers)
    print("3" in numbers)
    print(numbers + [6,5,3])

    # numbers[0] wields 3
    # numbers[-1] yields 2
    # numbers[3] yields 1
    # numbers[:-1] yields [3,1,4,1,5,9]
    # numbers[3:4] yields [1]
    # 5 in numbers yields True
    # 7 in numbers yields False
    # "3" in numbers yields False
    # numbers + [6,5,3] yields [3,1,4,1,5,9,2,6,5,3]

    # Change the first element of numbers to "ten"
    # numbers[0] = "ten"
    # Change the last element of numbers to 1
    # numbers[-1] = 1
    # Get all the elements from numbers except the first two
    # numbers[2:]
    # Check if 9 is an element of numbers
    # 9 in numbers


main()
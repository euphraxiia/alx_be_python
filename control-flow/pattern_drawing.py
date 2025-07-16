def main():
    try:
        size = int(input("Enter the size of the pattern: "))
        if size <= 0:
            print("Please enter a positive integer.")
            return

        row = 0
        while row < size:
            for col in range(size):
                print("*", end="")
            print()  # move to the next line after a row is printed
            row += 1
    except ValueError:
        print("Please enter a valid integer.")

if __name__ == "__main__":
    main()

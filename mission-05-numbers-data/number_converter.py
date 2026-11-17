def main():
    try:
        decimal_number = int(input("Enter a decimal integer: "), 10)
    except ValueError:
        print("Please enter a valid decimal integer.")
        return

    print(f"Binary: {bin(decimal_number)}")
    print(f"Hexadecimal: {hex(decimal_number)}")


if __name__ == "__main__":
    main()

def print_formatted(number):
    # 1. Determine the required width for padding.
    # This is the length of the binary representation of the input number.
    width = len(bin(number)[2:])

    # 2. Loop from 1 to the given number (inclusive).
    for i in range(1, number + 1):
        # 3. For each number, convert to the four bases.
        #    - Remove prefixes like '0o', '0x', '0b' using slicing [2:].
        #    - Convert hexadecimal to uppercase.
        deci = str(i)
        octa = oct(i)
        hexa = hex(i).upper()
        bina = bin(i)

        # 4. Print the formatted string.
        #    - The f-string handles the right-alignment and padding for each value.
        #    - e.g., f"{deci:>{width}}" pads the decimal string to the calculated width.
        print(f"{deci:>{width}} {octa:>{width}} {hexa:>{width}} {bina:>{width}}")

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
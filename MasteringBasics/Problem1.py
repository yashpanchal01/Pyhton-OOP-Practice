def most_frequent_char(input_string):
    """
    Finds the most frequent character in a string.
    If there's a tie, it returns the one that appears first.
    """
    # 1. Handle the edge case of an empty string
    if not input_string:
        return None

    # 2. Create a dictionary to store character counts
    counts = {}
    for char in input_string:
        # Increment the count for each character. .get() handles new characters gracefully.
        # The "long way" to do it
        if char in counts:
            # If the character is already a key, increment its value
            counts[char] = counts[char] + 1
        else:
            # If it's a new character, add it to the dictionary with a value of 1
            counts[char] = 1

    # 3. Find the character with the highest count
    # The `max()` function can find the key in a dictionary that has the maximum value
    # by using the `key` argument. `key=counts.get` tells it to compare the values,
    # not the keys.
    most_frequent = max(counts, key=counts.get)

    return most_frequent

# --- Examples ---
print(f"'programming' -> '{most_frequent_char('programming')}'")
print(f"'hello world' -> '{most_frequent_char('hello world')}'")
print(f"'banana'      -> '{most_frequent_char('banana')}'")
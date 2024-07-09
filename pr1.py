def demonstrate_string_functions():
    # Sample string
    sample_str = "Hello, World!"

    # 1. Length of the string
    print(f"Length of the string: {len(sample_str)}")

    # 2. Convert to uppercase
    print(f"Uppercase: {sample_str.upper()}")

    # 3. Convert to lowercase
    print(f"Lowercase: {sample_str.lower()}")

    # 4. Replace a substring
    print(f"Replace 'World' with 'Python': {sample_str.replace('World', 'Python')}")

    # 5. Find a substring
    print(f"Find 'World': {sample_str.find('World')}")

    # 6. Check if the string starts with a substring
    print(f"Starts with 'Hello': {sample_str.startswith('Hello')}")

    # 7. Check if the string ends with a substring
    print(f"Ends with '!': {sample_str.endswith('!')}")

    # 8. Split the string into a list of words
    print(f"Split into words: {sample_str.split()}")

    # 9. Join a list of words into a string
    words_list = ['Join', 'these', 'words']
    print(f"Join list into string: {' '.join(words_list)}")

    # 10. Strip whitespace from the string
    sample_str_with_whitespace = "   Hello, World!   "
    print(f"Original string with whitespace: '{sample_str_with_whitespace}'")
    print(f"String after strip: '{sample_str_with_whitespace.strip()}'")

    # 11. Check if the string is alphanumeric
    alphanumeric_str = "Hello123"
    print(f"Is '{alphanumeric_str}' alphanumeric? {alphanumeric_str.isalnum()}")

    # 12. Check if the string is alphabetic
    alphabetic_str = "Hello"
    print(f"Is '{alphabetic_str}' alphabetic? {alphabetic_str.isalpha()}")

    # 13. Check if the string contains only digits
    digit_str = "12345"
    print(f"Is '{digit_str}' digit? {digit_str.isdigit()}")

    # 14. Count the occurrences of a substring
    print(f"Count occurrences of 'o': {sample_str.count('o')}")

    # 15. Center the string with a specified width and fill character
    print(f"Center string with width 20 and fill character '*': {sample_str.center(20, '*')}")

if __name__ == "__main__":
    demonstrate_string_functions()

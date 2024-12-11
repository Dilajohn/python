#Write a function to check if a given string is a palindrome (reads the same backward as forward).
def is_palindrome(string):
    """
    Check if a string is a palindrome.
    
    Args:
        string (str): The string to check.
    
    Returns:
        bool: True if the string is a palindrome, False otherwise.
    """
    # Remove spaces and convert to lowercase
    cleaned_string = string.replace(" ", "").lower()
    return cleaned_string == cleaned_string[::-1]

# Test the function
print(is_palindrome("madam"))           # Output: True
print(is_palindrome("hello"))           # Output: False
print(is_palindrome("A man a plan a canal Panama"))  # Output: True

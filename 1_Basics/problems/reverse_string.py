"""Description:
Write a function that takes a string as input and returns the string reversed.

Example:
    Input: "hello"
    Output: "olleh"

Why It's Important:
Reversing a string is a fundamental problem that helps with understanding string manipulation and basic operations. It is useful for getting familiar with loops and string indexing.

"""




# Python Example Solution:

def reverse_string(s: str) -> str:
    return s[::-1]

# Example usage
print(reverse_string("hello"))  # Output: "olleh"

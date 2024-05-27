def find_first_repeating_character(s):
    char_count = {}
    
    for char in s:
        # Update character count in dictionary
        char_count[char] = char_count.get(char, 0) + 1
        
        # Check if the character is repeating
        if char_count[char] == 2:
            # Find the memory address of the first occurrence of the repeating character
            memory_address = id(char)
            return char, memory_address
    
    # If no repeating character found, return None
    return None

# Example usage:
string_input = input("Enter a string: ")
result = find_first_repeating_character(string_input)
if result:
    char, memory_address = result
    print("First repeating character:", char)
    print("Memory address:", memory_address)
else:
    print("No repeating character found.")
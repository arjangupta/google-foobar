def solution(s):
    # Parameter s is the plain text word
    
    output_str = ""
    
    if type(s) is not str:
        return output_str
    
    for char in s:
        output_str += braille_encode(char)
    
    return output_str

def braille_encode(char):
    # The encoding pattern followed here is given at https://braillebug.org/braillebug_answers.asp#w

    # Known data for encoding
    capital_char_prefix = "000001"
    space_char_prefix   = "000000"
    letter_arr = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','x','y','z']
    w = "010111" # w is an exception to the pattern. Binary string is found by: ( '0' + bin(22 + 1)[2:] )
    first10_letter_values = [32, 48, 36, 38, 34, 52, 54, 50, 20, 22]

    # Begin building encoded char
    if char == ' ':
        return space_char_prefix

    encoded_str = ""
    if char.isupper():
        encoded_str += capital_char_prefix
        char = char.lower()

    # Find which row and column the character belongs to
    letter_column = letter_arr.index(char) % len(first10_letter_values)  
    letter_row    = letter_arr.index(char) / len(first10_letter_values)
    # The 3rd dot is raised if it's in the second row, and the 3rd and 6th dot is raised in the third row
    letter_decimal_value = first10_letter_values[letter_column]
    if letter_row == 1:
        letter_decimal_value += 8
    elif letter_row == 2:
        letter_decimal_value += (8 + 1)
    
    letter_binary_value = bin(letter_decimal_value)[2:] # omit the '0b' prefix

    # Ensure that the binary string has a length of 6
    if len(letter_binary_value) < 6:
        number_of_zeros_to_prefix = 6 - len(letter_binary_value)
        letter_binary_value = ('0' * number_of_zeros_to_prefix) + letter_binary_value

    encoded_str += letter_binary_value

    return encoded_str

def main():
    # Read file without new lines
    test_cases_file = open("test_cases.txt")
    line_arr = [line[:-1] for line in test_cases_file]

    # Run all three test cases
    for i in range(0, len(line_arr), 2):
        text_str   = line_arr[i]
        solved_str = solution( text_str )
        binary_str = line_arr[i + 1]
        if solved_str == binary_str:
            print "TEST CASE #" + i + "PASSED"
        else:
            print "TEST CASE #" + i + "FAILED"

if __name__ == "__main__":
    main()
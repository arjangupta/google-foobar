def reverse_engineer(text_str, binary_str):
    # Check input str
    for char in binary_str:
        if char != '0' and char != '1':
            print("Something's wrong with your damn input.")
            return
    
    print ""
    print "--------- TEST CASE ---------"
    print "The given text string is: " + text_str
    print "Length of the text string is", len(text_str)
    print "Length of the binary string is", len(binary_str)
    print "The binary string length / 6 is", ( len(binary_str) / 6 )
    
    # Ensure binary_str vs text_str makes sense
    if ( len(binary_str) / 6 ) < len(text_str):
        print("Error: the input string length / 6 is less than the text string length.")
        return
    
    print "Now writing the corresponding char encodings to file"

    encodings_dict = {}
    i = 0
    for char in text_str:
        if char.isupper():
            encodings_dict["cap_char"] = binary_str[i:(i+6)]
            i += 6

        if char == ' ':
            encodings_dict["space_char"] = binary_str[i:(i+6)]
        else:
            encodings_dict[char.lower()] = binary_str[i:(i+6)]
        i += 6
    
    non_letter_encoding = {}
    for key in sorted(encodings_dict.keys()):
        if key != "space_char" and key != "cap_char":
            print key + ": " + encodings_dict[key] + " =", int(encodings_dict[key], base=2)
        else:
            non_letter_encoding[key] = encodings_dict[key]
    
    print ""
    for key in non_letter_encoding:
        print key + ": " + encodings_dict[key]

def main():
    # Read file without new lines
    test_cases_file = open("test_cases.txt")
    line_arr = [line[:-1] for line in test_cases_file]

    # Reverse engineer for all three test cases
    for i in range(0, len(line_arr), 2):
        reverse_engineer( line_arr[i], line_arr[i + 1] )

if __name__ == "__main__":
    main()
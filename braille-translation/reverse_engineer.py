def reverse_engineer(text_str, input_str):
    # Check input str
    for char in input_str:
        if char != '0' and char != '1':
            print("Something's wrong with your damn input.")
            return
    
    print "--------- TEST CASE ---------"
    print "The given text string is: " + text_str
    print "Length of the text string is", len(text_str)
    print "Length of the binary string is", len(input_str)
    print "The binary string length / 6 is", ( len(input_str) / 6)
    
    if ( len(input_str) / 6 ) < len(text_str):
        print("Error: the input string length / 6 is less than the text string length.")
        return
    
    print("Now printing the corresponding char encodings:")

    encodings_dict = {}
    i = 0
    for char in text_str:
        if char.isupper():
            encodings_dict["cap_char"] = input_str[i:(i+6)]
            i += 6

        if char == ' ':
            encodings_dict["space_char"] = input_str[i:(i+6)]
        else:
            encodings_dict[char.lower()] = input_str[i:(i+6)]
        i += 6
    
    for key in sorted(encodings_dict.keys()):
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
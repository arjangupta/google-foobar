def reverse_engineer(input_str, text_str):

    # Check input str
    for char in input_str:
        if char != '0' and char != '1':
            print("Something's wrong with your damn input.")
            return
    
    print("The given text string is: " + text_str)
    print("Length of the text string is", len(text_str))
    print("Length of the input string is", len(input_str))
    print("The input string length / 6 is", ( len(input_str) / 6) )
    
    if ( len(input_str) / 6 ) < len(text_str):
        print("Error: the input string length / 6 is less than the text string length.")
        return
    
    print("Now printing the corresponding char encodings:")

    i = 0
    for char in text_str:
        if char.isupper():
            print("cap_char: " + input_str[i:(i+6)])
            i += 6
        print(char.lower() + ': '  + input_str[i:(i+6)])
        i += 6

def main():
    text_str_arr = []
    input_str_arr = []
    
    for i in range(3):
        text_str[i] = input()
        input_str[i] = input()
    
    for i in range(3):
        reverse_engineer(text_str[i], input_str[i])

if __name__ == "__main__":
    main()
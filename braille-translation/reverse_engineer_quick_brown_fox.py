# import sys

def main():
    input_str = input()

    for char in input_str:
        if char != '0' and char != '1':
            print("Something's wrong with your damn input.")
            return
    
    text_str = "The quick brown fox jumps over the lazy dog"
    print('\nI assume this means "' + text_str + '"')
    print("Length of the text string is", len(text_str))
    print("Length of the input string is", len(input_str))
    print("The input string length / 6 is", ( len(input_str) / 6) )
    
    if ( len(input_str) / 6) < len(text_str):
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

if __name__ == "__main__":
    main()
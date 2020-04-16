def solution(s):
    # Parameter s is the plain text word
    
    output_str = ""
    
    if type(s) is not str:
        return output_str
    
    for char in str:
        if char == ' ':
            output_str += "000000"
        elif char.isUpper():
            output_str += "000001"
        else:
            
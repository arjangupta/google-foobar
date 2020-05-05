def solution(start, length):
    current_total  = 0
    current_length = length
    current_start  = start
    for i in range(length):
        row_total = summation_of_xors(current_start - 1) ^ summation_of_xors(current_start + current_length - 1)
        current_total  ^= row_total
        current_start  += length
        current_length -= 1
    return current_total

def summation_of_xors(n):
    remainder = n % 4
    if remainder == 0:
        return n
    elif remainder == 1:
        return 1
    elif remainder == 2:
        return n + 1
    elif remainder == 3:
        return 0

def test_case(start, length, expected_result):
    print "Test for ( " + str(start) + ", " + str(length) + " ) ",
    if expected_result != solution(start, length):
        print "FAILED."
    else:
        print "passed."

def main():
    # Run the test cases
    test_case(0, 3, 2)
    test_case(17, 4, 14)
    test_case(1, 1, 1)

if __name__ == "__main__":
    main()
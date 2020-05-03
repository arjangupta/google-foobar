def solution(start, length):
    return 100

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

if __name__ == "__main__":
    main()
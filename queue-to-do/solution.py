def solution(start, length):
    partition_position  = length
    current_xor_result  = 0
    current_employee_id = start
    while partition_position > 0:
        for employee_position in range(length):
            if employee_position < partition_position:
                current_xor_result ^= current_employee_id
            current_employee_id += 1
        partition_position -= 1
    return current_xor_result

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